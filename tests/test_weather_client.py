"""Tests for the weather API client."""

import pytest
from unittest.mock import Mock, patch
import requests
from weather_cli.weather_client import OpenWeatherMapClient, WeatherApiClient
from weather_cli.weather_data import WeatherData
from weather_cli.exceptions import WeatherApiException


class TestOpenWeatherMapClient:
    """Test cases for the OpenWeatherMapClient class."""

    def setup_method(self, method):
        """Set up test fixtures."""
        # Create client instance with mocked config using context managers
        with (
            patch(
                "weather_cli.config_util.ConfigUtil.get_api_key",
                return_value="test_api_key",
            ),
            patch(
                "weather_cli.config_util.ConfigUtil.get_api_base_url",
                return_value="https://api.openweathermap.org/data/2.5",
            ),
        ):
            self.client = OpenWeatherMapClient()

    @patch("weather_cli.weather_client.requests.get")
    def test_get_weather_success(self, mock_get):
        """Test successful weather data retrieval."""
        # Mock successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "London",
            "main": {"temp": 15.5},
            "weather": [{"description": "partly cloudy"}],
        }
        mock_get.return_value = mock_response

        # Test the method
        result = self.client.get_weather_from_api("London")

        # Verify the result
        assert isinstance(result, WeatherData)
        assert result.city == "London"
        assert result.temperature_celsius == 15.5
        assert result.description == "Partly Cloudy"

        # Verify API call
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        assert "q=London" in args[0]
        assert "appid=test_api_key" in args[0]
        assert "units=metric" in args[0]
        assert kwargs["timeout"] == 30

    @patch("weather_cli.weather_client.requests.get")
    def test_get_weather_city_not_found(self, mock_get):
        """Test handling of city not found error."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = "city not found"
        mock_get.return_value = mock_response

        with pytest.raises(WeatherApiException, match="City not found"):
            self.client.get_weather_from_api("NonExistentCity")

    @patch("weather_cli.weather_client.requests.get")
    def test_get_weather_invalid_api_key(self, mock_get):
        """Test handling of invalid API key error."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.text = "Invalid API key"
        mock_get.return_value = mock_response

        with pytest.raises(WeatherApiException, match="Invalid API key"):
            self.client.get_weather_from_api("London")

    @patch("weather_cli.weather_client.requests.get")
    def test_get_weather_rate_limit_exceeded(self, mock_get):
        """Test handling of rate limit exceeded error."""
        mock_response = Mock()
        mock_response.status_code = 429
        mock_response.text = "Too many requests"
        mock_get.return_value = mock_response

        with pytest.raises(WeatherApiException, match="Rate limit exceeded"):
            self.client.get_weather_from_api("London")

    @patch("weather_cli.weather_client.requests.get")
    def test_get_weather_server_error(self, mock_get):
        """Test handling of server error."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal server error"
        mock_get.return_value = mock_response

        with pytest.raises(
            WeatherApiException, match="Weather service is temporarily unavailable"
        ):
            self.client.get_weather_from_api("London")

    @patch("weather_cli.weather_client.requests.get")
    def test_get_weather_timeout_error(self, mock_get):
        """Test handling of request timeout."""
        mock_get.side_effect = requests.exceptions.Timeout()

        with pytest.raises(WeatherApiException, match="Request timeout"):
            self.client.get_weather_from_api("London")

    @patch("weather_cli.weather_client.requests.get")
    def test_get_weather_connection_error(self, mock_get):
        """Test handling of connection error."""
        mock_get.side_effect = requests.exceptions.ConnectionError()

        with pytest.raises(WeatherApiException, match="Unable to connect"):
            self.client.get_weather_from_api("London")

    def test_validate_city_name_valid(self):
        """Test validation of valid city names."""
        # These should not raise exceptions
        self.client._validate_city_name("London")
        self.client._validate_city_name("New York")
        self.client._validate_city_name("São Paulo")
        self.client._validate_city_name("St. Petersburg")
        self.client._validate_city_name("Los Angeles-Long Beach")

    def test_validate_city_name_empty(self):
        """Test validation of empty city names."""
        with pytest.raises(WeatherApiException, match="City name cannot be empty"):
            self.client._validate_city_name("")

        with pytest.raises(WeatherApiException, match="City name cannot be empty"):
            self.client._validate_city_name("   ")

        with pytest.raises(WeatherApiException, match="City name cannot be empty"):
            self.client._validate_city_name(None)

    def test_validate_city_name_too_long(self):
        """Test validation of overly long city names."""
        long_city = "a" * 101
        with pytest.raises(WeatherApiException, match="City name is too long"):
            self.client._validate_city_name(long_city)

    def test_validate_city_name_invalid_characters(self):
        """Test validation of city names with invalid characters."""
        with pytest.raises(
            WeatherApiException, match="City name contains invalid characters"
        ):
            self.client._validate_city_name("London<script>")

        with pytest.raises(
            WeatherApiException, match="City name contains invalid characters"
        ):
            self.client._validate_city_name("Paris&Berlin")

    def test_build_api_url(self):
        """Test API URL building."""
        url = self.client._build_api_url("London")

        assert "https://api.openweathermap.org/data/2.5/weather" in url
        assert "q=London" in url
        assert "appid=test_api_key" in url
        assert "units=metric" in url

    def test_build_api_url_with_spaces(self):
        """Test API URL building with city names containing spaces."""
        url = self.client._build_api_url("New York")

        assert "q=New%20York" in url

    def test_redact_api_key(self):
        """Test API key redaction in URLs."""
        url = (
            "https://api.openweathermap.org/data/2.5/weather?"
            "q=London&appid=test_api_key&units=metric"
        )
        redacted = self.client._redact_api_key(url)

        assert "test_api_key" not in redacted
        assert "REDACTED" in redacted
        assert "London" in redacted

    def test_parse_weather_response_valid(self):
        """Test parsing of valid weather response."""
        response_data = {
            "name": "Paris",
            "main": {"temp": 20.0},
            "weather": [{"description": "clear sky"}],
        }

        result = self.client._parse_weather_response(response_data)

        assert result.city == "Paris"
        assert result.temperature_celsius == 20.0
        assert result.description == "Clear Sky"

    def test_parse_weather_response_missing_name(self):
        """Test parsing of response missing city name."""
        response_data = {
            "main": {"temp": 20.0},
            "weather": [{"description": "clear sky"}],
        }

        with pytest.raises(WeatherApiException, match="Invalid API response format"):
            self.client._parse_weather_response(response_data)

    def test_parse_weather_response_missing_temperature(self):
        """Test parsing of response missing temperature."""
        response_data = {"name": "Berlin", "weather": [{"description": "clear sky"}]}

        with pytest.raises(WeatherApiException, match="Invalid API response format"):
            self.client._parse_weather_response(response_data)

    def test_parse_weather_response_missing_weather(self):
        """Test parsing of response missing weather description."""
        response_data = {"name": "Madrid", "main": {"temp": 25.0}}

        with pytest.raises(WeatherApiException, match="Invalid API response format"):
            self.client._parse_weather_response(response_data)

    def test_parse_weather_response_invalid_temperature_type(self):
        """Test parsing of response with invalid temperature type."""
        response_data = {
            "name": "Rome",
            "main": {"temp": "very hot"},
            "weather": [{"description": "sunny"}],
        }

        with pytest.raises(WeatherApiException, match="Invalid API response format"):
            self.client._parse_weather_response(response_data)

    @patch("weather_cli.weather_client.requests.get")
    def test_get_weather_with_special_characters_in_city(self, mock_get):
        """Test weather retrieval with special characters in city name."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "São Paulo",
            "main": {"temp": 28.0},
            "weather": [{"description": "sunny"}],
        }
        mock_get.return_value = mock_response

        result = self.client.get_weather_from_api("São Paulo")

        assert result.city == "São Paulo"
        assert result.temperature_celsius == 28.0
        assert result.description == "Sunny"


class TestWeatherApiClientInterface:
    """Test cases for the WeatherApiClient abstract base class."""

    def test_cannot_instantiate_abstract_class(self):
        """Test that the abstract base class cannot be instantiated."""
        with pytest.raises(TypeError):
            WeatherApiClient()

    def test_concrete_implementation_must_implement_abstract_method(self):
        """Test that concrete implementations must implement the abstract method."""

        class IncompleteClient(WeatherApiClient):
            pass

        with pytest.raises(TypeError):
            IncompleteClient()

    def test_concrete_implementation_works(self):
        """Test that a proper concrete implementation works."""

        class TestClient(WeatherApiClient):
            def get_weather_from_api(self, city: str) -> WeatherData:
                return WeatherData(
                    city=city, temperature_celsius=20.0, description="Test weather"
                )

        client = TestClient()
        result = client.get_weather_from_api("Test City")

        assert result.city == "Test City"
        assert result.temperature_celsius == 20.0
        assert result.description == "Test weather"
