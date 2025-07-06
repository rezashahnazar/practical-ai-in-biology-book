#!/usr/bin/env python3
"""
Script to find unused references in markdown files.
Compares reference citations in content with reference list at the end.
"""

import os
import re
import glob
from pathlib import Path


def extract_citations_from_content(content):
    """Extract all citation numbers from the content (before references section)."""
    # Find the references section
    ref_section_start = content.find("## **منابع**")
    if ref_section_start == -1:
        ref_section_start = content.find("---\n\n## **منابع**")

    if ref_section_start == -1:
        # If no references section found, search entire content
        content_to_search = content
    else:
        # Only search content before references section
        content_to_search = content[:ref_section_start]

    # Find all citation patterns like [1], [2], [10], etc.
    citations = re.findall(r"\[(\d+)\]", content_to_search)
    return set(int(citation) for citation in citations)


def extract_references_from_list(content):
    """Extract reference numbers from the references section."""
    # Find the references section
    ref_section_start = content.find("## **منابع**")
    if ref_section_start == -1:
        ref_section_start = content.find("---\n\n## **منابع**")

    if ref_section_start == -1:
        return set()

    # Get the references section
    ref_section = content[ref_section_start:]

    # Find all reference patterns like [1] https://..., [2] https://..., etc.
    references = re.findall(r"^\[(\d+)\]", ref_section, re.MULTILINE)
    return set(int(ref) for ref in references)


def analyze_file(file_path):
    """Analyze a single markdown file for unused references."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        citations = extract_citations_from_content(content)
        references = extract_references_from_list(content)

        unused_refs = references - citations
        missing_refs = citations - references

        return {
            "file": file_path,
            "citations": sorted(citations),
            "references": sorted(references),
            "unused_refs": sorted(unused_refs),
            "missing_refs": sorted(missing_refs),
        }
    except Exception as e:
        return {"file": file_path, "error": str(e)}


def main():
    """Main function to analyze all section files in chapters 1-3."""
    chapters = [
        "01-ai-revolution-in-biology",
        "02-how-machines-learn",
        "03-art-of-pattern-recognition",
    ]
    sections = ["01", "02", "03", "04", "05"]

    all_results = []

    for chapter in chapters:
        for section in sections:
            pattern = f"{chapter}/{section}-*.md"
            files = glob.glob(pattern)

            for file_path in files:
                # Skip introduction files (00-*.md)
                if "00-" in file_path:
                    continue

                result = analyze_file(file_path)
                all_results.append(result)

    # Print results
    print("=" * 80)
    print("ANALYSIS OF UNUSED REFERENCES IN CHAPTERS 1-3")
    print("=" * 80)
    print()

    total_unused = 0
    total_missing = 0

    for result in all_results:
        if "error" in result:
            print(f"❌ ERROR in {result['file']}: {result['error']}")
            continue

        file_name = os.path.basename(result["file"])
        chapter_name = os.path.dirname(result["file"])

        print(f"📄 {chapter_name}/{file_name}")
        print(f"   Citations found: {len(result['citations'])}")
        print(f"   References listed: {len(result['references'])}")

        if result["unused_refs"]:
            print(f"   ❌ UNUSED REFERENCES: {result['unused_refs']}")
            total_unused += len(result["unused_refs"])

        if result["missing_refs"]:
            print(f"   ⚠️  MISSING REFERENCES: {result['missing_refs']}")
            total_missing += len(result["missing_refs"])

        if not result["unused_refs"] and not result["missing_refs"]:
            print(f"   ✅ All references are properly used")

        print()

    print("=" * 80)
    print(f"SUMMARY:")
    print(f"Total unused references: {total_unused}")
    print(f"Total missing references: {total_missing}")
    print("=" * 80)

    # Generate detailed report for unused references
    print("\nDETAILED UNUSED REFERENCES REPORT:")
    print("-" * 50)

    for result in all_results:
        if "error" not in result and result["unused_refs"]:
            file_name = os.path.basename(result["file"])
            chapter_name = os.path.dirname(result["file"])
            print(f"\n{chapter_name}/{file_name}:")
            print(f"  Unused references: {result['unused_refs']}")

            # Show the actual unused reference lines
            try:
                with open(result["file"], "r", encoding="utf-8") as f:
                    content = f.read()

                ref_section_start = content.find("## **منابع**")
                if ref_section_start == -1:
                    ref_section_start = content.find("---\n\n## **منابع**")

                if ref_section_start != -1:
                    ref_section = content[ref_section_start:]
                    lines = ref_section.split("\n")

                    for line in lines:
                        for ref_num in result["unused_refs"]:
                            if line.strip().startswith(f"[{ref_num}]"):
                                print(f"    [{ref_num}] {line.strip()}")
                                break
            except Exception as e:
                print(f"    Error reading file: {e}")


if __name__ == "__main__":
    main()
