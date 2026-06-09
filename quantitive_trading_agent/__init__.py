"""
Quantitative Trading Agent

Advanced AI agent for quantitative finance and trading analysis
powered by swarms + Claude Fable 5.
"""

from .agent import create_quantitative_trading_agent, QUANTITATIVE_TRADING_SYSTEM_PROMPT

__version__ = "0.1.0"
__all__ = ["create_quantitative_trading_agent", "QUANTITATIVE_TRADING_SYSTEM_PROMPT"]
