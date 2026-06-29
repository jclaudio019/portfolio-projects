"""Centralized configuration placeholders for portfolio stage."""

from dataclasses import dataclass


@dataclass
class AppConfig:
    project_name: str = "retail-replenishment-allocation-engine"
    forecast_horizon_days: int = 7
    default_service_level: float = 0.95
