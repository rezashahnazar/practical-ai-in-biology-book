#!/usr/bin/env python3
"""
Build a single Markdown file for the book by concatenating:
1) README.md (as front matter)
2) All Markdown files referenced in README.md (in order of appearance)
3) Any remaining Markdown files not in README.md (sorted alphabetically by path)

Output: book.md in the project root.
"""

from __future__ import annotations

import os
import re
from collections import OrderedDict
from typing import Iterable, List, Set


def read_text_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def write_text_file(file_path: str, content: str) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def extract_markdown_links(markdown_text: str) -> List[str]:
    """Return target URLs from Markdown links of the form [text](url).

    Only returns the raw URL targets. Does not resolve against any base path.
    """
    # This regex aims to match standard Markdown link syntax [label](target)
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    return link_pattern.findall(markdown_text)


def normalize_md_path(project_root: str, maybe_relative: str) -> str:
    """Turn a README-relative path into an absolute, normalized path.

    - Strips URL fragments after '#'
    - Joins relative to project root
    - Normalizes and returns absolute path
    """
    no_fragment = maybe_relative.split("#", 1)[0]
    joined = os.path.join(project_root, no_fragment)
    return os.path.normpath(os.path.abspath(joined))


def list_all_markdown_files(project_root: str) -> List[str]:
    markdown_files: List[str] = []
    excluded_dirs: Set[str] = {
        ".git",
        ".hg",
        ".svn",
        ".venv",
        "node_modules",
        "venv",
        "env",
        "__pycache__",
    }
    for dirpath, dirnames, filenames in os.walk(project_root):
        # prune excluded directories
        dirnames[:] = [
            d for d in dirnames if d not in excluded_dirs and not d.startswith(".")
        ]
        for filename in filenames:
            if filename.lower().endswith(".md"):
                markdown_files.append(
                    os.path.normpath(os.path.abspath(os.path.join(dirpath, filename)))
                )
    return markdown_files


def ordered_unique(sequence: Iterable[str]) -> List[str]:
    seen = OrderedDict()
    for item in sequence:
        if item not in seen:
            seen[item] = None
    return list(seen.keys())


def anchor_id_for_rel_path(rel_path: str) -> str:
    """Create a deterministic HTML anchor id from a project-relative path.

    Example: "01-ai-revolution-in-biology/00-introduction.md" ->
             "01-ai-revolution-in-biology-00-introduction"
    """
    # remove extension
    if rel_path.lower().endswith(".md"):
        rel_path = rel_path[: -len(".md")]
    # normalize separators to '-'
    anchor = rel_path.replace(os.sep, "-")
    # collapse spaces to '-'
    anchor = re.sub(r"\s+", "-", anchor)
    # allow only letters, numbers, dash, underscore and Persian letters common in repo
    anchor = re.sub(r"[^0-9A-Za-z_\-\u0600-\u06FF]", "-", anchor)
    # collapse multiple dashes
    anchor = re.sub(r"-+", "-", anchor).strip("-")
    return anchor


def rewrite_readme_links_to_internal(readme_text: str, project_root: str) -> str:
    """Rewrite links in README that point to .md files into internal anchors.

    Keeps non-.md links intact. If a link has a fragment, it is ignored and we
    link to the start of the corresponding included file.
    """
    link_pattern = re.compile(r"(\[([^\]]+)\])\(([^)]+)\)")

    def replace(match: re.Match) -> str:
        label_with_brackets = match.group(1)
        target = match.group(3)
        # Only rewrite .md links
        target_no_fragment = target.split("#", 1)[0]
        if not target_no_fragment.lower().endswith(".md"):
            return match.group(0)
        # Build absolute then project-relative path
        try:
            abs_target = normalize_md_path(project_root, target_no_fragment)
            rel_target = os.path.relpath(abs_target, project_root)
        except Exception:
            return match.group(0)
        anchor_id = anchor_id_for_rel_path(rel_target)
        return f"{label_with_brackets}(#{anchor_id})"

    return link_pattern.sub(replace, readme_text)


def build_book() -> str:
    project_root = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(project_root, "README.md")
    output_path = os.path.join(project_root, "book.md")

    if not os.path.exists(readme_path):
        raise FileNotFoundError(f"README.md not found at {readme_path}")

    readme_text_raw = read_text_file(readme_path)

    # 1) Start with README.md itself
    ordered_files: List[str] = [readme_path]

    # 2) Files referenced in README.md (filter only .md)
    link_targets = extract_markdown_links(readme_text_raw)
    toc_files: List[str] = []
    for target in link_targets:
        if target.lower().endswith(".md"):
            toc_files.append(normalize_md_path(project_root, target))

    # Deduplicate while preserving order
    toc_files = ordered_unique(toc_files)

    # Exclude README if it appeared via link (unlikely here)
    toc_files = [p for p in toc_files if os.path.basename(p).lower() != "readme.md"]

    # 3) Any remaining markdown files not included above
    all_md = list_all_markdown_files(project_root)

    # Exclude output file in case it already exists from previous builds
    all_md = [p for p in all_md if os.path.abspath(p) != os.path.abspath(output_path)]

    # Combine in final order
    ordered_files.extend(toc_files)

    already_included: Set[str] = set(ordered_files)
    remaining_files = sorted([p for p in all_md if p not in already_included])
    ordered_files.extend(remaining_files)

    # Concatenate contents with clear separators
    parts: List[str] = []
    for idx, file_path in enumerate(ordered_files):
        rel_path = os.path.relpath(file_path, project_root)
        parts.append(f"\n\n<!-- File: {rel_path} -->\n\n")
        # For README.md, rewrite its links to internal anchors
        if os.path.abspath(file_path) == os.path.abspath(readme_path):
            rewritten = rewrite_readme_links_to_internal(readme_text_raw, project_root)
            parts.append(rewritten.rstrip() + "\n")
        else:
            # Insert an anchor target before each included file
            anchor_id = anchor_id_for_rel_path(rel_path)
            parts.append(f'<a id="{anchor_id}"></a>\n\n')
            parts.append(read_text_file(file_path).rstrip() + "\n")

    write_text_file(output_path, "".join(parts).lstrip())
    return output_path


if __name__ == "__main__":
    out = build_book()
    print(f"Created: {out}")
