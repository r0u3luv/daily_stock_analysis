# -*- coding: utf-8 -*-
"""Decision guardrail using daily market context for Issue #1381."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, List

from src.report_language import normalize_report_language


_CONSERVATIVE_TAGS = {"high_risk", "market_cooling", "conservative", "low_position_cap"}
_CONSERVATIVE_TEXT_MARKERS_ZH = ("退潮", "观望", "高风险", "谨慎", "保守", "仓位上限", "轻仓")
_CONSERVATIVE_TEXT_MARKERS_EN = ("high risk", "risk-off", "risk off", "watch", "cautious", "conservative", "position cap")
_AGGRESSIVE_BUY_MARKERS_ZH = ("立即买入", "马上买入", "积极买入", "激进买入", "追高", "加仓")
_AGGRESSIVE_BUY_MARKERS_EN = ("buy now", "strong buy", "aggressive buy", "chase", "add aggressively")


def apply_daily_market_context_guardrail(
    result: Any,
    *,
    daily_market_context: Any,
    report_language: str = "zh",
) -> List[str]:
    """Soften aggressive buy advice when daily market context is conservative."""

    if result is None or not _is_conservative_context(daily_market_context):
        return []

    language = normalize_report_language(report_language or getattr(result, "report_language", "zh"))
    if not _has_aggressive_buy_signal(result, language=language):
        return []

    adjustments: List[str] = []
    if str(getattr(result, "decision_type", "") or "").lower() == "buy":
        result.decision_type = "hold"
        adjustments.append("daily_market_context_buy_softened")
    elif _contains_any(str(getattr(result, "operation_advice", "") or ""), _buy_markers(language)):
        adjustments.append("daily_market_context_buy_softened")

    softened_advice = (
        "Market context is conservative; avoid aggressive buying, keep position small, and wait for confirmation."
        if language == "en"
        else "大盘环境偏谨慎，暂不追高；仅保留小仓试探或等待确认。"
    )
    result.operation_advice = softened_advice

    if _is_high_confidence(getattr(result, "confidence_level", "")):
        result.confidence_level = "Medium" if language == "en" else "中"
        adjustments.append("confidence_capped_daily_market_context")

    dashboard = getattr(result, "dashboard", None)
    if not isinstance(dashboard, dict):
        dashboard = {}
        result.dashboard = dashboard

    core = dashboard.get("core_conclusion")
    if isinstance(core, dict):
        core["one_sentence"] = softened_advice

    phase_decision = dashboard.get("phase_decision")
    if not isinstance(phase_decision, dict):
        phase_decision = {}
        dashboard["phase_decision"] = phase_decision
    limitations = phase_decision.get("data_limitations")
    if not isinstance(limitations, list):
        limitations = []
    limitation = (
        "Daily market context is conservative/high risk; aggressive buy advice was softened."
        if language == "en"
        else "大盘环境偏谨慎/高风险，已软化激进买入建议。"
    )
    if limitation not in limitations:
        limitations.append(limitation)
    phase_decision["data_limitations"] = limitations
    reason = str(phase_decision.get("confidence_reason") or "").strip()
    reason_note = (
        "Market context requires conservative sizing."
        if language == "en"
        else "大盘环境要求降低进攻性并控制仓位。"
    )
    phase_decision["confidence_reason"] = (
        f"{reason}；{reason_note}" if reason and language != "en" else
        f"{reason}; {reason_note}" if reason else reason_note
    )

    return adjustments


def _is_conservative_context(context: Any) -> bool:
    if not isinstance(context, Mapping):
        return False
    tags = context.get("risk_tags")
    if isinstance(tags, list) and any(str(tag) in _CONSERVATIVE_TAGS for tag in tags):
        return True
    summary = str(context.get("summary") or "")
    lowered = summary.lower()
    return any(marker in summary for marker in _CONSERVATIVE_TEXT_MARKERS_ZH) or any(
        marker in lowered for marker in _CONSERVATIVE_TEXT_MARKERS_EN
    )


def _has_aggressive_buy_signal(result: Any, *, language: str) -> bool:
    decision_type = str(getattr(result, "decision_type", "") or "").lower()
    if decision_type == "buy":
        return True
    advice = str(getattr(result, "operation_advice", "") or "")
    return _contains_any(advice, _buy_markers(language))


def _buy_markers(language: str) -> tuple[str, ...]:
    return _AGGRESSIVE_BUY_MARKERS_EN if language == "en" else _AGGRESSIVE_BUY_MARKERS_ZH


def _contains_any(text: str, markers: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(marker.lower() in lowered for marker in markers)


def _is_high_confidence(value: Any) -> bool:
    return str(value or "").strip().lower() in {"高", "high"}
