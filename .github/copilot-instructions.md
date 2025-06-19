# Codestyle Instructions

## Python Code Style
- Line length: 100 characters
- Target Python version: 3.10+
- Use Black formatting with default settings
- Follow flake8 linting rules

## Type Hints
- Always use type hints for function definitions and class methods
- No implicit optional types
- Check untyped definitions strictly
- Enable all mypy warnings for better code quality

## General Rules
- Maintain strict equality checks
- Remove unused imports and variables
- Use descriptive variable and function names
- Follow PEP 8 conventions

## Common Commands
- Run tests: `pytest`
- Run tests with coverage: `pytest --cov=src`
- Format code: `black src tests`
- Lint code: `flake8 src tests`
- Type check: `mypy src`
- Run application: `python -m weather_cli.main` or `weather`
