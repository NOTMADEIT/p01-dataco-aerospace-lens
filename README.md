# P01 — DataCo Aerospace Lens

## Project Aerospace Framing
This project applies supply chain analytics to the DataCo Global dataset through an aerospace-grade lens: where late deliveries are not inconveniences but mission-critical failures. We treat tail-risk metrics, delivery reliability, and logistics network vulnerabilities with the same rigor used in aerospace operations — because in high-stakes supply chains, the 5% worst-case scenario defines system resilience.

## Structure

- data/ — raw data (gitignored)
- notebooks/ — EDA and exploration
- src/ — production functions
- reports/ — markdown + figures
- tests/ — pytest
- .github/ — CI/CD workflows

## Stack
- Python 3.11 | uv | pandas | numpy | matplotlib | seaborn | networkx | streamlit
- CI: GitHub Actions (black + ruff + pytest)

## Quick Start

uv sync

uv run pytest tests/ -v