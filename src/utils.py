import pandas as pd
import numpy as np
from pathlib import Path


def load_data(path: str = "data/DataCoSupplyChainDataset.csv") -> pd.DataFrame:
    """Load raw DataCo with dtype enforcement."""
    dtype = {
        "Type": "category",
        "Shipping Mode": "category",
        "Delivery Status": "category",
        "Late_delivery_risk": "int8",
    }
    df = pd.read_csv(
        path,
        dtype=dtype,
        parse_dates=["shipping date (DateOrders)", "order date (DateOrders)"],
        encoding="latin-1",
    )
    return df


def enforce_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Clean + pipe-friendly."""
    df = df.copy()
    df.columns = [
        col.strip().lower().replace(" ", "_").replace("(", "").replace(")", "")
        for col in df.columns
    ]
    return df


def calculate_tail_metrics(series: pd.Series, name: str = "metric") -> dict:
    """Aerospace lens ngay từ đầu."""
    return {
        "mean": series.mean(),
        "p50": series.quantile(0.5),
        "p95": series.quantile(0.95),
        "p99": series.quantile(0.99),
        "p99.9": series.quantile(0.999),
        "max": series.max(),
        "dpmo_late": (series > 0).mean() * 1_000_000,
    }
