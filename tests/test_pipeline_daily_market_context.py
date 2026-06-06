# -*- coding: utf-8 -*-
"""Pipeline tests for Issue #1381 daily market context injection."""

from __future__ import annotations

from datetime import date
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from src.analyzer import GeminiAnalyzer
from src.core.pipeline import StockAnalysisPipeline
from src.services.daily_market_context import DailyMarketContext


def _market_context() -> DailyMarketContext:
    return DailyMarketContext(
        region="cn",
        trade_date=date(2026, 6, 6),
        summary="大盘退潮，高风险，建议观望，仓位上限30%。",
        risk_tags=["high_risk", "low_position_cap"],
        source="analysis_history",
    )


def test_pipeline_loads_daily_market_context_when_market_review_enabled() -> None:
    pipeline = StockAnalysisPipeline.__new__(StockAnalysisPipeline)
    pipeline.config = SimpleNamespace(market_review_enabled=True, report_language="zh")
    pipeline.db = MagicMock()
    pipeline.notifier = MagicMock()
    pipeline.analyzer = MagicMock()
    pipeline.search_service = MagicMock()

    with patch("src.core.pipeline.DailyMarketContextService") as service_cls:
        service = service_cls.return_value
        service.get_context.return_value = _market_context()

        context = pipeline._load_daily_market_context("cn")

    assert context is not None
    service_cls.assert_called_once_with(db_manager=pipeline.db)
    service.get_context.assert_called_once_with(
        region="cn",
        config=pipeline.config,
        notifier=pipeline.notifier,
        analyzer=pipeline.analyzer,
        search_service=pipeline.search_service,
        force_refresh=False,
        allow_generate=True,
    )


def test_pipeline_attaches_low_sensitive_market_context_to_enhanced_context() -> None:
    pipeline = StockAnalysisPipeline.__new__(StockAnalysisPipeline)
    enhanced_context = {"code": "600519"}

    pipeline._attach_daily_market_context(
        enhanced_context,
        _market_context(),
        report_language="zh",
    )

    assert enhanced_context["daily_market_context"]["region"] == "cn"
    assert enhanced_context["daily_market_context"]["summary"].startswith("大盘退潮")
    assert "大盘环境摘要" in enhanced_context["daily_market_context_summary"]
    assert "market_review_payload" not in str(enhanced_context)


def test_analyzer_prompt_renders_daily_market_context_before_technical_data() -> None:
    analyzer = GeminiAnalyzer.__new__(GeminiAnalyzer)
    analyzer._get_skill_prompt_sections = lambda: ("", "", False)
    context = {
        "code": "600519",
        "stock_name": "贵州茅台",
        "date": "2026-06-06",
        "today": {"close": 1800, "open": 1790, "high": 1810, "low": 1780},
        "daily_market_context": _market_context().to_safe_dict(),
    }

    prompt = analyzer._format_prompt(context, "贵州茅台", report_language="zh")

    assert "大盘环境摘要" in prompt
    assert "大盘退潮" in prompt
    assert prompt.index("大盘环境摘要") < prompt.index("技术面数据")
