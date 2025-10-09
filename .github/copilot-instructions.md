# Python Weather CLI - AI Agent Instructions

## Architecture Overview

**3-Layer CLI Application** with strict separation of concerns:
- **Entry Point** (`main.py`): Orchestrates argument parsing → logging setup → error handling → exit codes
- **Service Layer** (`weather_service.py`): Business logic with dependency injection pattern
- **Client Layer** (`weather_client.py`): HTTP API abstraction via `WeatherApiClient` ABC
- **Data Models** (`weather_data.py`): Immutable dataclasses with `__post_init__` validation
- **Configuration** (`config_util.py`): Environment-based config with security-first design

**Critical insight**: The abstract `WeatherApiClient` interface allows swapping API providers without touching service layer. Dependency injection in `WeatherService.__init__(client: Optional[WeatherApiClient])` enables testing with mocks.

## Non-Negotiable Patterns

### 1. Dependency Injection for Testing
**Every service class** must accept optional dependencies for mock injection:
```python
class WeatherService:
    def __init__(self, client: Optional[WeatherApiClient] = None) -> None:
        self.client = client or OpenWeatherMapClient()  # Default real implementation
```
**Why**: Enables unit testing without real API calls. See `test_weather_service.py` for examples.

### 2. Security-First Configuration
**Never** hardcode or log secrets. Configuration pattern from `config_util.py`:
- Load from env vars or `.env` file (`python-dotenv`)
- Support multiple key name variants: `OPENWEATHERMAP_API_KEY`, `OPEN_WEATHER_API_KEY`, etc.
- Redact in logs: `self._redact_api_key(url)` replaces keys with `"REDACTED"`
- Fail fast: Raise `ConfigException` if missing, never use placeholder defaults

### 3. Immutable Data with Validation
**All data models** use `@dataclass(frozen=True)` with validation:
```python
@dataclass(frozen=True)
class WeatherData:
    city: str
    temperature_celsius: float
    description: str
    
    def __post_init__(self) -> None:
        if not isinstance(self.city, str): raise TypeError("city must be a string")
        if not self.city.strip(): raise ValueError("city cannot be empty")
```
**Why**: Immutability prevents bugs. Validation in `__post_init__` catches bad data at construction.

### 4. Strict Type Hints (mypy --strict)
**Every function/method** requires complete type annotations. Config in `pyproject.toml`:
```ini
[tool.mypy]
disallow_untyped_defs = true      # No untyped functions
no_implicit_optional = true        # Explicit Optional[T] required
warn_return_any = true             # No returning Any
```
**Before committing**: Run `mypy src` - must pass with zero errors.

### 5. Exception Hierarchy & Error Handling
Two custom exceptions in `exceptions.py`:
- `ConfigException`: Environment/setup issues (missing API key, invalid config)
- `WeatherApiException`: Runtime API errors (network, 404, 401, timeouts)

**Main.py pattern**: Catch specific exceptions first, log detailed error, print user-friendly message to stderr, return exit code 1.

## Testing Requirements (>90% Coverage)

**Test structure mirrors source**: `test_weather_client.py` tests `weather_client.py`

**Every new feature needs tests for**:
1. Happy path (successful execution)
2. All error paths (network errors, invalid inputs, API errors)
3. Input validation edge cases (empty strings, invalid characters, length limits)
4. Security (API keys never logged)

**Mock external dependencies** to avoid real API calls:
```python
def setup_method(self, method):
    with (
        patch("weather_cli.config_util.ConfigUtil.get_api_key", return_value="test_key"),
        patch("weather_cli.config_util.ConfigUtil.get_api_base_url", return_value="https://api.openweathermap.org/data/2.5"),
    ):
        self.client = OpenWeatherMapClient()

@patch("weather_cli.weather_client.requests.get")
def test_get_weather_success(self, mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"name": "London", "main": {"temp": 15.5}, "weather": [{"description": "partly cloudy"}]}
    mock_get.return_value = mock_response
    
    result = self.client.get_weather_from_api("London")
    assert result.city == "London"
```

**Run tests**: `pytest --cov=weather_cli tests/`

## Code Quality Gate (All Must Pass)

```bash
black src tests          # Format (line length: 100)
flake8 src tests         # Lint (max-line-length = 100)
mypy src                 # Type check (strict mode)
pytest --cov=weather_cli tests/  # Tests + coverage
```

**Line length**: 100 chars max (configured in `pyproject.toml`)
**Import order**: stdlib → third-party → local

## CLI Design Standards

**Error output routing**:
- Success/normal output → `stdout` via `print()`
- Errors → `stderr` via `print(..., file=sys.stderr)`
- Exit codes: 0 = success, 1 = any error

**Logging configuration** (in `main.py`):
```python
log_level = logging.DEBUG if debug else logging.INFO
format="[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
```

**Argument parsing**: Use `argparse` with clear help text. Current args: `city` (positional), `--debug` (flag).

## Adding New Features

**Extending API client** (e.g., forecast endpoint):
1. Add method to `OpenWeatherMapClient` following: validate input → build URL → request → parse response
2. Use `self._validate_city_name()` for inputs, `self._redact_api_key()` for logging
3. Raise `WeatherApiException` for all API errors
4. Handle HTTP codes: 401 (invalid key), 404 (not found), 429 (rate limit), 500+ (server error)

**Adding data models**: Create `@dataclass(frozen=True)` in `weather_data.py` with `__post_init__` validation and `__str__` for display.

**Adding CLI flags**: Extend `parse_arguments()` in `main.py`, then pass to `run_weather_cli()`.

**Adding configuration**: Add to `ConfigUtil` as static methods, load from env vars, raise `ConfigException` if required values missing.

## Project Build & Run

**Virtual environment setup** (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Installation** (editable mode for development):
```bash
pip install -e .                      # Install package in editable mode
pip install -r requirements-dev.txt   # Add dev tools (pytest, black, mypy, flake8)
```

**Why editable install?** `pip install -e .` makes the `weather_cli` module importable without PYTHONPATH manipulation. Changes to source code are immediately reflected without reinstalling.

**Configuration**: Create `.env` file with `OPENWEATHERMAP_API_KEY=your_key_here`

**Run CLI**:
```bash
python -m weather_cli.main "London"           # Module execution
weather "London"                               # If installed via setup.py
python -m weather_cli.main "London" --debug   # With debug logging
```

**Entry point**: Defined in `setup.py` as `weather=weather_cli.main:main` console script.

## Feature Development Context

**Active branch**: `001-visualization-feature-for` is working on terminal-based weather data visualization (see `specs/001-visualization-feature-for/spec.md`). Key requirements:
- `--visualize` flag for ASCII/Unicode chart rendering
- Support for multiple metrics (temperature, humidity, wind speed)
- Multi-city comparison visualizations
- Terminal width detection and responsive rendering

**When implementing specs**: Follow the user story priorities (P1 → P2 → P3) and ensure all acceptance scenarios are testable.
