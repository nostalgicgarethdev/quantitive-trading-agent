#!/usr/bin/env python3
"""
Tool-Calling Pattern with Fable 5 (Recommended when you need real data)

Fable 5 **does not support tools/function calling**.

The official recommended pattern (from the docs) is:
1. Use a tool-capable model (e.g. claude-sonnet-4-6) to gather fresh data.
2. Pass the results to a Fable 5 agent for deep reasoning and synthesis.

This example uses yfinance to fetch real market data.
"""

from swarms import Agent, SequentialWorkflow
import yfinance as yf
from quantitive_trading_agent.agent import create_quantitative_trading_agent

def get_stock_data(ticker: str) -> str:
    """Fetch key financial metrics for a ticker using yfinance."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = stock.fast_info.get("last_price", "N/A")
        return (
            f"{ticker} - Price: ${price}, "
            f"Market Cap: {info.get('marketCap', 'N/A')}, "
            f"PE Ratio: {info.get('trailingPE', 'N/A')}, "
            f"52-Week High/Low: {info.get('fiftyTwoWeekHigh', 'N/A')}/{info.get('fiftyTwoWeekLow', 'N/A')}"
        )
    except Exception as e:
        return f"Error fetching data for {ticker}: {e}"


def run_tool_augmented_analysis():
    # Step 1: Tool-using agent (Sonnet) gathers fresh data
    data_collector = Agent(
        agent_name="Data-Collector",
        model_name="claude-sonnet-4-6",  # Sonnet supports tools well
        tools=[get_stock_data],
        max_loops=3,
        system_prompt="You are a data collection specialist. Use the available tools to gather accurate, up-to-date market data for the requested tickers.",
    )

    # Step 2: Fable 5 performs deep analysis on the collected data
    fable_analyst = create_quantitative_trading_agent(
        agent_name="Fable-5-Deep-Analyst",
        system_prompt=(
            "You are a senior quantitative strategist. You receive raw data from the Data-Collector. "
            "Perform deep, insightful analysis, identify implications, risks, and opportunities. "
            "Structure your response professionally with clear reasoning."
        ),
        thinking_tokens=4096,
        reasoning_effort="high",
        max_loops=1,
    )

    pipeline = SequentialWorkflow(agents=[data_collector, fable_analyst], max_loops=1)

    task = (
        "Fetch current data for NVDA, AMD, and TSM, then provide a deep comparative analysis "
        "of their valuations, momentum, and risks for a quantitative investor."
    )

    print("🚀 Running Tool + Fable 5 Pattern (Data Collector → Fable 5 Analyst)\n")
    result = pipeline.run(task)
    print(result)
    return result


if __name__ == "__main__":
    run_tool_augmented_analysis()
