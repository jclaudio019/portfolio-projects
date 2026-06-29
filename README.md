# Retail Replenishment & Allocation Engine

This public portfolio project builds a supply-chain analytics workflow for retail inventory planning.

## Business problem

Retail teams need a structured way to forecast SKU-store demand, estimate risk and variability, and convert forecasts into operational replenishment decisions such as safety stock, reorder points, stockout prevention, and allocation priorities.

## Planned data sources

- Store Item Demand Forecasting Challenge
- M5 Forecasting Walmart
- Favorita Grocery Sales
- Optional extension: FreshRetailNet

## Planned modeling workflow

1. Demand forecasting
2. Forecast uncertainty estimation
3. Safety stock calculation
4. Reorder point logic
5. Inventory simulation
6. Allocation priority scoring

## Setup

```bash
uv sync
uv run python scripts/check_env.py
uv run pytest
uv run ruff check .
```

If you want development dependencies (pytest, ruff, mypy, pre-commit, nbstripout) installed with the editable project environment, include them in your project sync workflow according to `pyproject.toml`.

## Data and privacy notes

This portfolio project uses only public datasets and does not use private/internal company data.
