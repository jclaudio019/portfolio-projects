"""Notebook-friendly EDA helpers for the M5 retail time-series workflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import warnings

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


CATEGORY_COLORS = {
    "FOODS": "tab:blue",
    "HOBBIES": "tab:orange",
    "HOUSEHOLD": "tab:green",
}


@dataclass(frozen=True)
class NotebookContext:
    """Resolved project paths and shared plotting colors for notebook work."""

    project_root: Path
    data_dir: Path
    processed_dir: Path
    category_colors: dict[str, str] = field(default_factory=lambda: CATEGORY_COLORS.copy())


def find_project_root(start: Path | None = None) -> Path:
    """Find the repo root from a notebook or script location."""

    start_path = (start or Path.cwd()).resolve()
    for candidate in (start_path, *start_path.parents):
        helper_dir = candidate / "helpers"
        if (candidate / "pyproject.toml").exists() and helper_dir.exists():
            return candidate
    raise FileNotFoundError("Could not locate the project root.")


def build_notebook_context(start: Path | None = None) -> NotebookContext:
    """Resolve reusable paths for EDA notebooks and scripts."""

    project_root = find_project_root(start)
    data_dir = project_root / "data"
    processed_dir = data_dir / "processed"
    return NotebookContext(
        project_root=project_root,
        data_dir=data_dir,
        processed_dir=processed_dir,
    )


def configure_notebook_display() -> None:
    """Apply a consistent, portfolio-friendly notebook display style."""

    warnings.filterwarnings("ignore", category=FutureWarning)
    sns.set_theme(style="white")
    plt.rcParams["figure.figsize"] = (14, 6)
    plt.rcParams["axes.grid"] = False
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False
    pd.set_option("display.max_columns", 100)
    pd.set_option("display.float_format", "{:,.2f}".format)


def bootstrap_notebook(start: Path | None = None) -> NotebookContext:
    """Configure plotting and return the resolved notebook context."""

    configure_notebook_display()
    context = build_notebook_context(start)
    context.processed_dir.mkdir(parents=True, exist_ok=True)
    return context


def finish_axis(
    ax,
    title: str,
    xlabel: str,
    ylabel: str,
    rotation: int = 0,
):
    """Apply consistent titles, labels, and tick handling to plots."""

    ax.set_title(title, pad=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(False)
    if rotation:
        plt.setp(ax.get_xticklabels(), rotation=rotation, ha="right")
    plt.tight_layout()
    return ax


def plot_category_multiline(
    df: pd.DataFrame,
    title: str,
    color_map: dict[str, str] | None = None,
) -> None:
    """Plot all categories together as a daily time-series view."""

    colors = color_map or CATEGORY_COLORS
    pivot = df.pivot(index="ds", columns="cat_id", values="y")
    ax = pivot.plot(
        figsize=(16, 7),
        color=[colors.get(col, "tab:gray") for col in pivot.columns],
    )
    finish_axis(ax, title=title, xlabel="Date", ylabel="Units Sold")
    plt.show()


def plot_category_panels(
    df: pd.DataFrame,
    title_suffix: str,
    color_map: dict[str, str] | None = None,
) -> None:
    """Plot one time-series panel per category."""

    colors = color_map or CATEGORY_COLORS
    for cat in sorted(df["cat_id"].unique()):
        data = df.loc[df["cat_id"].eq(cat)].sort_values("ds")
        ax = data.plot(
            x="ds",
            y="y",
            figsize=(16, 5),
            legend=False,
            color=colors.get(cat, "tab:gray"),
        )
        finish_axis(
            ax,
            title=f"Daily Sales - {cat} | {title_suffix}",
            xlabel="Date",
            ylabel="Units Sold",
        )
        plt.show()


def plot_category_bar_panels(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title_prefix: str,
    xlabel: str,
    ylabel: str,
    rotation: int = 0,
    color_map: dict[str, str] | None = None,
) -> None:
    """Plot one bar chart per category for seasonal summaries."""

    colors = color_map or CATEGORY_COLORS
    for cat in sorted(df["cat_id"].unique()):
        data = df.loc[df["cat_id"].eq(cat)]
        ax = data.plot(
            x=x_col,
            y=y_col,
            kind="bar",
            figsize=(10, 4),
            legend=False,
            color=colors.get(cat, "tab:gray"),
            edgecolor="black",
            alpha=0.80,
        )
        finish_axis(
            ax,
            title=f"{title_prefix} - {cat}",
            xlabel=xlabel,
            ylabel=ylabel,
            rotation=rotation,
        )
        plt.show()


def plot_category_histograms(
    df: pd.DataFrame,
    title_suffix: str,
    density: bool = False,
    color_map: dict[str, str] | None = None,
) -> None:
    """Plot one histogram per category with mean and median markers."""

    colors = color_map or CATEGORY_COLORS
    y_label = "Density" if density else "Frequency"
    view_label = "Density" if density else "Frequency"

    for cat in sorted(df["cat_id"].unique()):
        data = df.loc[df["cat_id"].eq(cat), "y"]
        mean_sales = data.mean()
        median_sales = data.median()

        ax = data.hist(
            bins="sqrt",
            density=density,
            figsize=(12, 4),
            color=colors.get(cat, "tab:gray"),
            edgecolor="black",
            alpha=0.45,
        )
        ax.axvline(mean_sales, color="black", linestyle="--", label=f"Mean: {mean_sales:,.0f}")
        ax.axvline(median_sales, color="red", linestyle=":", label=f"Median: {median_sales:,.0f}")
        finish_axis(
            ax,
            title=f"{cat} Sales Distribution | {title_suffix} | {view_label}",
            xlabel="Daily Units Sold",
            ylabel=y_label,
        )
        ax.legend()
        plt.show()


def add_calendar_flags(df: pd.DataFrame) -> pd.DataFrame:
    """Add simple reusable calendar flags for time-series EDA."""

    out = df.copy()
    out["year"] = out["ds"].dt.year
    out["month"] = out["ds"].dt.month
    out["day"] = out["ds"].dt.day
    out["dayofweek"] = out["ds"].dt.day_name()
    out["weekofyear"] = out["ds"].dt.isocalendar().week.astype(int)
    out["is_christmas"] = out["month"].eq(12) & out["day"].eq(25)
    out["is_christmas_eve"] = out["month"].eq(12) & out["day"].eq(24)
    out["is_day_after_christmas"] = out["month"].eq(12) & out["day"].eq(26)
    out["is_new_years_day"] = out["month"].eq(1) & out["day"].eq(1)
    out["is_thanksgiving_window"] = out["month"].eq(11) & out["day"].between(22, 28)
    return out
