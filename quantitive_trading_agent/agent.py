"""
Quantitative Trading Agent Module

Reusable factory for creating a high-performance quantitative finance agent
using the swarms framework and Anthropic's Claude Fable 5.
"""

from swarms import Agent

QUANTITATIVE_TRADING_SYSTEM_PROMPT = (
    "You are Quantitative-Trading-Agent, an advanced AI assistant specializing in quantitative finance, "
    "trading, and algorithmic analysis. You have deep expertise in analyzing financial instruments, "
    "with a focus on exchange-traded funds (ETFs), equities, derivatives, and portfolio construction. "
    "You always provide thorough, data-driven, and well-cited analysis suitable for both institutional "
    "and individual investors, incorporating recent performance metrics, expense ratios, portfolio holdings, "
    "liquidity considerations, risk factors, and competitive landscape insights. When responding, organize "
    "information clearly, use tables or bullet points where appropriate, and explain your reasoning process "
    "explicitly. Proactively mention relevant industry trends and regulatory context as needed. Avoid making "
    "financial recommendations, but focus on providing comparative research to empower decision-making. Use "
    "plain language to explain technical topics, and cite reputable public sources when possible. Your "
    "responses should reflect professionalism, accuracy, and a collaborative, respectful tone."
)


def create_quantitative_trading_agent(
    agent_name: str = "Quantitative-Trading-Agent",
    max_loops: int = 1,
    thinking_tokens: int = 1024,
    reasoning_effort: str = "high",
    temperature: float = None,
    tools_list_dictionary: list = None,
    **kwargs
) -> Agent:
    """
    Factory function to create a specialized Quantitative Trading Agent.

    Args:
        agent_name: Name of the agent
        max_loops: Maximum reasoning loops
        thinking_tokens: Tokens allocated for internal reasoning (Claude)
        reasoning_effort: "low", "medium", or "high"
        temperature: Sampling temperature (None = model default)
        tools_list_dictionary: Optional list of tools to equip the agent with
        **kwargs: Additional arguments passed to swarms.Agent

    Returns:
        Configured swarms.Agent instance ready for quantitative finance tasks.
    """
    return Agent(
        agent_name=agent_name,
        agent_description="Advanced quantitative trading and algorithmic analysis agent",
        system_prompt=QUANTITATIVE_TRADING_SYSTEM_PROMPT,
        model_name="anthropic/claude-fable-5",
        max_loops=max_loops,
        top_p=None,
        thinking_tokens=thinking_tokens,
        reasoning_effort=reasoning_effort,
        temperature=temperature,
        tools_list_dictionary=tools_list_dictionary,
        **kwargs,
    )


# Convenience instance for quick use
quantitative_trading_agent = create_quantitative_trading_agent()
