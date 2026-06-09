#!/usr/bin/env python3
"""
Example: Semiconductor ETF Comparison

Demonstrates the Quantitative Trading Agent performing a detailed
comparative analysis of semiconductor ETFs.
"""

from quantitive_trading_agent.agent import create_quantitative_trading_agent

def run_semiconductor_etf_analysis():
    """Run a focused semiconductor ETF comparison."""
    agent = create_quantitative_trading_agent(
        reasoning_effort="high",
        thinking_tokens=2048,  # Give it more thinking budget for complex comparison
    )

    task = (
        "Analyze the best semiconductor ETFs and provide a detailed comparison. "
        "Include metrics such as performance (YTD, 1-year, 5-year), expense ratio, "
        "AUM, top holdings, sector allocation, liquidity (average daily volume), "
        "tracking error, and any notable investment strategies or index methodologies. "
        "Cover at least SMH, SOXX, XSD, SMH, and one other relevant ETF. "
        "Organize your response with clear sections and tables."
    )

    print("🚀 Running Semiconductor ETF Analysis with Quantitative-Trading-Agent\n")
    result = agent.run(task=task)
    print(result)
    return result


if __name__ == "__main__":
    run_semiconductor_etf_analysis()
