from __future__ import annotations
import pandas as pd

def validate_table(df: pd.DataFrame, required: set[str]) -> dict:
    missing = sorted(required - set(df.columns))
    duplicates = int(df.duplicated().sum())
    nulls = int(df.isna().sum().sum())
    status = "PASS" if not missing and duplicates == 0 else "REVIEW"
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_required_columns": missing,
        "duplicate_rows": duplicates,
        "null_cells": nulls,
        "status": status,
    }
