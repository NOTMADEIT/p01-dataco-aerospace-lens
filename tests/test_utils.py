import pandas as pd
import pytest
from src.utils import load_data, enforce_dtypes, calculate_tail_metrics


def test_enforce_dtypes():
    df = pd.DataFrame(
        {
            "Order Date": ["2024-01-01", "2024-01-02"],
            "Shipping Date": ["2024-01-03", "2024-01-04"],
        }
    )
    result = enforce_dtypes(df)
    assert result["Order Date"].dtype == "datetime64[ns]"
    assert result["Shipping Date"].dtype == "datetime64[ns]"


def test_calculate_tail_metrics():
    df = pd.DataFrame(
        {
            "Days for shipping (real)": [1, 2, 3, 4, 10],
            "Delivery Status": [
                "Late delivery",
                "On time",
                "On time",
                "Late delivery",
                "On time",
            ],
        }
    )
    metrics = calculate_tail_metrics(df)
    assert metrics["p95_delay"] is not None
    assert 0 <= metrics["late_delivery_rate"] <= 1
