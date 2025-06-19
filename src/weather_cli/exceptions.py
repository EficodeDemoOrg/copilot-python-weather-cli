"""Custom exceptions for the weather CLI application."""

from typing import Optional


class WeatherApiException(Exception):
    """Base exception for API-related errors."""

    def __init__(self, message: str, status_code: Optional[int] = None) -> None:
        """Initialize the WeatherApiException.

        Args:
            message: The error message
            status_code: Optional HTTP status code
        """
        super().__init__(message)
        self.status_code = status_code


class ConfigException(Exception):
    """Exception for configuration-related errors."""

    def __init__(self, message: str) -> None:
        """Initialize the ConfigException.

        Args:
            message: The error message
        """
        super().__init__(message)
