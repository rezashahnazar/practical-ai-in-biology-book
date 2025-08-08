#!/usr/bin/env python3
"""
Export book.md to a well-styled PDF using Playwright.

Features:
- RTL body text (right-aligned); LTR code blocks (left-aligned)
- Mermaid diagrams rendered client-side
- Images included and scaled to page
- Internal links preserved
- Prevent overflow via CSS and wrapping rules
- Uses Vazirmatn Google font for body text

Requires: playwright (Chromium installed), markdown-it-py, mdit-py-plugins, jinja2

Run: uv run python export_pdf.py
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from jinja2 import Template
from markdown_it import MarkdownIt
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.deflist import deflist_plugin
from mdit_py_plugins.tasklists import tasklists_plugin
from mdit_py_plugins.attrs import attrs_plugin
from playwright.sync_api import sync_playwright


PROJECT_ROOT = Path(__file__).resolve().parent
INPUT_MD = PROJECT_ROOT / "book.md"
OUTPUT_PDF = PROJECT_ROOT / "book.pdf"


def build_markdown_renderer() -> MarkdownIt:
    md = (
        MarkdownIt("commonmark", {"html": True, "linkify": True, "typographer": True})
        .use(footnote_plugin)
        .use(deflist_plugin)
        .use(tasklists_plugin, enabled=True)
        .use(attrs_plugin)
    )

    # Enable GFM-style tables where supported by markdown-it-py
    try:
        md.enable("table")
    except Exception:
        pass

    # Anchors for headings (use slug generation similar to GitHub)
    md.use(anchors_plugin, permalink=False)

    # Transform ```mermaid fences into <div class="mermaid">...</div>
    fence = md.renderer.rules.get("fence")

    def fence_override(tokens, idx, options, env):  # type: ignore[no-untyped-def]
        token = tokens[idx]
        info_raw = (token.info or "").strip()
        lang = info_raw.split()[0].lower() if info_raw else ""
        if lang == "mermaid":
            content = token.content
            return f'<div class="mermaid">\n{content}\n</div>'
        if fence:
            return fence(tokens, idx, options, env)  # default
        # fallback
        return f"<pre><code>{md.utils.escapeHtml(token.content)}</code></pre>"

    md.renderer.rules["fence"] = fence_override
    return md


HTML_TEMPLATE = Template(
    r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{{ title }}</title>
  <!-- Base href for resolving relative assets (images) from filesystem -->
  <base href="{{ base_href }}" />

  <!-- Vazirmatn font -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;700&display=swap" rel="stylesheet">

  <!-- Mermaid -->
  <script defer src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>

  <style>
    @page {
      size: A4;
      margin: 12mm;
    }

    html, body {
      font-family: 'Vazirmatn', system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, 'Apple Color Emoji', 'Segoe UI Emoji';
      font-size: 12pt;
      color: #111;
      background: white;
      direction: rtl;
      text-align: right;
      line-height: 1.6;
      overflow-wrap: anywhere;
    }

    h1, h2, h3, h4, h5, h6 {
      break-after: avoid-page;
      break-inside: avoid;
      page-break-after: avoid;
      line-height: 1.3;
    }

    p, ul, ol, li, blockquote, table, pre, code, .mermaid, img, figure {
      break-inside: avoid-page;
      page-break-inside: avoid;
    }

    p { margin: 0.4em 0; }

    a { color: #0b57d0; text-decoration: none; }
    a:hover { text-decoration: underline; }

    /* Code blocks LTR */
    pre, code, pre code {
      direction: ltr;
      text-align: left;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;
      white-space: pre-wrap; /* wrap to avoid overflow */
      word-break: break-word;
      background: #f6f8fa;
    }
    pre {
      padding: 10px 12px;
      border-radius: 6px;
      overflow: hidden;
    }

    /* Tables */
    table { width: 100%; border-collapse: collapse; table-layout: fixed; }
    th, td { border: 1px solid #ddd; padding: 6px; word-break: break-word; }
    th { background: #f3f4f6; }

    /* Images */
    img { max-width: 100%; height: auto; }

    /* Mermaid diagrams are LTR */
    .mermaid { direction: ltr; text-align: center; }

    /* Headings spacing */
    h1 { font-size: 1.8em; margin: 0.8em 0 0.4em; }
    h2 { font-size: 1.6em; margin: 0.7em 0 0.4em; }
    h3 { font-size: 1.35em; margin: 0.6em 0 0.3em; }
  </style>
</head>
<body>
  <main id="content">
    {{ body|safe }}
  </main>

  <script>
    // Ensure Mermaid renders and fonts are loaded before printing
    (function() {
      function waitForMermaid() {
        return new Promise((resolve) => {
          if (window.mermaid) {
            try {
              window.mermaid.initialize({ startOnLoad: false, securityLevel: 'loose' });
              window.mermaid.run({ querySelector: '.mermaid' }).then(() => resolve()).catch(() => resolve());
            } catch (e) { resolve(); }
          } else {
            resolve();
          }
        });
      }

      (async () => {
        try { await document.fonts.ready; } catch (e) {}
        await waitForMermaid();
        window.__export_ready_done = true;
      })();
    })();
  </script>
</body>
</html>
"""
)


def render_html(markdown_text: str, base_href: str) -> str:
    md = build_markdown_renderer()
    body_html = md.render(markdown_text)
    html = HTML_TEMPLATE.render(
        title="Practical AI in Biology - Book", body=body_html, base_href=base_href
    )
    return html


def export_pdf_from_html(html: str, output_pdf: Path, base_dir: Path) -> None:
    # Write HTML to disk and navigate to file:// URL so local images load reliably
    html_path = base_dir / "book_export.html"
    html_path.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--allow-file-access-from-files"])
        context = browser.new_context()
        page = context.new_page()
        page.goto(html_path.as_uri(), wait_until="domcontentloaded")

        # Wait for fonts & mermaid to finish
        page.wait_for_function(
            "() => window.__export_ready_done === true", timeout=60_000
        )

        # Ensure images are loaded
        page.wait_for_load_state("networkidle")

        # Generate PDF
        page.pdf(
            path=str(output_pdf),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "12mm", "right": "12mm", "bottom": "12mm", "left": "12mm"},
        )
        context.close()
        browser.close()


def main() -> None:
    if not INPUT_MD.exists():
        raise FileNotFoundError(f"Input markdown not found: {INPUT_MD}")
    markdown_text = INPUT_MD.read_text(encoding="utf-8")
    # Use file:// base href so relative images like assets/... load correctly
    base_href = PROJECT_ROOT.as_uri() + "/"
    html = render_html(markdown_text, base_href)
    export_pdf_from_html(html, OUTPUT_PDF, PROJECT_ROOT)
    print(f"PDF written to: {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
