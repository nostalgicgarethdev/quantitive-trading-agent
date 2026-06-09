"""
quantitive-trading-agent

Advanced quantitative finance agents powered by swarms + Claude Fable 5.

Official docs reference:
https://docs.swarms.world/examples/model-providers/claude-fable-5
"""

from .agent import (
    create_quantitative_trading_agent,
    quantitative_trading_agent,
    QUANTITATIVE_TRADING_SYSTEM_PROMPT,
)
from .prompts import (
    QUANTITATIVE_TRADING_AGENT,
    ETF_RESEARCHER,
    QUANTITATIVE_ANALYST,
    REPORT_WRITER,
    TECHNICAL_ANALYST,
    MACRO_ECONOMIST,
    RISK_MANAGER,
    STRATEGY_CODER,
    get_prompt,
)

__version__ = "0.2.0"
__all__ = [
    "create_quantitative_trading_agent",
    "quantitative_trading_agent",
    "QUANTITATIVE_TRADING_SYSTEM_PROMPT",
    "QUANTITATIVE_TRADING_AGENT",
    "ETF_RESEARCHER",
    "QUANTITATIVE_ANALYST",
    "REPORT_WRITER",
    "TECHNICAL_ANALYST",
    "MACRO_ECONOMIST",
    "RISK_MANAGER",
    "STRATEGY_CODER",
    "get_prompt",
]
