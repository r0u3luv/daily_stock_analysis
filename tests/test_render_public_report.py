"""Tests for the GitHub Pages report renderer."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = ROOT / "scripts" / "render_public_report.py"
SPEC = importlib.util.spec_from_file_location("render_public_report", SCRIPT_PATH)
assert SPEC and SPEC.loader
render_public_report = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(render_public_report)


def test_markdown_to_html_keeps_report_details_after_summary_separator():
    report = """# Daily report

## Summary

---

## Detailed decision

| Entry | Stop loss |
| --- | --- |
| 100 | 90 |

- Watch earnings
"""

    rendered = render_public_report._markdown_to_html(report)

    assert "Detailed decision" in rendered
    assert "<table>" in rendered
    assert "<li>Watch earnings</li>" in rendered


def test_markdown_to_html_escapes_raw_html():
    rendered = render_public_report._markdown_to_html("<script>alert('xss')</script>")

    assert "<script>" not in rendered
    assert "&lt;script&gt;" in rendered


def test_main_skips_empty_latest_report(tmp_path, monkeypatch):
    report_dir = tmp_path / "reports"
    output_dir = tmp_path / "public-report"
    report_dir.mkdir()
    (report_dir / "report_2026-07-13.md").write_text(" \n", encoding="utf-8")
    output_file = tmp_path / "github-output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output_file))
    monkeypatch.setattr(
        "sys.argv",
        ["render_public_report.py", "--report-dir", str(report_dir), "--output-dir", str(output_dir)],
    )

    assert render_public_report.main() == 0
    assert not (output_dir / "index.html").exists()
    assert output_file.read_text(encoding="utf-8") == "has_report=false\n"


def test_main_writes_full_latest_report(tmp_path, monkeypatch):
    report_dir = tmp_path / "reports"
    output_dir = tmp_path / "public-report"
    report_dir.mkdir()
    (report_dir / "report_2026-07-13.md").write_text(
        "# Summary\n\n---\n\n## Detailed decision\n\n- Keep watching\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        "sys.argv",
        ["render_public_report.py", "--report-dir", str(report_dir), "--output-dir", str(output_dir)],
    )

    assert render_public_report.main() == 0
    page = (output_dir / "index.html").read_text(encoding="utf-8")
    assert "Detailed decision" in page
    assert "Keep watching" in page
