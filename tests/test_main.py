"""Tests for the main application module."""

import sys
import pytest
from unittest.mock import Mock, patch
from io import StringIO

from weather_cli.main import parse_arguments, run_weather_cli, main, setup_logging
from weather_cli.weather_data import WeatherData
from weather_cli.exceptions import WeatherApiException, ConfigException


class TestParseArguments:
    """Test cases for argument parsing."""

    def test_parse_arguments_city_only(self):
        """Test parsing arguments with city name only."""
        with patch.object(sys, "argv", ["weather-cli", "London"]):
            args = parse_arguments()
            assert args.city == "London"
            assert args.debug is False

    def test_parse_arguments_with_debug(self):
        """Test parsing arguments with debug flag."""
        with patch.object(sys, "argv", ["weather-cli", "Paris", "--debug"]):
            args = parse_arguments()
            assert args.city == "Paris"
            assert args.debug is True

    def test_parse_arguments_city_with_spaces(self):
        """Test parsing arguments with city name containing spaces."""
        with patch.object(sys, "argv", ["weather-cli", "New York"]):
            args = parse_arguments()
            assert args.city == "New York"

    def test_parse_arguments_missing_city(self):
        """Test that missing city argument raises SystemExit."""
        with patch.object(sys, "argv", ["weather-cli"]):
            with pytest.raises(SystemExit):
                parse_arguments()


class TestSetupLogging:
    """Test cases for logging setup."""

    @patch("weather_cli.main.logging.basicConfig")
    def test_setup_logging_default(self, mock_basic_config):
        """Test logging setup with default settings."""
        setup_logging()

        mock_basic_config.assert_called_once()
        call_kwargs = mock_basic_config.call_args[1]
        assert call_kwargs["level"] == 20  # logging.INFO

    @patch("weather_cli.main.logging.basicConfig")
    def test_setup_logging_debug(self, mock_basic_config):
        """Test logging setup with debug enabled."""
        setup_logging(debug=True)

        mock_basic_config.assert_called_once()
        call_kwargs = mock_basic_config.call_args[1]
        assert call_kwargs["level"] == 10  # logging.DEBUG


class TestRunWeatherCli:
    """Test cases for the main application logic."""

    @patch("weather_cli.main.WeatherService")
    @patch("weather_cli.main.setup_logging")
    def test_run_weather_cli_success(
        self, mock_setup_logging, mock_weather_service_class
    ):
        """Test successful weather CLI run."""
        # Setup mocks
        mock_service = Mock()
        mock_weather_service_class.return_value = mock_service

        weather_data = WeatherData(
            city="London", temperature_celsius=15.5, description="Partly cloudy"
        )
        mock_service.get_weather.return_value = weather_data

        # Capture stdout
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            result = run_weather_cli("London")

        # Verify result
        assert result == 0
        mock_setup_logging.assert_called_once_with(False)
        mock_service.get_weather.assert_called_once_with("London")

        # Verify output
        output = mock_stdout.getvalue()
        assert "Weather for London:" in output
        assert "15.5°C" in output
        assert "Partly cloudy" in output

    @patch("weather_cli.main.WeatherService")
    @patch("weather_cli.main.setup_logging")
    def test_run_weather_cli_debug(
        self, mock_setup_logging, mock_weather_service_class
    ):
        """Test weather CLI run with debug enabled."""
        mock_service = Mock()
        mock_weather_service_class.return_value = mock_service

        weather_data = WeatherData(
            city="Paris", temperature_celsius=20.0, description="Sunny"
        )
        mock_service.get_weather.return_value = weather_data

        with patch("sys.stdout", new_callable=StringIO):
            result = run_weather_cli("Paris", debug=True)

        assert result == 0
        mock_setup_logging.assert_called_once_with(True)

    @patch("weather_cli.main.WeatherService")
    @patch("weather_cli.main.setup_logging")
    def test_run_weather_cli_config_exception(
        self, mock_setup_logging, mock_weather_service_class
    ):
        """Test handling of configuration exceptions."""
        mock_service = Mock()
        mock_weather_service_class.return_value = mock_service
        mock_service.get_weather.side_effect = ConfigException("API key not found")

        with patch("sys.stderr", new_callable=StringIO) as mock_stderr:
            result = run_weather_cli("London")

        assert result == 1
        error_output = mock_stderr.getvalue()
        assert "Configuration Error: API key not found" in error_output

    @patch("weather_cli.main.WeatherService")
    @patch("weather_cli.main.setup_logging")
    def test_run_weather_cli_weather_api_exception(
        self, mock_setup_logging, mock_weather_service_class
    ):
        """Test handling of weather API exceptions."""
        mock_service = Mock()
        mock_weather_service_class.return_value = mock_service
        mock_service.get_weather.side_effect = WeatherApiException("City not found")

        with patch("sys.stderr", new_callable=StringIO) as mock_stderr:
            result = run_weather_cli("NonExistentCity")

        assert result == 1
        error_output = mock_stderr.getvalue()
        assert "Weather Error: City not found" in error_output

    @patch("weather_cli.main.WeatherService")
    @patch("weather_cli.main.setup_logging")
    def test_run_weather_cli_keyboard_interrupt(
        self, mock_setup_logging, mock_weather_service_class
    ):
        """Test handling of keyboard interrupt."""
        mock_service = Mock()
        mock_weather_service_class.return_value = mock_service
        mock_service.get_weather.side_effect = KeyboardInterrupt()

        with patch("sys.stderr", new_callable=StringIO) as mock_stderr:
            result = run_weather_cli("London")

        assert result == 1
        error_output = mock_stderr.getvalue()
        assert "Operation cancelled by user." in error_output

    @patch("weather_cli.main.WeatherService")
    @patch("weather_cli.main.setup_logging")
    def test_run_weather_cli_unexpected_exception(
        self, mock_setup_logging, mock_weather_service_class
    ):
        """Test handling of unexpected exceptions."""
        mock_service = Mock()
        mock_weather_service_class.return_value = mock_service
        mock_service.get_weather.side_effect = RuntimeError("Unexpected error")

        with patch("sys.stderr", new_callable=StringIO) as mock_stderr:
            result = run_weather_cli("London")

        assert result == 1
        error_output = mock_stderr.getvalue()
        assert "Unexpected Error: Unexpected error" in error_output


