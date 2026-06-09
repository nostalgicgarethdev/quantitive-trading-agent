#!/usr/bin/env python3
"""
Mixture of Agents (MoA) Example

Uses cheaper/faster worker models to generate diverse ideas in parallel,
then has a powerful Fable 5 agent synthesize the best answer.

This is a cost-effective, high-quality pattern recommended in the docs:
https://docs.swarms.world/examples/model-providers/claude-fable-5#mixture-of-agents

Fable 5 shines here as the aggregator.
"""

from swarms import Agent, MixtureOfAgents
from quantitive_trading_agent.agent import create_quantitative_trading_agent

def run_mixture_of_agents_analysis():
    # Worker agents (cheaper models for idea generation)
    workers = [
        Agent(
            agent_name="Worker-Haiku",
            model_name="claude-haiku-4-5",
            max_loops=1,
            system_prompt="You are a concise, insightful analyst. Generate 3-5 key points on the topic.",
        ),
        Agent(
            agent_name="Worker-Sonnet",
            model_name="claude-sonnet-4-6",
            max_loops=1,
            system_prompt="You are a detailed analyst. Provide structured analysis with pros/cons and data points.",
        ),
        Agent(
            agent_name="Worker-GPT",
            model_name="gpt-4.1",
            max_loops=1,
            system_prompt="You are a creative strategist. Suggest unconventional angles and scenarios.",
        ),
    ]

    # Fable 5 as the powerful aggregator / synthesizer
    aggregator = create_quantitative_trading_agent(
        agent_name="Fable-5-Aggregator",
        system_prompt=(
            "You are an expert synthesizer. Take the diverse worker responses and produce "
            "one coherent, high-quality, data-driven analysis. Resolve contradictions, "
            "highlight the strongest points, and structure the final output professionally."
        ),
        thinking_tokens=4096,
        reasoning_effort="high",
        max_loops=1,
    )

    moa = MixtureOfAgents(
        agents=workers,
        aggregator_agent=aggregator,
        layers=2,  # Two rounds of refinement
    )

    task = (
        "What are the key risks and opportunities for investors in the AI semiconductor sector over the next 12 months?"
    )

    print("🚀 Running Mixture of Agents (Workers + Fable 5 Aggregator)\n")
    result = moa.run(task)
    print(result)
    return result


if __name__ == "__main__":
    run_mixture_of_agents_analysis()
