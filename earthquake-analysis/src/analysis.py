"""Analysis functions for the Earthquake Analysis System."""

from __future__ import annotations

from math import radians, sin, cos, sqrt, asin
from typing import Iterable

from models import AnalyzedEarthquake, EarthquakeEvent


EARTH_RADIUS_KM = 6371.0


def compute_risk_score(
    magnitude: float,
    depth: float,
    population_density: float,
) -> float:
    """Compute a normalized risk score from 0 to 100.

    Higher magnitude and population density increase risk.
    Lower depth (shallower earthquake) increases risk.
    """
    if magnitude < 0 or depth < 0 or population_density < 0:
        raise ValueError("Magnitude, depth, and population_density must be non-negative.")

    magnitude_component = min((magnitude / 10.0) * 50.0, 50.0)
    depth_component = max(0.0, 20.0 - min(depth, 700.0) / 35.0)
    population_component = min(population_density / 100.0, 30.0)

    return round(magnitude_component + depth_component + population_component, 2)


def estimate_damage_radius(magnitude: float) -> float:
    """Estimate a simple damage radius in kilometers from magnitude."""
    if magnitude < 0:
        raise ValueError("Magnitude must be non-negative.")
    return round(max(1.0, magnitude * 8.0), 2)


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Compute great-circle distance between two points in kilometers."""
    lat1_r, lon1_r, lat2_r, lon2_r = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2_r - lat1_r
    dlon = lon2_r - lon1_r
    a = sin(dlat / 2) ** 2 + cos(lat1_r) * cos(lat2_r) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    return EARTH_RADIUS_KM * c


def cluster_earthquakes(
    events: Iterable[EarthquakeEvent],
    distance_threshold_km: float = 100.0,
) -> list[list[EarthquakeEvent]]:
    """Group nearby earthquakes into hotspot clusters.

    This is a simple threshold-based clustering approach suitable for a course project.
    """
    if distance_threshold_km <= 0:
        raise ValueError("distance_threshold_km must be positive.")

    events = list(events)
    clusters: list[list[EarthquakeEvent]] = []
    used: set[int] = set()

    for i, event in enumerate(events):
        if i in used:
            continue

        cluster = [event]
        used.add(i)

        for j in range(i + 1, len(events)):
            if j in used:
                continue
            other = events[j]
            distance = haversine_distance(
                event.latitude,
                event.longitude,
                other.latitude,
                other.longitude,
            )
            if distance <= distance_threshold_km:
                cluster.append(other)
                used.add(j)

        clusters.append(cluster)

    return clusters


def build_analyzed_event(event: EarthquakeEvent, population_density: float) -> AnalyzedEarthquake:
    """Create an AnalyzedEarthquake object from a base event."""
    risk_score = compute_risk_score(event.magnitude, event.depth, population_density)
    damage_radius = estimate_damage_radius(event.magnitude)
    return AnalyzedEarthquake(
        magnitude=event.magnitude,
        depth=event.depth,
        location=event.location,
        timestamp=event.timestamp,
        latitude=event.latitude,
        longitude=event.longitude,
        risk_score=risk_score,
        damage_radius=damage_radius,
    )
