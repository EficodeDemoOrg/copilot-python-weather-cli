"""Tests for the weather service."""

import pytest
from unittest.mock import Mock, patch
from weather_cli.weather_service import WeatherService
from weather_cli.weather_client import WeatherApiClient
from weather_cli.weather_data import WeatherData
from weather_cli.exceptions import WeatherApiException


class TestWeatherService:
    """Test cases for the WeatherService class."""

    def test_init_with_default_client(self):
        """Test WeatherService initialization with default client."""
        service = WeatherService()
        assert service.client is not None

    def test_init_with_custom_client(self):
        """Test WeatherService initialization with custom client."""
        mock_client = Mock(spec=WeatherApiClient)
        service = WeatherService(client=mock_client)
        assert service.client is mock_client

    def test_get_weather_valid_city(self):
        """Test successful weather retrieval for a valid city."""
        # Create mock client
        mock_client = Mock(spec=WeatherApiClient)
        expected_weather = WeatherData(
            city="London", temperature_celsius=15.5, description="Partly cloudy"
        )
        mock_client.get_weather_from_api.return_value = expected_weather

        # Create service with mock client
        service = WeatherService(client=mock_client)

        # Test the method
        result = service.get_weather("London")

        # Verify the result
        assert result == expected_weather
        mock_client.get_weather_from_api.assert_called_once_with("London")

    def test_get_weather_strips_whitespace(self):
        """Test that city name whitespace is stripped."""
        mock_client = Mock(spec=WeatherApiClient)
        expected_weather = WeatherData(
            city="Paris", temperature_celsius=20.0, description="Sunny"
        )
        mock_client.get_weather_from_api.return_value = expected_weather

        service = WeatherService(client=mock_client)
        result = service.get_weather("  Paris  ")

        assert result == expected_weather
        mock_client.get_weather_from_api.assert_called_once_with("Paris")

    def test_get_weather_empty_city(self):
        """Test error handling for empty city name."""
        mock_client = Mock(spec=WeatherApiClient)
        service = WeatherService(client=mock_client)

        with pytest.raises(
            WeatherApiException, match="City name cannot be null or empty"
        ):
            service.get_weather("")

        # Client should not be called
        mock_client.get_weather_from_api.assert_not_called()

    def test_get_weather_whitespace_only_city(self):
        """Test error handling for whitespace-only city name."""
        mock_client = Mock(spec=WeatherApiClient)
        service = WeatherService(client=mock_client)

        with pytest.raises(
            WeatherApiException, match="City name cannot be null or empty"
        ):
            service.get_weather("   ")

        # Client should not be called
        mock_client.get_weather_from_api.assert_not_called()

    def test_get_weather_none_city(self):
        """Test error handling for None city name."""
        mock_client = Mock(spec=WeatherApiClient)
        service = WeatherService(client=mock_client)

        with pytest.raises(
            WeatherApiException, match="City name cannot be null or empty"
        ):
            service.get_weather(None)

        # Client should not be called
        mock_client.get_weather_from_api.assert_not_called()

    def test_get_weather_api_exception_propagated(self):
        """Test that WeatherApiException from client is propagated."""
        mock_client = Mock(spec=WeatherApiClient)
        mock_client.get_weather_from_api.side_effect = WeatherApiException(
            "City not found"
        )

        service = WeatherService(client=mock_client)

        with pytest.raises(WeatherApiException, match="City not found"):
            service.get_weather("NonExistentCity")

        mock_client.get_weather_from_api.assert_called_once_with("NonExistentCity")

    def test_get_weather_unexpected_exception_wrapped(self):
        """Test that unexpected exceptions are wrapped in WeatherApiException."""
        mock_client = Mock(spec=WeatherApiClient)
        mock_client.get_weather_from_api.side_effect = ValueError("Unexpected error")

        service = WeatherService(client=mock_client)

        with pytest.raises(
            WeatherApiException, match="Unexpected error: Unexpected error"
        ):
            service.get_weather("TestCity")

        mock_client.get_weather_from_api.assert_called_once_with("TestCity")

    def test_get_weather_logging_success(self, caplog):
        """Test logging for successful weather retrieval."""
        mock_client = Mock(spec=WeatherApiClient)
        expected_weather = WeatherData(
            city="Tokyo", temperature_celsius=25.0, description="Clear"
        )
        mock_client.get_weather_from_api.return_value = expected_weather

        service = WeatherService(client=mock_client)

        with caplog.at_level("INFO"):
            service.get_weather("Tokyo")

        # Check log messages
        log_messages = [record.message for record in caplog.records]
        assert any(
            "Fetching weather data for city: Tokyo" in msg for msg in log_messages
        )
        assert any(
            "Successfully retrieved weather data for Tokyo" in msg
            for msg in log_messages
        )

    def test_get_weather_logging_empty_city(self, caplog):
        """Test logging for empty city name error."""
        mock_client = Mock(spec=WeatherApiClient)
        service = WeatherService(client=mock_client)

        with caplog.at_level("ERROR"):
            with pytest.raises(WeatherApiException):
                service.get_weather("")

        # Check error log message
        log_messages = [record.message for record in caplog.records]
        assert any("Empty city name provided" in msg for msg in log_messages)

    def test_get_weather_logging_api_exception(self, caplog):
        """Test logging for API exceptions."""
        mock_client = Mock(spec=WeatherApiClient)
        mock_client.get_weather_from_api.side_effect = WeatherApiException("API error")

        service = WeatherService(client=mock_client)

        with caplog.at_level("ERROR"):
            with pytest.raises(WeatherApiException):
                service.get_weather("TestCity")

        # Check error log message
        log_messages = [record.message for record in caplog.records]
        assert any(
            "Failed to fetch weather data for city: TestCity" in msg
            for msg in log_messages
        )

    def test_get_weather_logging_unexpected_exception(self, caplog):
        """Test logging for unexpected exceptions."""
        mock_client = Mock(spec=WeatherApiClient)
        mock_client.get_weather_from_api.side_effect = RuntimeError("Runtime error")

        service = WeatherService(client=mock_client)

        with caplog.at_level("ERROR"):
            with pytest.raises(WeatherApiException):
                service.get_weather("TestCity")

        # Check error log message
        log_messages = [record.message for record in caplog.records]
        assert any(
            "Unexpected error while fetching weather data for TestCity" in msg
            for msg in log_messages
        )

    @patch("weather_cli.weather_service.OpenWeatherMapClient")
    def test_default_client_creation(self, mock_client_class):
        """Test that default client is created when none is provided."""
        mock_instance = Mock()
        mock_client_class.return_value = mock_instance

        service = WeatherService()

        assert service.client is mock_instance
        mock_client_class.assert_called_once()

    def test_get_weather_multiple_calls(self):
        """Test multiple calls to get_weather with same service instance."""
        mock_client = Mock(spec=WeatherApiClient)

        weather1 = WeatherData(
            city="City1", temperature_celsius=10.0, description="Cold"
        )
        weather2 = WeatherData(
            city="City2", temperature_celsius=30.0, description="Hot"
        )

        mock_client.get_weather_from_api.side_effect = [weather1, weather2]

        service = WeatherService(client=mock_client)

        result1 = service.get_weather("City1")
        result2 = service.get_weather("City2")

        assert result1 == weather1
        assert result2 == weather2
        assert mock_client.get_weather_from_api.call_count == 2
