#!/usr/bin/env python3
"""
Script to remove unused references from markdown files.
Based on the analysis results from find_unused_references_summary.py
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


def remove_unused_references(content, unused_refs):
    """Remove unused references from the content."""
    if not unused_refs:
        return content

    # Find the references section
    ref_section_start = content.find("## **منابع**")
    if ref_section_start == -1:
        ref_section_start = content.find("---\n\n## **منابع**")

    if ref_section_start == -1:
        return content

    # Split content into main content and references
    main_content = content[:ref_section_start]
    ref_section = content[ref_section_start:]

    # Split references into lines
    lines = ref_section.split("\n")
    filtered_lines = []

    for line in lines:
        # Check if this line starts with a reference number that should be removed
        match = re.match(r"^\[(\d+)\]", line.strip())
        if match:
            ref_num = int(match.group(1))
            if ref_num not in unused_refs:
                filtered_lines.append(line)
        else:
            # Keep non-reference lines (headers, empty lines, etc.)
            filtered_lines.append(line)

    # Rejoin the content
    return main_content + "\n".join(filtered_lines)


def process_file(file_path):
    """Process a single markdown file to remove unused references."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        citations = extract_citations_from_content(content)
        references = extract_references_from_list(content)
        unused_refs = references - citations

        if not unused_refs:
            print(f"✅ {file_path}: No unused references to remove")
            return

        # Remove unused references
        new_content = remove_unused_references(content, unused_refs)

        # Write back to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"🗑️  {file_path}: Removed {len(unused_refs)} unused references")

    except Exception as e:
        print(f"❌ ERROR processing {file_path}: {e}")


def main():
    """Main function to process all section files in chapters 1-3."""
    chapters = [
        "01-ai-revolution-in-biology",
        "02-how-machines-learn",
        "03-art-of-pattern-recognition",
    ]
    sections = ["01", "02", "03", "04", "05"]

    print("=" * 80)
    print("REMOVING UNUSED REFERENCES FROM CHAPTERS 1-3")
    print("=" * 80)
    print()

    total_processed = 0

    for chapter in chapters:
        for section in sections:
            pattern = f"{chapter}/{section}-*.md"
            files = glob.glob(pattern)

            for file_path in files:
                # Skip introduction files (00-*.md)
                if "00-" in file_path:
                    continue

                process_file(file_path)
                total_processed += 1

    print()
    print("=" * 80)
    print(f"PROCESSING COMPLETE: {total_processed} files processed")
    print("=" * 80)


if __name__ == "__main__":
    main()
