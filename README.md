# quantitive-trading-agent

**CA:** `AvSWbdTVPdSaLa7cYJ3sRTgvQHZEcW1HN8g6xuvsswrm`

An advanced AI agent (and multi-agent systems) for quantitative finance, trading, and algorithmic analysis, built with the [swarms](https://github.com/kyegomez/swarms) framework.

**Officially aligned with the Swarms Claude Fable 5 documentation**:
https://docs.swarms.world/examples/model-providers/claude-fable-5

Powered by **Anthropic Claude Fable 5** (the public Mythos-class model).

## Features

- Single high-performance Fable 5 agent with production-grade defaults
- Full suite of **multi-agent architectures** using Fable 5
- Follows all official limitations and best practices (no tools on Fable 5, temperature=None, etc.)
- Includes the exact "Quantitative-Trading-Agent" system prompt featured in the official docs
- Pattern for combining tool-calling models with Fable 5 reasoning

## Token

**CA:** `AvSWbdTVPdSaLa7cYJ3sRTgvQHZEcW1HN8g6xuvsswrm`

This is the official contract address for the project's community token.

- [View on Solscan](https://solscan.io/token/AvSWbdTVPdSaLa7cYJ3sRTgvQHZEcW1HN8g6xuvsswrm)
- [View on Birdeye](https://birdeye.so/token/AvSWbdTVPdSaLa7cYJ3sRTgvQHZEcW1HN8g6xuvsswrm)

## Installation

```bash
git clone https://github.com/nostalgicgarethdev/quantitive-trading-agent.git
cd quantitive-trading-agent
pip install -r requirements.txt
```

Set your Anthropic API key:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

> **Note**: Claude Fable 5 access is required. The model is automatically routed via LiteLLM in Swarms.

## Quick Start (Single Agent)

```bash
python main.py
```

Or as a module:

```python
from quantitive_trading_agent.agent import create_quantitative_trading_agent

agent = create_quantitative_trading_agent()

result = agent.run(
    task="Compare SMH, SOXX, and XSD semiconductor ETFs including performance, holdings, and strategy."
)
print(result)
```

## Multi-Agent Systems with Fable 5

This repo includes ready-to-run examples of every major pattern from the official docs:

### Sequential Workflow
Researcher → Analyst → Writer pipeline for high-quality reports.

```bash
python examples/multi_agent_sequential.py
```

### Concurrent Workflow
Multiple specialized Fable 5 experts run in parallel.

```bash
python examples/multi_agent_concurrent.py
```

### Mixture of Agents (MoA)
Cheaper worker models generate ideas → Fable 5 synthesizes the best answer (great for cost + quality).

```bash
python examples/multi_agent_mixture.py
```

### Hierarchical Swarm
Fable 5 as Director that decomposes tasks and delegates to faster worker agents.

```bash
python examples/multi_agent_hierarchical.py
```

### Tool + Fable 5 Pattern (Recommended when you need real data)
Fable 5 does **not** support tools. Use a tool-capable model (Sonnet/Haiku/GPT) to fetch data, then Fable 5 for deep analysis.

```bash
python examples/tool_pattern_data_collector.py
```

## Core Agent Factory

The `create_quantitative_trading_agent()` function is pre-configured with the correct Fable 5 settings:

- `model_name="anthropic/claude-fable-5"`
- `temperature=None` and `top_p=None` (required)
- `tools_list_dictionary=None` (tools not supported on Fable 5)
- `thinking_tokens` + `reasoning_effort` for extended thinking
- Production options: `persistent_memory`, `context_compression`, `autosave`

## Reusable Prompts

The package includes a collection of specialized system prompts in `quantitive_trading_agent/prompts.py`:

```python
from quantitive_trading_agent.prompts import (
    get_prompt,
    ETF_RESEARCHER,
    QUANTITATIVE_ANALYST,
    STRATEGY_CODER,
)

prompt = get_prompt("etf_researcher")
```

Available roles: `quantitative_trading`, `etf_researcher`, `quant_analyst`, `report_writer`, `technical`, `macro`, `risk`, `strategy_coder`.

## Additional Examples

| File | Description |
|------|-------------|
| `examples/autonomous_research.py` | Long-running autonomous agent with `max_loops="auto"` + persistent memory |
| `examples/streaming_analysis.py` | Real-time token streaming from Fable 5 |
| `examples/strategy_code_generation.py` | Ask Fable 5 to write complete backtesting / trading strategy code |
| `examples/vision_chart_analysis.py` | Using Fable 5's vision capabilities to analyze charts (provide your own image) |

### Running All Examples

```bash
python examples/semiconductor_etf_analysis.py
python examples/multi_agent_sequential.py
python examples/autonomous_research.py   # Can take several minutes
```

## Advanced Usage

### Custom Configuration

```python
from quantitive_trading_agent.agent import create_quantitative_trading_agent

agent = create_quantitative_trading_agent(
    thinking_tokens=4096,
    reasoning_effort="high",
    max_loops="auto",
    persistent_memory=True,
    autosave=True,
)
```

### Combining with Tools (Recommended Pattern)

See `examples/tool_pattern_data_collector.py` for the correct way to use real data with Fable 5.

## Production Best Practices

- Start with `thinking_tokens=1024` or `2048` and `reasoning_effort="medium"`
- Only use `reasoning_effort="high"` + high `thinking_tokens` when the task truly benefits
- Use Fable 5 as the **top of the hierarchy** (director / aggregator) for cost efficiency
- Enable `persistent_memory` and `autosave` for any long-running research
- Set `max_loops` explicitly in production instead of always using `"auto"`

## Project Structure

```
quantitive-trading-agent/
├── quantitive_trading_agent/
│   ├── __init__.py
│   ├── agent.py
│   └── prompts.py
├── examples/
│   ├── *.py (many ready-to-run examples)
├── main.py
├── requirements.txt
├── .env.example
├── README.md
└── LICENSE
```

## Next Steps / Ideas

- Add your own tools (use a Sonnet agent for data fetching)
- Build a simple Streamlit or Gradio UI around the agent
- Connect to real data providers (Polygon, FMP, etc.)
- Implement agent-to-agent memory sharing

## Disclaimer

This project and all generated analysis are for **research and educational purposes only**. Nothing here constitutes financial advice. Always do your own due diligence.

See `quantitive_trading_agent/agent.py` for full options.

## Important Fable 5 Limitations (per official docs)

- **No tools/function calling** — Always use `tools_list_dictionary=None`
- **No temperature** — Always pass `temperature=None`
- Use Fable 5 for deep reasoning/synthesis. Pair it with Sonnet/Haiku/GPT when you need tool use or speed.

## Production Tips (from the docs)

- Use `thinking_tokens=2048`–`8192` + `reasoning_effort="high"` for hard problems
- Prefer Fable 5 as the **aggregator/director** in multi-agent systems rather than every worker
- Enable `persistent_memory=True`, `context_compression=True`, and `autosave=True` for long-running agents
- Set `max_loops` explicitly in production

## Examples

| File | Description |
|------|-------------|
| `main.py` | Basic single-agent semiconductor ETF analysis |
| `examples/semiconductor_etf_analysis.py` | Focused ETF comparison |
| `examples/portfolio_risk_analysis.py` | Portfolio construction discussion |
| `examples/multi_agent_*.py` | All major multi-agent patterns |
| `examples/tool_pattern_data_collector.py` | Tool-augmented workflow |

## Disclaimer

This project is for research and educational purposes. It does not provide financial advice.

## Acknowledgments

- Built on [swarms](https://github.com/kyegomez/swarms)
- Directly based on the official [Claude Fable 5 + Swarms documentation](https://docs.swarms.world/examples/model-providers/claude-fable-5)
- Powered by Anthropic Claude Fable 5

## License

MIT
