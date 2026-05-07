"""Input and output helpers for the Earthquake Analysis System."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Generator

import pandas as pd

from models import EarthquakeEvent


class DataLoadError(Exception):
    """Raised when earthquake data cannot be loaded correctly."""


REQUIRED_COLUMNS = {"mag", "depth", "place", "time", "latitude", "longitude"}


def load_earthquake_dataframe(csv_path: str | Path) -> pd.DataFrame:
    """Load a USGS earthquake CSV file into a DataFrame."""
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise DataLoadError(f"File not found: {csv_path}")

    try:
        df = pd.read_csv(csv_path)
    except Exception as exc:
        raise DataLoadError(f"Could not read CSV file: {exc}") from exc

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise DataLoadError(f"Missing required columns: {sorted(missing)}")

    return df


def earthquake_generator(csv_path: str | Path) -> Generator[EarthquakeEvent, None, None]:
    """Yield one EarthquakeEvent at a time from a USGS CSV file."""
    df = load_earthquake_dataframe(csv_path)

    for _, row in df.iterrows():
        yield EarthquakeEvent(
            magnitude=float(row["mag"]),
            depth=float(row["depth"]),
            location=str(row["place"]),
            timestamp=pd.to_datetime(row["time"]).to_pydatetime(),
            latitude=float(row["latitude"]),
            longitude=float(row["longitude"]),
        )


def save_results(dataframe: pd.DataFrame, output_path: str | Path) -> None:
    """Save processed earthquake results to a CSV file."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False)
