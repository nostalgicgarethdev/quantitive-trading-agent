#!/usr/bin/env python3
"""
Hierarchical Swarm Example

Fable 5 acts as the "Director" that breaks down complex tasks and delegates
to faster/cheaper worker agents.

Excellent pattern when you want Fable 5's superior reasoning at the top level
while controlling costs.

From the docs:
https://docs.swarms.world/examples/model-providers/claude-fable-5#hierarchical-swarm
"""

from swarms import Agent, HierarchicalSwarm
from quantitive_trading_agent.agent import create_quantitative_trading_agent

def run_hierarchical_competitive_analysis():
    # Fable 5 as the intelligent director
    director = create_quantitative_trading_agent(
        agent_name="Fable-5-Director",
        system_prompt=(
            "You are the Director of a quantitative research team. "
            "Break complex questions into clear subtasks, delegate them to your analysts, "
            "review their work, and synthesize a final high-quality deliverable."
        ),
        thinking_tokens=4096,
        reasoning_effort="high",
        max_loops=1,
    )

    # Worker analysts (using faster models)
    workers = [
        Agent(
            agent_name=f"Analyst-{i}",
            model_name="claude-haiku-4-5",  # Fast and cheap for execution
            max_loops=2,
            system_prompt="You are a diligent quantitative analyst. Execute the task given to you thoroughly and return clear findings.",
        )
        for i in range(1, 5)
    ]

    swarm = HierarchicalSwarm(
        director=director,
        agents=workers,
        max_loops=2,
    )

    task = (
        "Produce a competitive analysis of the AI inference chip market. "
        "Cover key players, technology trends, market size projections, and investment implications."
    )

    print("🚀 Running Hierarchical Swarm (Fable 5 Director + Worker Analysts)\n")
    result = swarm.run(task)
    print(result)
    return result


if __name__ == "__main__":
    run_hierarchical_competitive_analysis()
