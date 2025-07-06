#!/usr/bin/env python3
"""
Simplified script to find unused references in markdown files.
Focuses on summary statistics and unused reference numbers.
"""

import os
import re
import glob


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
            "citations": len(citations),
            "references": len(references),
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

    # Print summary results
    print("=" * 80)
    print("SUMMARY OF UNUSED REFERENCES IN CHAPTERS 1-3")
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
        print(
            f"   Citations: {result['citations']}, References: {result['references']}"
        )

        if result["unused_refs"]:
            print(f"   ❌ UNUSED: {len(result['unused_refs'])} references")
            print(f"      Numbers: {result['unused_refs']}")
            total_unused += len(result["unused_refs"])

        if result["missing_refs"]:
            print(f"   ⚠️  MISSING: {len(result['missing_refs'])} references")
            total_missing += len(result["missing_refs"])

        if not result["unused_refs"] and not result["missing_refs"]:
            print(f"   ✅ All references are properly used")

        print()

    print("=" * 80)
    print(f"TOTAL SUMMARY:")
    print(f"Total unused references: {total_unused}")
    print(f"Total missing references: {total_missing}")
    print("=" * 80)


if __name__ == "__main__":
    main()
