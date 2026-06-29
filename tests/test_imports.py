"""Smoke tests ensuring the package layout remains importable."""

from importlib import import_module


def test_package_imports() -> None:
    package_imports = [
        "retail_replenishment",
        "retail_replenishment.config",
        "retail_replenishment.data",
        "retail_replenishment.data.load_datasets",
        "retail_replenishment.features",
        "retail_replenishment.features.calendar_features",
        "retail_replenishment.forecasting",
        "retail_replenishment.forecasting.baseline_models",
        "retail_replenishment.inventory",
        "retail_replenishment.inventory.reorder_policy",
        "retail_replenishment.allocation",
        "retail_replenishment.allocation.priority_score",
        "retail_replenishment.simulation",
        "retail_replenishment.simulation.inventory_simulator",
        "retail_replenishment.visualization",
        "retail_replenishment.visualization.plots",
    ]

    for module_name in package_imports:
        imported = import_module(module_name)
        assert imported is not None
