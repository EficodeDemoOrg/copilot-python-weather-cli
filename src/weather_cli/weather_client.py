"""Weather API client for the weather CLI application."""

import logging
import re
import urllib.parse
from abc import ABC, abstractmethod
from typing import Dict, Any, NoReturn

import requests

from .weather_data import WeatherData
from .config_util import ConfigUtil
from .exceptions import WeatherApiException

logger = logging.getLogger(__name__)


class WeatherApiClient(ABC):
    """Abstract base class for weather API clients."""

    @abstractmethod
    def get_weather_from_api(self, city: str) -> WeatherData:
        """Get weather data for a city from the API.

        Args:
            city: The name of the city to get weather for

        Returns:
            WeatherData object containing the weather information

        Raises:
            WeatherApiException: If there's an error fetching weather data
        """
        pass


class OpenWeatherMapClient(WeatherApiClient):
    """OpenWeatherMap API client implementation."""

    # Regex pattern for valid city names (letters, numbers, spaces, hyphens, periods)
    CITY_NAME_PATTERN = re.compile(r"^[\w\s\-\.]+$", re.UNICODE)
    REQUEST_TIMEOUT = 30

    def __init__(self) -> None:
        """Initialize the OpenWeatherMap client."""
        self.api_key = ConfigUtil.get_api_key()
        self.base_url = ConfigUtil.get_api_base_url()

    def get_weather_from_api(self, city: str) -> WeatherData:
        """Get weather data for a city from the OpenWeatherMap API.

        Args:
            city: The name of the city to get weather for

        Returns:
            WeatherData object containing the weather information

        Raises:
            WeatherApiException: If there's an error fetching weather data
        """
        self._validate_city_name(city)

        url = self._build_api_url(city)

        try:
            logger.debug(f"Making API request to: {self._redact_api_key(url)}")
            response = requests.get(url, timeout=self.REQUEST_TIMEOUT)

            logger.debug(f"API response status code: {response.status_code}")

            if response.status_code == 200:
                return self._parse_weather_response(response.json())
            else:
                self._handle_api_error(response.status_code, response.text)

        except requests.exceptions.Timeout:
            logger.error("Request timeout occurred")
            raise WeatherApiException("Request timeout. Please try again later.")
        except requests.exceptions.ConnectionError:
            logger.error("Connection error occurred")
            raise WeatherApiException(
                "Unable to connect to the weather service. Please check your internet connection."
            )
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error occurred: {e}")
            raise WeatherApiException(f"Network error: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            raise WeatherApiException(f"Unexpected error: {str(e)}")

    def _validate_city_name(self, city: str) -> None:
        """Validate the city name format.

        Args:
            city: The city name to validate

        Raises:
            WeatherApiException: If the city name is invalid
        """
        if not city or not city.strip():
            raise WeatherApiException("City name cannot be empty.")

        city = city.strip()

        if len(city) > 100:  # Reasonable limit for city names
            raise WeatherApiException("City name is too long.")

        if not self.CITY_NAME_PATTERN.match(city):
            raise WeatherApiException("City name contains invalid characters.")

    def _build_api_url(self, city: str) -> str:
        """Build the API URL for the weather request.

        Args:
            city: The city name

        Returns:
            The complete API URL
        """
        encoded_city = urllib.parse.quote(city.strip())
        return (
            f"{self.base_url}/weather"
            f"?q={encoded_city}"
            f"&appid={self.api_key}"
            f"&units=metric"
        )

    def _redact_api_key(self, url: str) -> str:
        """Redact the API key from a URL for safe logging.

        Args:
            url: The URL containing the API key

        Returns:
            The URL with the API key redacted
        """
        return url.replace(self.api_key, "REDACTED")

    def _parse_weather_response(self, response_data: Dict[str, Any]) -> WeatherData:
        """Parse the weather API response into a WeatherData object.

        Args:
            response_data: The JSON response from the API

        Returns:
            WeatherData object containing the parsed weather information

        Raises:
            WeatherApiException: If the response format is invalid
        """
        try:
            city = response_data["name"]
            temperature = float(response_data["main"]["temp"])
            description = response_data["weather"][0]["description"]

            logger.debug(f"Successfully parsed weather data for {city}")

            return WeatherData(
                city=city,
                temperature_celsius=temperature,
                description=description.title(),
            )

        except KeyError as e:
            logger.error(f"Missing required field in API response: {e}")
            raise WeatherApiException(f"Invalid API response format: missing field {e}")
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid data type in API response: {e}")
            raise WeatherApiException(f"Invalid API response format: {e}")
        except Exception as e:
            logger.error(f"Error parsing API response: {e}")
            raise WeatherApiException(f"Error parsing weather data: {e}")

    def _handle_api_error(self, status_code: int, response_text: str) -> NoReturn:
        """Handle API error responses.

        Args:
            status_code: The HTTP status code
            response_text: The response body text

        Raises:
            WeatherApiException: With an appropriate error message
        """
        logger.error(
            f"API error - Status code: {status_code}, Response: {response_text}"
        )

        if status_code == 401:
            raise WeatherApiException(
                "Invalid API key. Please check your API key configuration."
            )
        elif status_code == 404:
            raise WeatherApiException(
                "City not found. Please check the city name and try again."
            )
        elif status_code == 429:
            raise WeatherApiException("Rate limit exceeded. Please try again later.")
        elif 500 <= status_code < 600:
            raise WeatherApiException(
                f"Weather service is temporarily unavailable. HTTP status: {status_code}"
            )
        else:
            raise WeatherApiException(
                f"API error: Received HTTP status code {status_code}"
            )
