#!/usr/bin/env python3
"""
Vision + Chart Analysis Example

Fable 5 has strong vision capabilities. This example shows how to
pass a chart image for analysis (technical or fundamental charts).

Note: You need to provide a real image path or URL.
"""

from quantitive_trading_agent.agent import create_quantitative_trading_agent

def analyze_chart(image_path: str = None):
    """
    Analyze a financial chart using Fable 5's vision.
    
    Args:
        image_path: Path to a chart image (PNG/JPG) or URL.
    """
    agent = create_quantitative_trading_agent(
        agent_name="Chart-Analyst",
        max_loops=1,
        thinking_tokens=2048,
        reasoning_effort="high",
    )

    if image_path is None:
        print("No image provided. Using example task with placeholder.")
        task = (
            "Imagine you are looking at a 1-year price chart of SMH with volume. "
            "Describe what a typical bullish breakout pattern would look like and "
            "what risk management rules a quantitative trader should apply."
        )
        result = agent.run(task)
    else:
        task = "Analyze this financial chart in detail. Identify trends, key levels, volume patterns, and any notable formations. Suggest what this might mean for a quantitative trader."
        result = agent.run(task=task, img=image_path)

    print("🚀 Fable 5 Chart / Vision Analysis\n")
    print(result)
    return result


if __name__ == "__main__":
    # Replace with your own chart image
    # analyze_chart("path/to/your/semiconductor_etf_chart.png")
    analyze_chart()  # Runs text-only example
