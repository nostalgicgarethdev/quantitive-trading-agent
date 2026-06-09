#!/usr/bin/env python3
"""
Multi-Agent Concurrent Workflow Example

Runs multiple specialized Fable 5 agents in parallel on the same question.
Each agent acts as a domain expert.

From the official docs:
https://docs.swarms.world/examples/model-providers/claude-fable-5#concurrent-workflow
"""

from swarms import Agent, ConcurrentWorkflow
from quantitive_trading_agent.agent import create_quantitative_trading_agent

def run_concurrent_market_analysis():
    topics = ["Technical Analysis", "Fundamental Analysis", "Macro & Geopolitics", "Risk & Valuation"]

    agents = [
        create_quantitative_trading_agent(
            agent_name=f"{topic.replace(' ', '-')}-Expert",
            system_prompt=f"You are a world-class expert in {topic.lower()}. Provide deep, specific insights on the given topic.",
            thinking_tokens=1536,
            reasoning_effort="high",
            max_loops=1,
        )
        for topic in topics
    ]

    workflow = ConcurrentWorkflow(agents=agents)

    task = (
        "Analyze the current state and outlook for the semiconductor industry and "
        "major chip stocks (NVDA, AMD, TSM, AVGO). Provide expert perspective from your domain."
    )

    print("🚀 Running Concurrent Multi-Agent Analysis (Parallel Fable 5 Experts)\n")
    results = workflow.run(task)

    for name, response in results.items():
        print(f"\n{'='*60}")
        print(f"=== {name} ===")
        print(f"{'='*60}\n")
        print(response)

    return results


if __name__ == "__main__":
    run_concurrent_market_analysis()
