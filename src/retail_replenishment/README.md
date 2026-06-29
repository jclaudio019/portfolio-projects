# Retail Replenishment Package

This package contains the core Python scaffold for the **Retail Replenishment & Allocation Engine** portfolio project.

It is the implementation layer behind a broader retail supply chain analytics workflow focused on:

- demand forecasting
- forecast uncertainty
- safety stock and reorder policy design
- stockout risk monitoring
- inventory simulation
- allocation priority scoring

## Current State

The package is intentionally in an early scaffold phase. We have set up the environment, module layout, validation scripts, and placeholder interfaces so the project can grow in a structured way without pretending the forecasting system is already production-ready.

Current components include:

- `config.py` for shared project configuration
- `data/` for dataset loading utilities
- `features/` for calendar and feature engineering helpers
- `forecasting/` for baseline model entry points
- `inventory/` for reorder policy logic
- `allocation/` for priority scoring logic
- `simulation/` for inventory simulation workflows
- `visualization/` for plotting helpers

## Planning Context

The current project direction is informed by M5 retail demand analysis and portfolio planning work centered on category-level demand behavior. The immediate analytical goal is to build a defensible path from retail demand understanding to replenishment decision support.

The current business framing is:

- retailers need demand visibility before they can make good replenishment decisions
- category-level demand behavior should be understood before jumping to SKU-store modeling
- calendar effects and abnormal demand periods should be modeled explicitly instead of being casually removed

This means the package is being shaped to support a workflow that moves from:

1. exploratory demand analysis
2. baseline forecasting
3. uncertainty-aware inventory policy logic
4. simulation and allocation decision support

## Framework Influence

This project is also being structured using a proprietary framework shared by a mentor. That framework influences how the work is organized, framed, and communicated across:

- problem definition
- business context
- analytical discovery
- execution planning
- recommendations and next steps

The framework is used here as a planning and storytelling aid rather than something being reproduced or published in full. This repository only includes the implementation artifacts and public-facing synthesis derived from that process.

## What Is Built vs Planned

Built now:

- the `uv`-based Python environment
- the package/module structure
- notebook scaffolds
- environment validation and lightweight import tests
- placeholder interfaces for the main retail analytics domains

Planned next:

- M5 data loading and standardized local storage patterns
- category-level baseline forecasts
- calendar and event feature engineering
- reorder point and safety stock calculations
- inventory simulation experiments
- allocation scoring logic tied to forecast outputs

## Intended Use

This README is meant to orient future development inside `src/retail_replenishment` so the codebase stays connected to the business problem:

- not just forecasting for its own sake
- not just notebooks without operational structure
- not just model accuracy without replenishment relevance

The goal is to turn retail demand analysis into a coherent supply chain analytics portfolio project with clear business value and reproducible technical structure.
