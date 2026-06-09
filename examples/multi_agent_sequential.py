#!/usr/bin/env python3
"""
Multi-Agent Sequential Workflow Example

Uses multiple Claude Fable 5 agents in a SequentialWorkflow:
Researcher → Analyst → Writer

This is one of the recommended patterns from the official docs:
https://docs.swarms.world/examples/model-providers/claude-fable-5#multi-agent-systems-with-fable-5

Perfect for producing high-quality, well-structured trading research reports.
"""

from swarms import Agent, SequentialWorkflow
from quantitive_trading_agent.agent import create_quantitative_trading_agent

def run_sequential_etf_report():
    """
    Build a high-quality ETF comparison report using a research pipeline.
    All agents use Fable 5 with appropriate thinking budgets.
    """
    researcher = create_quantitative_trading_agent(
        agent_name="ETF-Researcher",
        system_prompt="You are a meticulous ETF researcher. Gather comprehensive data, metrics, holdings, and recent news on the requested ETFs. Cite sources where possible.",
        thinking_tokens=2048,
        reasoning_effort="high",
        max_loops=1,
    )

    analyst = create_quantitative_trading_agent(
        agent_name="ETF-Analyst",
        system_prompt="You are a sharp quantitative analyst. Identify key insights, risks, opportunities, and comparative advantages from the research provided.",
        thinking_tokens=2048,
        reasoning_effort="high",
        max_loops=1,
    )

    writer = create_quantitative_trading_agent(
        agent_name="Report-Writer",
        system_prompt="You are an expert financial writer. Synthesize the research and analysis into a clear, professional, well-structured report with tables and executive summary.",
        thinking_tokens=1024,
        reasoning_effort="high",
        max_loops=1,
    )

    pipeline = SequentialWorkflow(
        agents=[researcher, analyst, writer],
        max_loops=1,
    )

    task = (
        "Produce a professional comparative report on the top semiconductor ETFs: "
        "SMH, SOXX, and XSD. Cover performance, expense ratios, AUM, top holdings, "
        "liquidity, strategies, and risks."
    )

    print("🚀 Running Sequential Multi-Agent Workflow (Fable 5 Research Pipeline)\n")
    result = pipeline.run(task)
    print(result)
    return result


if __name__ == "__main__":
    run_sequential_etf_report()
