"""Smoke tests ensuring the package layout remains importable."""

from importlib import import_module


def test_helpers_imports() -> None:
    helper_imports = [
        "helpers",
        "helpers.eda",
    ]

    for module_name in helper_imports:
        imported = import_module(module_name)
        assert imported is not None
