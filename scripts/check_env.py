"""Quick environment validation script for onboarding a new machine."""

from importlib.metadata import version


def _print_pkg_version(package_name: str, distribution_name: str) -> None:
    try:
        print(f"{package_name}: {version(distribution_name)}")
    except Exception as exc:
        raise RuntimeError(f"Unable to verify required package '{package_name}': {exc}") from exc


def main() -> None:
    required_packages = [
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("scipy", "scipy"),
        ("scikit-learn", "scikit-learn"),
        ("statsmodels", "statsmodels"),
        ("statsforecast", "statsforecast"),
        ("mlforecast", "mlforecast"),
        ("datasetsforecast", "datasetsforecast"),
        ("lightgbm", "lightgbm"),
        ("polars", "polars"),
        ("pyarrow", "pyarrow"),
        ("duckdb", "duckdb"),
        ("matplotlib", "matplotlib"),
        ("plotly", "plotly"),
        ("jupyter", "jupyter"),
        ("ipykernel", "ipykernel"),
        ("pydantic", "pydantic"),
        ("typer", "typer"),
        ("rich", "rich"),
        ("loguru", "loguru"),
    ]

    for package_name, dist_name in required_packages:
        _print_pkg_version(package_name, dist_name)

    print("Environment check completed: required packages are available.")


if __name__ == "__main__":
    main()
