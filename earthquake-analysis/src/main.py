"""Main entry point for the Earthquake Analysis System."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from analysis import build_analyzed_event, cluster_earthquakes
from io_utils import earthquake_generator, save_results


DEFAULT_POPULATION_DENSITY = 500.0


def main() -> None:
    """Run a simple end-to-end earthquake analysis workflow."""
    data_path = Path("data/earthquakes.csv")
    output_path = Path("results/analysis_results.csv")

    events = list(earthquake_generator(data_path))
    analyzed_events = [
        build_analyzed_event(event, DEFAULT_POPULATION_DENSITY)
        for event in events
    ]

    results_df = pd.DataFrame([event.summary_dict() for event in analyzed_events])
    save_results(results_df, output_path)

    clusters = cluster_earthquakes(events)
    print(f"Loaded {len(events)} earthquake events.")
    print(f"Detected {len(clusters)} hotspot clusters.")
    print(f"Saved results to: {output_path}")

    plot_magnitude_histogram(results_df)


def plot_magnitude_histogram(results_df: pd.DataFrame) -> None:
    """Display a histogram of earthquake magnitudes."""
    plt.figure(figsize=(8, 5))
    plt.hist(results_df["magnitude"], bins=10, edgecolor="black")
    plt.title("Earthquake Magnitude Distribution")
    plt.xlabel("Magnitude")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
