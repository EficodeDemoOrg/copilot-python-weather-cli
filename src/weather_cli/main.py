"""Main entry point for the weather CLI application."""

import argparse
import logging
import sys

from .weather_service import WeatherService
from .exceptions import WeatherApiException, ConfigException


def setup_logging(debug: bool = False) -> None:
    """Set up logging configuration.

    Args:
        debug: Whether to enable debug logging
    """
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments.

    Returns:
        Parsed arguments namespace
    """
    parser = argparse.ArgumentParser(
        description="Get current weather information for a city", prog="weather-cli"
    )

    parser.add_argument("city", help="Name of the city to get weather for")

    parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    return parser.parse_args()


def run_weather_cli(city: str, debug: bool = False) -> int:
    """Run the weather CLI application.

    Args:
        city: The city name to get weather for
        debug: Whether to enable debug logging

    Returns:
        Exit code (0 for success, 1 for error)
    """
    setup_logging(debug)
    logger = logging.getLogger(__name__)

    try:
        logger.debug(f"Starting weather CLI for city: {city}")

        weather_service = WeatherService()
        weather_data = weather_service.get_weather(city)

        print(weather_data)
        logger.debug("Weather data displayed successfully")

        return 0

    except ConfigException as e:
        logger.error(f"Configuration error: {e}")
        print(f"Configuration Error: {e}", file=sys.stderr)
        return 1

    except WeatherApiException as e:
        logger.error(f"Weather API error: {e}")
        print(f"Weather Error: {e}", file=sys.stderr)
        return 1

    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
        print("\nOperation cancelled by user.", file=sys.stderr)
        return 1

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected Error: {e}", file=sys.stderr)
        return 1


def main() -> None:
    """Main entry point for the application."""
    args = parse_arguments()
    exit_code = run_weather_cli(args.city, args.debug)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
