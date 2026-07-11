#!/usr/bin/env python3
"""Render only the summary portion of the latest daily report for GitHub Pages."""

from __future__ import annotations

import argparse
import html
import os
import re
from datetime import datetime, timezone
from pathlib import Path


def _render_inline(text: str) -> str:
    escaped = html.escape(text, quote=False)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", escaped)


def _markdown_summary_to_html(summary: str) -> str:
    rendered: list[str] = []
    for line in summary.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("### "):
            rendered.append(f"<h3>{_render_inline(stripped[4:])}</h3>")
        elif stripped.startswith("## "):
            rendered.append(f"<h2>{_render_inline(stripped[3:])}</h2>")
        elif stripped.startswith("# "):
            rendered.append(f"<h1>{_render_inline(stripped[2:])}</h1>")
        elif stripped.startswith("> "):
            rendered.append(f"<p class=\"market-status\">{_render_inline(stripped[2:])}</p>")
        else:
            rendered.append(f"<p>{_render_inline(stripped)}</p>")
    return "\n".join(rendered)


def _public_summary(report: str) -> str | None:
    lines = report.splitlines()
    for index, line in enumerate(lines):
        if index and line.strip() == "---":
            return "\n".join(lines[:index]).strip()
    return None


def _write_output(name: str, value: str) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if output_path:
        with Path(output_path).open("a", encoding="utf-8") as output:
            output.write(f"{name}={value}\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report-dir", type=Path, default=Path("reports"))
    parser.add_argument("--output-dir", type=Path, default=Path("public-report"))
    args = parser.parse_args()

    reports = sorted(args.report_dir.glob("report_*.md"), key=lambda path: path.stat().st_mtime)
    if not reports:
        print("No daily report found; public page deployment skipped.")
        _write_output("has_report", "false")
        return 0

    summary = _public_summary(reports[-1].read_text(encoding="utf-8"))
    if not summary:
        print("Daily report has no summary separator; public page deployment skipped.")
        _write_output("has_report", "false")
        return 0

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    page = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>NVDA Daily Stock Analysis</title>
  <style>
    body {{ background: #f6f8fa; color: #1f2328; font: 16px/1.6 system-ui, sans-serif; margin: 0; }}
    main {{ background: #fff; border: 1px solid #d0d7de; border-radius: 12px; margin: 40px auto; max-width: 760px; padding: 32px; }}
    h1 {{ font-size: 1.75rem; }} h2 {{ margin-top: 2rem; }}
    .market-status {{ background: #ddf4ff; border-radius: 6px; padding: 12px; }}
    footer {{ border-top: 1px solid #d0d7de; color: #57606a; font-size: .875rem; margin-top: 2rem; padding-top: 1rem; }}
  </style>
</head>
<body>
  <main>
    {_markdown_summary_to_html(summary)}
    <footer>
      <p>Updated {generated_at}. This page is an automated summary for informational purposes only, not investment advice.</p>
      <p>Only the report summary is published. Detailed reports, workflow logs, email addresses, and credentials are not included.</p>
    </footer>
  </main>
</body>
</html>
"""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "index.html").write_text(page, encoding="utf-8")
    _write_output("has_report", "true")
    print(f"Rendered public summary from {reports[-1]}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
