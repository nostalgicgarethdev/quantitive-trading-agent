#!/bin/bash
# Simple script to run several key examples

set -e

echo "=== Running Basic Single Agent ==="
python main.py

echo ""
echo "=== Running Multi-Agent Sequential ==="
python examples/multi_agent_sequential.py

echo ""
echo "=== Running Streaming Example ==="
python examples/streaming_analysis.py

echo ""
echo "All selected examples completed."
