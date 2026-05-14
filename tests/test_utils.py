import pytest
import pandas as pd
from src.utils import load_data, enforce_dtypes, calculate_tail_metrics


def test_enforce_dtypes():
    df = pd.DataFrame(
        {
            "order date": ["2024-01-01", "2024-01-02"],
            "shipping date": ["2024-01-03", "2024-01-04"],
        }
    )
    result = enforce_dtypes(df)
    assert isinstance(result, pd.DataFrame)
    assert "order_date" in result.columns


def test_calculate_tail_metrics():
    s = pd.Series([1.0, 2.0, 3.0, 4.0, 10.0])
    metrics = calculate_tail_metrics(s, name="test")
    assert "p95" in metrics
    assert "p99" in metrics
    assert 0 <= metrics["dpmo_late"] <= 1_000_000


@pytest.mark.skip(reason="requires local dataset not in CI")
def test_calculate_tail_metrics_real():
    df = load_data()
    df = enforce_dtypes(df)
    metrics = calculate_tail_metrics(df["late_delivery_risk"])
    assert metrics["p99.9"] >= metrics["mean"]
