"""Tests for the configuration utility."""

import os
import pytest
from unittest.mock import patch
from weather_cli.config_util import ConfigUtil
from weather_cli.exceptions import ConfigException


class TestConfigUtil:
    """Test cases for the ConfigUtil class."""

    def test_get_api_key_from_environment(self):
        """Test getting API key from environment variable."""
        with patch.dict(os.environ, {"OPENWEATHERMAP_API_KEY": "test_api_key_123"}):
            api_key = ConfigUtil.get_api_key()
            assert api_key == "test_api_key_123"

    def test_get_api_key_strips_whitespace(self):
        """Test that API key whitespace is stripped."""
        with patch.dict(os.environ, {"OPENWEATHERMAP_API_KEY": "  test_api_key_456  "}):
            api_key = ConfigUtil.get_api_key()
            assert api_key == "test_api_key_456"

    @patch("weather_cli.config_util.load_dotenv")
    def test_get_api_key_missing_environment_variable(self, mock_load_dotenv):
        """Test getting API key when environment variable is missing."""
        mock_load_dotenv.return_value = None  # Don't load .env file
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ConfigException, match="API key not found"):
                ConfigUtil.get_api_key()

    def test_get_api_key_empty_environment_variable(self):
        """Test getting API key when environment variable is empty."""
        with patch.dict(os.environ, {"OPENWEATHERMAP_API_KEY": ""}):
            with pytest.raises(ConfigException, match="API key not found"):
                ConfigUtil.get_api_key()

    def test_get_api_key_whitespace_only_environment_variable(self):
        """Test getting API key when environment variable contains only whitespace."""
        with patch.dict(os.environ, {"OPENWEATHERMAP_API_KEY": "   "}):
            with pytest.raises(ConfigException, match="API key not found"):
                ConfigUtil.get_api_key()

    def test_get_api_base_url_from_environment(self):
        """Test getting API base URL from environment variable."""
        test_url = "https://api.example.com/weather"
        with patch.dict(os.environ, {"OPENWEATHERMAP_API_URL": test_url}):
            api_url = ConfigUtil.get_api_base_url()
            assert api_url == test_url

    def test_get_api_base_url_strips_whitespace(self):
        """Test that API base URL whitespace is stripped."""
        test_url = "https://api.example.com/weather"
        with patch.dict(os.environ, {"OPENWEATHERMAP_API_URL": f"  {test_url}  "}):
            api_url = ConfigUtil.get_api_base_url()
            assert api_url == test_url

    def test_get_api_base_url_uses_default(self):
        """Test getting API base URL when environment variable is not set."""
        with patch.dict(os.environ, {}, clear=True):
            api_url = ConfigUtil.get_api_base_url()
            assert api_url == ConfigUtil.DEFAULT_API_BASE_URL

    def test_get_api_base_url_empty_environment_variable(self):
        """Test getting API base URL when environment variable is empty."""
        with patch.dict(os.environ, {"OPENWEATHERMAP_API_URL": ""}):
            api_url = ConfigUtil.get_api_base_url()
            assert api_url == ConfigUtil.DEFAULT_API_BASE_URL

    def test_get_api_base_url_whitespace_only_environment_variable(self):
        """Test getting API base URL when environment variable contains only whitespace."""
        with patch.dict(os.environ, {"OPENWEATHERMAP_API_URL": "   "}):
            api_url = ConfigUtil.get_api_base_url()
            assert api_url == ConfigUtil.DEFAULT_API_BASE_URL

    def test_default_api_base_url_constant(self):
        """Test that the default API base URL constant is correct."""
        expected_url = "https://api.openweathermap.org/data/2.5"
        assert ConfigUtil.DEFAULT_API_BASE_URL == expected_url

    @patch.dict(os.environ, {"OPENWEATHERMAP_API_KEY": "test_key"})
    def test_api_key_not_logged(self, caplog):
        """Test that API key is not logged in debug messages."""
        with caplog.at_level("DEBUG"):
            ConfigUtil.get_api_key()

        # Check that the actual API key is not in any log message
        for record in caplog.records:
            assert "test_key" not in record.message

    @patch.dict(os.environ, {"OPENWEATHERMAP_API_URL": "https://test.api.com"})
    def test_custom_url_logged(self, caplog):
        """Test that custom API URL is logged in debug messages."""
        with caplog.at_level("DEBUG"):
            ConfigUtil.get_api_base_url()

        # Check that the URL is mentioned in log messages
        log_messages = [record.message for record in caplog.records]
        assert any("https://test.api.com" in msg for msg in log_messages)

    def test_default_url_logged(self, caplog):
        """Test that default API URL is logged in debug messages."""
        with patch.dict(os.environ, {}, clear=True):
            with caplog.at_level("DEBUG"):
                ConfigUtil.get_api_base_url()

            # Check that the default URL is mentioned in log messages
            log_messages = [record.message for record in caplog.records]
            assert any(ConfigUtil.DEFAULT_API_BASE_URL in msg for msg in log_messages)
