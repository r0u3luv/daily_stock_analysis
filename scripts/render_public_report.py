#!/usr/bin/env python3
"""Render the latest daily report for GitHub Pages."""

from __future__ import annotations

import argparse
import os
from datetime import datetime, timezone
from pathlib import Path

import markdown2


def _markdown_to_html(report: str) -> str:
    """Render report Markdown while treating generated text as untrusted HTML."""
    return markdown2.markdown(
        report,
        extras=["tables", "fenced-code-blocks", "break-on-newline", "cuddled-lists"],
        safe_mode="escape",
    )


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

    report = reports[-1].read_text(encoding="utf-8").strip()
    if not report:
        print("Latest daily report is empty; public page deployment skipped.")
        _write_output("has_report", "false")
        return 0

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    page = f"""<!doctype html>
<html lang=\"ja\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>NVDA Daily Stock Analysis</title>
  <style>
    body {{ background: #f6f8fa; color: #1f2328; font: 16px/1.6 system-ui, sans-serif; margin: 0; }}
    main {{ background: #fff; border: 1px solid #d0d7de; border-radius: 12px; margin: 40px auto; max-width: 900px; padding: 32px; }}
    h1 {{ color: #0969da; font-size: 1.75rem; }} h2 {{ border-bottom: 1px solid #d0d7de; margin-top: 2rem; padding-bottom: .3em; }}
    h3 {{ margin-top: 1.5rem; }} p {{ margin: 0 0 .75rem; }}
    table {{ border-collapse: collapse; display: block; font-size: .875rem; margin: 12px 0; overflow-x: auto; width: 100%; }}
    th, td {{ border: 1px solid #d0d7de; padding: 6px 10px; text-align: left; }} th {{ background: #f6f8fa; }}
    blockquote {{ border-left: .25em solid #d0d7de; color: #57606a; margin: 0 0 12px; padding: 0 1em; }}
    pre {{ background: #f6f8fa; border-radius: 6px; overflow: auto; padding: 12px; }}
    code {{ background: rgba(175,184,193,.2); border-radius: 3px; padding: .2em .4em; }}
    footer {{ border-top: 1px solid #d0d7de; color: #57606a; font-size: .875rem; margin-top: 2rem; padding-top: 1rem; }}
  </style>
</head>
<body>
  <main>
    {_markdown_to_html(report)}
    <footer>
      <p>更新: {generated_at}。このページは自動生成された参考情報であり、投資助言ではありません。</p>
      <p>公開対象は最新の詳細レポートです。実行ログ、メールアドレス、認証情報は含みません。</p>
    </footer>
  </main>
</body>
</html>
"""
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "index.html").write_text(page, encoding="utf-8")
    _write_output("has_report", "true")
    print(f"Rendered public report from {reports[-1]}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
