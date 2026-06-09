#!/usr/bin/env python3
"""
Example: Portfolio Risk and Construction Analysis

Shows how the Quantitative Trading Agent can be used for higher-level
portfolio construction and risk discussions.
"""

from quantitive_trading_agent.agent import create_quantitative_trading_agent

def analyze_portfolio_construction():
    agent = create_quantitative_trading_agent(reasoning_effort="high")

    task = (
        "Compare three different approaches to building a semiconductor-heavy portfolio: "
        "1) A concentrated single-ETF approach (e.g. SMH), "
        "2) A diversified basket of individual semiconductor stocks, "
        "3) A multi-factor smart-beta semiconductor ETF. "
        "Discuss risk factors, concentration risk, liquidity, cost, and rebalancing considerations for each. "
        "Provide a balanced comparison table and highlight scenarios where each approach might be preferable."
    )

    print("Running Portfolio Construction Analysis...\n")
    result = agent.run(task=task)
    print(result)
    return result


if __name__ == "__main__":
    analyze_portfolio_construction()
