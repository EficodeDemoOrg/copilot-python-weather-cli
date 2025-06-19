"""Configuration utility for the weather CLI application."""

import os
import logging

from dotenv import load_dotenv

from .exceptions import ConfigException

logger = logging.getLogger(__name__)


class ConfigUtil:
    """Utility class for managing application configuration."""

    DEFAULT_API_BASE_URL = "https://api.openweathermap.org/data/2.5"

    @staticmethod
    def get_api_key() -> str:
        """Get the OpenWeatherMap API key from environment variables or .env file.

        Returns:
            The API key from environment variables or .env file

        Raises:
            ConfigException: If the API key is not found or is empty
        """
        # Load .env file if it exists (this won't override existing env vars)
        load_dotenv()

        # Try multiple possible key names
        possible_keys = [
            "OPENWEATHERMAP_API_KEY",
            "OPEN_WEATHER_API_KEY",
            "OPENWEATHER_API_KEY",
        ]

        for key_name in possible_keys:
            api_key = os.getenv(key_name)
            if api_key and api_key.strip():
                logger.debug(f"API key loaded successfully from {key_name}")
                return api_key.strip()

        logger.error("API key not found in environment variables or .env file")
        raise ConfigException(
            "API key not found. Please set one of the following environment variables: "
            + ", ".join(possible_keys)
            + " or add it to a .env file."
        )

    @staticmethod
    def get_api_base_url() -> str:
        """Get the OpenWeatherMap API base URL from environment variables or use default.

        Returns:
            The API base URL, either from environment variables or the default
        """
        # Load .env file if it exists
        load_dotenv()

        api_url = os.getenv("OPENWEATHERMAP_API_URL")

        if api_url and api_url.strip():
            url = api_url.strip()
            logger.debug(f"Using API base URL from environment: {url}")
            return url
        else:
            logger.debug(f"Using default API base URL: {ConfigUtil.DEFAULT_API_BASE_URL}")
            return ConfigUtil.DEFAULT_API_BASE_URL
