#!/usr/bin/env python3
"""
Quantitative Trading Agent - Main Entry Point

Example usage of the Quantitative-Trading-Agent built with swarms.
"""

from quantitive_trading_agent.agent import create_quantitative_trading_agent

def main():
    print("Initializing Quantitative-Trading-Agent (Claude Fable 5)...\n")

    agent = create_quantitative_trading_agent(
        agent_name="Quantitative-Trading-Agent",
        max_loops=1,
        thinking_tokens=1024,
        reasoning_effort="high",
    )

    task = (
        "Analyze the best semiconductor ETFs and provide a detailed comparison. "
        "Include metrics such as performance, expense ratio, holdings, and any notable strategies."
    )

    print(f"Running task:\n{task}\n")
    print("=" * 80)

    out = agent.run(task=task)

    print(out)
    print("=" * 80)
    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
