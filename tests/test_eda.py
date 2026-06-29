"""Tests for reusable notebook EDA helpers."""

from pathlib import Path

import pandas as pd

from helpers.eda import add_calendar_flags, build_notebook_context, find_project_root


def test_find_project_root_from_notebooks_dir() -> None:
    notebooks_dir = Path(__file__).resolve().parents[1] / "notebooks"
    project_root = find_project_root(notebooks_dir)

    assert project_root == Path(__file__).resolve().parents[1]


def test_build_notebook_context_uses_repo_data_dirs() -> None:
    notebooks_dir = Path(__file__).resolve().parents[1] / "notebooks"
    context = build_notebook_context(notebooks_dir)

    assert context.data_dir == context.project_root / "data"
    assert context.processed_dir == context.data_dir / "processed"
    assert context.category_colors["FOODS"] == "tab:blue"


def test_add_calendar_flags_marks_known_dates() -> None:
    df = pd.DataFrame(
        {
            "ds": pd.to_datetime(["2015-12-24", "2015-12-25", "2015-11-26", "2016-01-01"]),
            "y": [1, 2, 3, 4],
        }
    )

    flagged = add_calendar_flags(df)

    assert flagged.loc[0, "is_christmas_eve"]
    assert flagged.loc[1, "is_christmas"]
    assert flagged.loc[2, "is_thanksgiving_window"]
    assert flagged.loc[3, "is_new_years_day"]
