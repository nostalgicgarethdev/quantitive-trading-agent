#!/usr/bin/env python3
"""
Streaming Analysis Example

Shows how to stream tokens in real-time from a Fable 5 agent.
Useful for building dashboards, UIs, or live research tools.
"""

from quantitive_trading_agent.agent import create_quantitative_trading_agent

def on_token(token: str) -> None:
    """Simple callback to print tokens as they arrive."""
    print(token, end="", flush=True)


def run_streaming_etf_analysis():
    agent = create_quantitative_trading_agent(
        agent_name="Streaming-Analyst",
        streaming_on=True,
        thinking_tokens=2048,
        reasoning_effort="high",
    )

    # Alternative: use streaming_callback for more control
    # agent = create_quantitative_trading_agent(
    #     streaming_callback=on_token,
    #     ...
    # )

    task = (
        "Provide a detailed comparison of SMH vs SOXX. Include recent performance, "
        "holdings overlap, expense ratios, and which might be more suitable for different investor types."
    )

    print("🚀 Streaming Fable 5 Analysis (tokens will appear live)\n")
    print("-" * 60 + "\n")

    result = agent.run(task)

    print("\n" + "-" * 60)
    print("\n[Streaming complete]")
    return result


if __name__ == "__main__":
    run_streaming_etf_analysis()
