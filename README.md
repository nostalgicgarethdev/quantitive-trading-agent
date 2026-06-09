# quantitive-trading-agent

An advanced AI agent for quantitative finance, trading, and algorithmic analysis, built with the [swarms](https://github.com/kyegomez/swarms) framework.

Powered by **Anthropic Claude Fable 5** (the Mythos-class model made safe for general use).

## Features

- Deep expertise in ETFs, equities, derivatives, and portfolio construction
- Data-driven analysis with performance metrics, expense ratios, holdings, liquidity, and risk factors
- Clear, professional output using tables and structured reasoning
- Configurable high-reasoning mode suitable for complex financial tasks
- Easy to extend with custom tools

## Installation

```bash
git clone https://github.com/nostalgicgarethdev/quantitive-trading-agent.git
cd quantitive-trading-agent
pip install -r requirements.txt
```

Set your Anthropic API key (required for Claude Fable 5):

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

> **Note**: Claude Fable 5 is a new flagship model. Ensure your API key has access to `anthropic/claude-fable-5`.

## Quick Start

```bash
python main.py
```

## Usage as a Module

```python
from quantitive_trading_agent.agent import create_quantitative_trading_agent

agent = create_quantitative_trading_agent()

result = agent.run(
    task="Compare the top semiconductor ETFs including SMH, SOXX, and XSD. Focus on expense ratios, top holdings, and recent performance."
)

print(result)
```

## Example Task (Semiconductor ETFs)

The included `main.py` runs a detailed comparison of semiconductor ETFs using Claude Fable 5 with high reasoning effort.

## Project Structure

```
quantitive-trading-agent/
├── quantitive_trading_agent/
│   ├── __init__.py
│   └── agent.py           # Reusable agent factory
├── examples/
│   └── semiconductor_etf_analysis.py
├── main.py
├── requirements.txt
└── README.md
```

## Configuration

The agent uses these swarms settings optimized for finance:

- `model_name="anthropic/claude-fable-5"`
- `reasoning_effort="high"`
- `thinking_tokens=1024`
- `max_loops=1`

You can easily modify `create_quantitative_trading_agent()` to add tools (e.g. web search, code interpreter, yfinance data fetching).

## Extending the Agent

Add tools via `tools_list_dictionary` or by subclassing. Example tools you might add:

- Real-time market data (yfinance, polygon)
- SEC filings parser
- Backtesting engine
- News sentiment

## Disclaimer

This project provides analytical research and comparison tools. It does **not** provide financial advice. Always do your own research and consult professionals before making investment decisions.

## License

MIT

## Acknowledgments

- Built with [swarms](https://github.com/kyegomez/swarms)
- Powered by Anthropic's Claude Fable 5
