# Python Weather CLI

## Requirements

This project has two sets of requirements:

- **Minimum requirements**: Only what you need to run the app.
- **Optional (development) requirements**: For testing, code formatting, and linting. Recommended if you want to contribute or check code quality.

### Minimum requirements
- Python 3.10 or later
- requests
- python-dotenv

Install with:
```bash
pip install -r requirements.txt
```

### Optional (development) requirements
- pytest: Run tests
- pytest-mock: Mocking for tests
- pytest-cov: Test coverage reporting
- black: Code formatter (auto-formats Python code)
- flake8: Linter (checks code style and errors)
- mypy: Type checker (checks type hints)
- types-requests: Type stubs for requests (for mypy type checking)

Install with:
```bash
pip install -r requirements-dev.txt
```

If you only install the minimum requirements, you can run the app but not run tests, lint, or format code.

## What is this?

A simple Python command-line app that fetches and displays the current weather for any city using the OpenWeatherMap API. You run it from the terminal and get the city name, temperature (Celsius), and weather description.

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd python-weather-cli
```

### 2. Set up your API key

This project uses a `.env` file for the API key. You must set your OpenWeatherMap API key in this file.

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api) and get your API key.
2. Copy the example file and add your key:

```bash
cp .env.example .env
# Edit .env and set your key:
# OPENWEATHERMAP_API_KEY=your_api_key_here
```

### 3. Install dependencies

#### Recommended: Development installation (for full features, testing, linting, formatting)

```bash
pip install -r requirements-dev.txt
```

#### Fallback: Basic installation (only run the app, no tests/linting/formatting)

```bash
pip install -r requirements.txt
```

## Usage

Run the app from the project root:

```bash
python -m weather_cli.main "London"
python -m weather_cli.main "New York"
python -m weather_cli.main "Tokyo"
```

Or use the installed script:

```bash
weather "London"
weather "New York"  
weather "Tokyo"
```

You can use any city name. The app will print the current weather for that city.

## Command-line help

You can see all available options with:

```bash
python -m weather_cli.main --help
```

Or:

```bash
weather --help
```

Example output:

```
usage: weather-cli [-h] [--debug] city

Get current weather information for a city

positional arguments:
  city        Name of the city to get weather for

options:
  -h, --help  show this help message and exit
  --debug     Enable debug logging
```

## Project Structure

```
python-weather-cli/
├── .env.example
├── README.md
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── pyproject.toml
├── src/
│   └── weather_cli/
│       ├── __init__.py
│       ├── main.py
│       ├── weather_service.py
│       ├── weather_client.py
│       ├── weather_data.py
│       ├── config_util.py
│       └── exceptions.py
├── tests/
└── docs/
```

## Development commands (if you did the development install)

- **Run all tests:**
  ```bash
  pytest
  ```
- **Run tests with coverage:**
  ```bash
  pytest --cov=src
  ```
- **Format code with black:**
  ```bash
  black src tests
  ```
- **Lint code with flake8:**
  ```bash
  flake8 src tests
  ```
- **Type check with mypy:**
  ```bash
  mypy src
  ```

## Testing

This project includes comprehensive unit tests covering all major components and functionality. The test suite ensures reliability, security, and proper error handling across the application.

**Quick testing commands:**
- Run all tests: `pytest`
- Run with coverage: `pytest --cov=src`
- Run specific test file: `pytest tests/test_weather_client.py`

The testing approach includes:
- **Unit testing** with mocked dependencies for isolation
- **Error handling** testing for all failure scenarios  
- **Security testing** to ensure API keys aren't exposed
- **Input validation** testing for edge cases and malicious input
- **Integration testing** of component interactions

For detailed information about what is tested and how, see [tests/TESTING.md](tests/TESTING.md).

## Code style

- This project uses [black](https://black.readthedocs.io/) for formatting and [flake8](https://flake8.pycqa.org/) for linting.
- The maximum line length is set to **100 characters** for both tools.
- Target Python version: 3.10+

To check code style:
```bash
flake8 src tests
```
To auto-format code:
```bash
black src tests
```
To type check:
```bash
mypy src
```

---

For more details, see the code and comments in each file.
