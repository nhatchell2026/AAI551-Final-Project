"""Data models for the Earthquake Analysis System."""

from __future__ import annotations

from datetime import datetime


class EarthquakeEvent:
    """Represents a single earthquake event.

    Attributes:
        magnitude: Magnitude of the earthquake.
        depth: Focal depth in kilometers.
        location: Human-readable place name.
        timestamp: Time the event occurred.
        latitude: Latitude coordinate.
        longitude: Longitude coordinate.
    """

    def __init__(
        self,
        magnitude: float,
        depth: float,
        location: str,
        timestamp: datetime,
        latitude: float,
        longitude: float,
    ) -> None:
        if magnitude < 0:
            raise ValueError("Magnitude cannot be negative.")
        if not -90 <= latitude <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        if not -180 <= longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180.")

        self.magnitude = float(magnitude)
        self.depth = float(depth)
        self.location = str(location)
        self.timestamp = timestamp
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def classify_severity(self) -> str:
        """Return a label describing earthquake severity."""
        if self.magnitude < 4.0:
            return "Minor"
        if self.magnitude < 6.0:
            return "Moderate"
        if self.magnitude < 7.0:
            return "Strong"
        return "Major"

    def __str__(self) -> str:
        """Return a readable summary of the earthquake event."""
        return (
            f"EarthquakeEvent(location='{self.location}', magnitude={self.magnitude}, "
            f"depth={self.depth} km, time={self.timestamp.isoformat()})"
        )

    def __eq__(self, other: object) -> bool:
        """Compare two earthquake events by their main identifying fields."""
        if not isinstance(other, EarthquakeEvent):
            return NotImplemented
        return (
            self.magnitude == other.magnitude
            and self.depth == other.depth
            and self.location == other.location
            and self.timestamp == other.timestamp
            and self.latitude == other.latitude
            and self.longitude == other.longitude
        )


class AnalyzedEarthquake(EarthquakeEvent):
    """Earthquake event extended with analysis outputs."""

    def __init__(
        self,
        magnitude: float,
        depth: float,
        location: str,
        timestamp: datetime,
        latitude: float,
        longitude: float,
        risk_score: float = 0.0,
        damage_radius: float = 0.0,
    ) -> None:
        super().__init__(magnitude, depth, location, timestamp, latitude, longitude)
        self.risk_score = float(risk_score)
        self.damage_radius = float(damage_radius)

    def summary_dict(self) -> dict:
        """Return a dictionary summary for exporting or display."""
        return {
            "location": self.location,
            "magnitude": self.magnitude,
            "depth": self.depth,
            "timestamp": self.timestamp.isoformat(),
            "latitude": self.latitude,
            "longitude": self.longitude,
            "severity": self.classify_severity(),
            "risk_score": self.risk_score,
            "damage_radius": self.damage_radius,
        }
