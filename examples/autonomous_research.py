#!/usr/bin/env python3
"""
Autonomous Long-Running Research Example

Demonstrates using max_loops="auto" with persistent memory.
Fable 5 is particularly strong at long-horizon autonomous tasks.

From the docs: Fable 5 excels when the task is longer and more complex.
"""

from quantitive_trading_agent.agent import create_quantitative_trading_agent

def run_autonomous_market_research():
    agent = create_quantitative_trading_agent(
        agent_name="Autonomous-Researcher",
        max_loops="auto",           # Let the agent plan and iterate until done
        thinking_tokens=8192,
        reasoning_effort="high",
        persistent_memory=True,     # Important for long sessions
        context_compression=True,
        context_length=200_000,
        autosave=True,
    )

    task = (
        "Research the current state of the AI semiconductor supply chain in 2026. "
        "Identify the top 5 critical bottlenecks, key companies involved at each stage, "
        "recent geopolitical developments affecting supply, and investment implications. "
        "Write a comprehensive report and save key findings to a structured markdown file called ai_semiconductor_supply_chain_2026.md. "
        "Continue iterating until you have high-quality, well-cited information."
    )

    print("🚀 Starting Autonomous Research Agent (Fable 5 with max_loops='auto')\n")
    print("This may take several minutes as the agent plans, researches, and refines...\n")

    result = agent.run(task)
    print("\n" + "=" * 80)
    print("AUTONOMOUS RESEARCH COMPLETE")
    print("=" * 80)
    print(result)
    return result


if __name__ == "__main__":
    run_autonomous_market_research()
