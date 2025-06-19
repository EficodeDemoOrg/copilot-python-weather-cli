"""Weather service layer for the weather CLI application."""

import logging
from typing import Optional

from .weather_data import WeatherData
from .weather_client import WeatherApiClient, OpenWeatherMapClient
from .exceptions import WeatherApiException

logger = logging.getLogger(__name__)


class WeatherService:
    """Service layer for weather operations."""

    def __init__(self, client: Optional[WeatherApiClient] = None) -> None:
        """Initialize the weather service.

        Args:
            client: Optional weather API client. If not provided, uses OpenWeatherMapClient.
        """
        self.client = client or OpenWeatherMapClient()
        logger.debug("WeatherService initialized")

    def get_weather(self, city: str) -> WeatherData:
        """Get weather information for a city.

        Args:
            city: The name of the city to get weather for

        Returns:
            WeatherData object containing the weather information

        Raises:
            WeatherApiException: If there's an error fetching weather data
        """
        if not city or not city.strip():
            logger.error("Empty city name provided")
            raise WeatherApiException("City name cannot be null or empty.")

        city = city.strip()
        logger.info(f"Fetching weather data for city: {city}")

        try:
            weather_data = self.client.get_weather_from_api(city)
            logger.info(f"Successfully retrieved weather data for {weather_data.city}")
            return weather_data

        except WeatherApiException:
            logger.error(f"Failed to fetch weather data for city: {city}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error while fetching weather data for {city}: {e}")
            raise WeatherApiException(f"Unexpected error: {str(e)}")
