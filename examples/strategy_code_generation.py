#!/usr/bin/env python3
"""
Strategy Code Generation Example

Fable 5 is excellent at writing high-quality quantitative code.
This example asks it to generate a complete backtesting script.
"""

from quantitive_trading_agent.agent import create_quantitative_trading_agent

def generate_trading_strategy_code():
    agent = create_quantitative_trading_agent(
        agent_name="Strategy-Developer",
        thinking_tokens=4096,
        reasoning_effort="high",
    )

    task = (
        "Design a simple mean-reversion trading strategy for a semiconductor ETF (e.g. SMH). "
        "Write a complete, self-contained Python script using pandas and yfinance that:\n"
        "1. Downloads historical data\n"
        "2. Calculates the strategy signals (e.g. using z-score of returns or RSI)\n"
        "3. Implements position sizing and basic risk management\n"
        "4. Runs a vectorized backtest and prints performance metrics (CAGR, Sharpe, max drawdown)\n"
        "5. Includes clear comments explaining the logic\n\n"
        "Use only common libraries. Make the code production-ready and easy to modify."
    )

    print("🚀 Generating Trading Strategy Code with Fable 5\n")
    code = agent.run(task)
    print(code)

    # Optional: save to file
    with open("generated_mean_reversion_strategy.py", "w") as f:
        f.write(code)
    print("\n[Code also saved to generated_mean_reversion_strategy.py]")

    return code


if __name__ == "__main__":
    generate_trading_strategy_code()
