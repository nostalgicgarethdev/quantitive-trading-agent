"""
Quantitative Trading Agent Module

Reusable factory for creating agents using Anthropic Claude Fable 5
with swarms, following official best practices from the docs.

See: https://docs.swarms.world/examples/model-providers/claude-fable-5
"""

from swarms import Agent
from typing import Optional, List, Dict, Any

# The exact system prompt featured in the official Swarms Claude Fable 5 docs
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
    system_prompt: Optional[str] = None,
    max_loops: int = 1,
    thinking_tokens: int = 1024,
    reasoning_effort: str = "high",
    temperature: Optional[float] = None,
    tools_list_dictionary: Optional[List[Dict[str, Any]]] = None,
    streaming_on: bool = False,
    persistent_memory: bool = False,
    context_compression: bool = False,
    context_length: int = 200_000,
    autosave: bool = False,
    **kwargs
) -> Agent:
    """
    Factory for a Claude Fable 5 powered Quantitative Trading Agent.

    IMPORTANT (from official docs):
    - temperature must be None (Fable 5 does not support it)
    - top_p must be None
    - tools_list_dictionary must be None (tools/function calling not supported on Fable 5)

    For tool use, use a different model (e.g. claude-sonnet-4-6) as a data collector
    and Fable 5 as the reasoning/synthesis layer.

    Args:
        agent_name: Name of the agent
        system_prompt: Custom system prompt (defaults to the official Quantitative-Trading-Agent prompt)
        max_loops: Number of loops ("auto" for autonomous agents)
        thinking_tokens: Budget for extended thinking (1024–16000+ recommended for hard tasks)
        reasoning_effort: "low" | "medium" | "high"
        temperature: Must be None for Fable 5
        tools_list_dictionary: Must be None for Fable 5
        streaming_on: Enable token streaming
        persistent_memory: Survive restarts (good for long-running agents)
        context_compression: Auto-summarize context
        context_length: Max context window
        autosave: Snapshot state after runs
        **kwargs: Passed through to swarms.Agent

    Returns:
        Configured swarms.Agent using anthropic/claude-fable-5
    """
    if system_prompt is None:
        system_prompt = QUANTITATIVE_TRADING_SYSTEM_PROMPT

    return Agent(
        agent_name=agent_name,
        agent_description="Advanced quantitative trading and algorithmic analysis agent",
        system_prompt=system_prompt,
        model_name="anthropic/claude-fable-5",
        max_loops=max_loops,
        top_p=None,                           # Required for Fable 5
        thinking_tokens=thinking_tokens,
        reasoning_effort=reasoning_effort,
        temperature=temperature,              # Must be None
        tools_list_dictionary=tools_list_dictionary,  # Must be None
        streaming_on=streaming_on,
        persistent_memory=persistent_memory,
        context_compression=context_compression,
        context_length=context_length,
        autosave=autosave,
        **kwargs,
    )


# Default production-ready instance (follows official best practices)
quantitative_trading_agent = create_quantitative_trading_agent(
    thinking_tokens=2048,
    reasoning_effort="medium",
    persistent_memory=True,
    context_compression=True,
    autosave=True,
)
