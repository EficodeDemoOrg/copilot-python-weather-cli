"""Weather data model for the weather CLI application."""

from dataclasses import dataclass


@dataclass(frozen=True)
class WeatherData:
    """Immutable data class representing weather information for a city.

    Attributes:
        city: The name of the city
        temperature_celsius: The current temperature in Celsius
        description: A description of the current weather conditions
    """

    city: str
    temperature_celsius: float
    description: str

    def __post_init__(self) -> None:
        """Validate the data types after initialization."""
        if not isinstance(self.city, str):
            raise TypeError("city must be a string")
        if not isinstance(self.temperature_celsius, (int, float)):
            raise TypeError("temperature_celsius must be a number")
        if not isinstance(self.description, str):
            raise TypeError("description must be a string")

        if not self.city.strip():
            raise ValueError("city cannot be empty")
        if not self.description.strip():
            raise ValueError("description cannot be empty")

    def __str__(self) -> str:
        """Return a formatted string representation of the weather data.

        Returns:
            A user-friendly string showing the weather information
        """
        return (
            f"Weather for {self.city}:\n"
            f"Temperature: {self.temperature_celsius:.1f}°C\n"
            f"Conditions: {self.description}"
        )
