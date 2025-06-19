"""Tests for the weather data model."""

import pytest
from weather_cli.weather_data import WeatherData


class TestWeatherData:
    """Test cases for the WeatherData class."""

    def test_create_weather_data_valid(self):
        """Test creating WeatherData with valid inputs."""
        weather = WeatherData(city="London", temperature_celsius=15.5, description="Partly cloudy")

        assert weather.city == "London"
        assert weather.temperature_celsius == 15.5
        assert weather.description == "Partly cloudy"

    def test_create_weather_data_with_integer_temperature(self):
        """Test creating WeatherData with integer temperature."""
        weather = WeatherData(city="Paris", temperature_celsius=20, description="Clear sky")

        assert weather.temperature_celsius == 20
        assert isinstance(weather.temperature_celsius, int)

    def test_weather_data_is_immutable(self):
        """Test that WeatherData objects are immutable."""
        weather = WeatherData(city="Tokyo", temperature_celsius=25.0, description="Sunny")

        with pytest.raises(AttributeError):
            weather.city = "Osaka"

        with pytest.raises(AttributeError):
            weather.temperature_celsius = 30.0

        with pytest.raises(AttributeError):
            weather.description = "Rainy"

    def test_invalid_city_type(self):
        """Test creating WeatherData with invalid city type."""
        with pytest.raises(TypeError, match="city must be a string"):
            WeatherData(city=123, temperature_celsius=15.5, description="Cloudy")

    def test_invalid_temperature_type(self):
        """Test creating WeatherData with invalid temperature type."""
        with pytest.raises(TypeError, match="temperature_celsius must be a number"):
            WeatherData(city="Berlin", temperature_celsius="cold", description="Cloudy")

    def test_invalid_description_type(self):
        """Test creating WeatherData with invalid description type."""
        with pytest.raises(TypeError, match="description must be a string"):
            WeatherData(city="Madrid", temperature_celsius=22.0, description=None)

    def test_empty_city_name(self):
        """Test creating WeatherData with empty city name."""
        with pytest.raises(ValueError, match="city cannot be empty"):
            WeatherData(city="", temperature_celsius=18.0, description="Sunny")

        with pytest.raises(ValueError, match="city cannot be empty"):
            WeatherData(city="   ", temperature_celsius=18.0, description="Sunny")

    def test_empty_description(self):
        """Test creating WeatherData with empty description."""
        with pytest.raises(ValueError, match="description cannot be empty"):
            WeatherData(city="Rome", temperature_celsius=25.0, description="")

        with pytest.raises(ValueError, match="description cannot be empty"):
            WeatherData(city="Rome", temperature_celsius=25.0, description="   ")

    def test_string_representation(self):
        """Test the string representation of WeatherData."""
        weather = WeatherData(city="Amsterdam", temperature_celsius=12.7, description="Light rain")

        expected = "Weather for Amsterdam:\n" "Temperature: 12.7°C\n" "Conditions: Light rain"

        assert str(weather) == expected

    def test_string_representation_integer_temperature(self):
        """Test string representation with integer temperature."""
        weather = WeatherData(city="Vienna", temperature_celsius=20, description="Clear")

        expected = "Weather for Vienna:\n" "Temperature: 20.0°C\n" "Conditions: Clear"

        assert str(weather) == expected

    def test_equality(self):
        """Test equality comparison of WeatherData objects."""
        weather1 = WeatherData(city="Stockholm", temperature_celsius=8.5, description="Overcast")

        weather2 = WeatherData(city="Stockholm", temperature_celsius=8.5, description="Overcast")

        weather3 = WeatherData(city="Stockholm", temperature_celsius=10.0, description="Overcast")

        assert weather1 == weather2
        assert weather1 != weather3

    def test_hash(self):
        """Test that WeatherData objects are hashable."""
        weather = WeatherData(city="Helsinki", temperature_celsius=5.0, description="Snow")

        # Should not raise an exception
        hash(weather)

        # Can be used in sets
        weather_set = {weather}
        assert len(weather_set) == 1
