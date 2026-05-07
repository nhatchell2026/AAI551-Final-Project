"""Pytest test cases for the Earthquake Analysis System."""

from datetime import datetime
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from analysis import compute_risk_score
from models import EarthquakeEvent


def test_compute_risk_score_returns_expected_value() -> None:
    """Test that the risk score function returns a stable known result."""
    result = compute_risk_score(magnitude=6.0, depth=10.0, population_density=1000.0)
    assert result == 59.71


def test_earthquake_event_classifies_severity_correctly() -> None:
    """Test that the severity classification matches the magnitude."""
    event = EarthquakeEvent(
        magnitude=6.5,
        depth=12.0,
        location="Test Region",
        timestamp=datetime(2026, 1, 1, 12, 0, 0),
        latitude=40.0,
        longitude=-74.0,
    )
    assert event.classify_severity() == "Strong"
