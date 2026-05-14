import pandas as pd
import numpy as np
from pathlib import Path


def load_data(filepath: str) -> pd.DataFrame:
    """Load CSV data from filepath."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    return pd.read_csv(path)


def enforce_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Enforce correct data types for DataCo dataset."""
    df = df.copy()
    if "Order Date" in df.columns:
        df["Order Date"] = pd.to_datetime(df["Order Date"])
    if "Shipping Date" in df.columns:
        df["Shipping Date"] = pd.to_datetime(df["Shipping Date"])
    return df


def calculate_tail_metrics(df: pd.DataFrame) -> dict:
    """Calculate tail-risk metrics for supply chain."""
    metrics = {
        "p95_delay": np.percentile(df["Days for shipping (real)"], 95)
        if "Days for shipping (real)" in df.columns
        else None,
        "late_delivery_rate": (df["Delivery Status"] == "Late delivery").mean()
        if "Delivery Status" in df.columns
        else None,
    }
    return metrics