class TestMain:
    """Test cases for the main entry point."""

    @patch("weather_cli.main.run_weather_cli")
    @patch("weather_cli.main.parse_arguments")
    @patch("sys.exit")
    def test_main_success(self, mock_exit, mock_parse_args, mock_run_cli):
        """Test main function with successful execution."""
        # Setup mocks
        mock_args = Mock()
        mock_args.city = "London"
        mock_args.debug = False
        mock_parse_args.return_value = mock_args
        mock_run_cli.return_value = 0

        # Call main
        main()

        # Verify calls
        mock_parse_args.assert_called_once()
        mock_run_cli.assert_called_once_with("London", False)
        mock_exit.assert_called_once_with(0)

    @patch("weather_cli.main.run_weather_cli")
    @patch("weather_cli.main.parse_arguments")
    @patch("sys.exit")
    def test_main_error(self, mock_exit, mock_parse_args, mock_run_cli):
        """Test main function with error."""
        # Setup mocks
        mock_args = Mock()
        mock_args.city = "NonExistentCity"
        mock_args.debug = True
        mock_parse_args.return_value = mock_args
        mock_run_cli.return_value = 1

        # Call main
        main()

        # Verify calls
        mock_parse_args.assert_called_once()
        mock_run_cli.assert_called_once_with("NonExistentCity", True)
        mock_exit.assert_called_once_with(1)

    @patch("weather_cli.main.run_weather_cli")
    @patch("weather_cli.main.parse_arguments")
    @patch("sys.exit")
    def test_main_with_debug_flag(self, mock_exit, mock_parse_args, mock_run_cli):
        """Test main function with debug flag."""
        # Setup mocks
        mock_args = Mock()
        mock_args.city = "Tokyo"
        mock_args.debug = True
        mock_parse_args.return_value = mock_args
        mock_run_cli.return_value = 0

        # Call main
        main()

        # Verify debug flag is passed
        mock_run_cli.assert_called_once_with("Tokyo", True)


class TestIntegration:
    """Integration tests for the main module."""

    @patch("weather_cli.main.WeatherService")
    def test_full_flow_success(self, mock_weather_service_class):
        """Test full application flow with successful outcome."""
        # Setup mock service
        mock_service = Mock()
        mock_weather_service_class.return_value = mock_service

        weather_data = WeatherData(
            city="Integration Test City",
            temperature_celsius=22.5,
            description="Perfect weather",
        )
        mock_service.get_weather.return_value = weather_data

        # Test the full flow
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            result = run_weather_cli("Integration Test City", debug=False)

        # Verify everything worked
        assert result == 0
        output = mock_stdout.getvalue()
        assert "Weather for Integration Test City:" in output
        assert "22.5°C" in output
        assert "Perfect weather" in output

    @patch("weather_cli.main.WeatherService")
    def test_full_flow_with_logging(self, mock_weather_service_class):
        """Test full application flow with debug logging."""
        # Setup mock service
        mock_service = Mock()
        mock_weather_service_class.return_value = mock_service

        weather_data = WeatherData(
            city="Debug City", temperature_celsius=18.0, description="Debugging weather"
        )
        mock_service.get_weather.return_value = weather_data

        # Test with debug logging
        with patch("sys.stdout", new_callable=StringIO):
            result = run_weather_cli("Debug City", debug=True)

        assert result == 0
