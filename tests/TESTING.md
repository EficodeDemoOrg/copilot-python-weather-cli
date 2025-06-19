# Testing Documentation

## Overview

This document describes the testing approach for the Python Weather CLI application. The project uses comprehensive unit testing to ensure reliability, maintainability, and correct behavior across all components.

## Testing Framework and Tools

- **pytest**: Primary testing framework with extensive fixture support
- **pytest-mock**: Provides advanced mocking capabilities
- **pytest-cov**: Test coverage reporting
- **unittest.mock**: Python's built-in mocking library for isolating dependencies

## What is Being Tested

### Core Components

#### 1. Configuration Management (`test_config_util.py`)
- **API Key Handling**: Tests loading API keys from environment variables with proper validation
- **Environment Variable Processing**: Ensures whitespace trimming and empty value handling
- **Default URL Configuration**: Validates fallback to default OpenWeatherMap API URL
- **Security**: Verifies API keys are not logged in debug output
- **Error Handling**: Tests proper exception raising for missing configuration

**Key Test Categories**:
- Environment variable loading and validation
- Whitespace handling and sanitization
- Configuration defaults and fallbacks
- Security (no API key leakage in logs)

#### 2. Main Application Logic (`test_main.py`)
- **Argument Parsing**: Command-line argument validation and processing
- **Logging Setup**: Different logging levels (INFO, DEBUG) configuration
- **Application Flow**: End-to-end execution paths
- **Error Handling**: Comprehensive exception handling for all error types
- **Output Formatting**: Stdout/stderr output verification

**Key Test Categories**:
- CLI argument parsing (city names, debug flags)
- Exception handling (configuration errors, API errors, unexpected errors)
- Application lifecycle (initialization, execution, cleanup)
- User interaction (help messages, error messages)

#### 3. Weather API Client (`test_weather_client.py`)
- **HTTP Requests**: Mocked API interactions with various response scenarios
- **Data Parsing**: JSON response parsing and transformation
- **Error Handling**: Network errors, API errors, timeout handling
- **Input Validation**: City name validation and sanitization
- **URL Building**: Proper API endpoint construction

**Key Test Categories**:
- Successful API responses and data extraction
- HTTP error codes (404, 401, 429, 500)
- Network issues (timeouts, connection errors)
- Input validation (empty cities, invalid characters, length limits)
- Response parsing edge cases

#### 4. Data Models (`test_weather_data.py`)
- **Object Creation**: Valid data object instantiation
- **Data Validation**: Type checking and constraint validation
- **Immutability**: Ensuring data objects cannot be modified after creation
- **Type Safety**: Runtime type checking for all fields

**Key Test Categories**:
- Valid object creation with different data types
- Type validation and error handling
- Immutability enforcement
- Edge cases (boundary values, special characters)

#### 5. Weather Service (`test_weather_service.py`)
- **Service Initialization**: Default and custom client injection
- **Business Logic**: Weather data retrieval orchestration
- **Data Flow**: Integration between service and client layers
- **Input Processing**: City name normalization and validation

**Key Test Categories**:
- Dependency injection patterns
- Service layer orchestration
- Data transformation and validation
- Error propagation

## Testing Strategies

### 1. Unit Testing
Each component is tested in isolation using mocks to eliminate external dependencies:
- **Mocked HTTP requests** prevent actual API calls during testing
- **Environment variable mocking** allows testing different configuration scenarios
- **Dependency injection** enables testing with controlled mock objects

### 2. Behavior-Driven Testing
Tests are written to verify specific behaviors rather than implementation details:
- Tests focus on public interfaces and expected outcomes
- Edge cases and error conditions are explicitly tested
- User-facing functionality is validated through end-to-end scenarios

### 3. Security Testing
- API keys are never exposed in logs or test output
- Input validation prevents injection attacks
- Error messages don't leak sensitive information

### 4. Comprehensive Error Testing
Every error path is tested to ensure graceful failure:
- Network connectivity issues
- Invalid API responses
- Configuration problems
- User input errors

## Test Organization

### File Structure
```
tests/
├── __init__.py
├── test_config_util.py      # Configuration management tests
├── test_main.py             # Main application logic tests
├── test_weather_client.py   # API client tests
├── test_weather_data.py     # Data model tests
└── test_weather_service.py  # Service layer tests
```

### Test Naming Convention
- Test files: `test_<module_name>.py`
- Test classes: `Test<ClassName>`
- Test methods: `test_<specific_behavior>`

## Running Tests

### Basic Test Execution
```bash
# Run all tests
PYTHONPATH=src pytest

# Run with coverage
PYTHONPATH=src pytest --cov=weather_cli tests/

# Run specific test file
PYTHONPATH=src pytest tests/test_weather_client.py

# Run with verbose output
PYTHONPATH=src pytest -v
```

### Test Configuration
Tests are configured in `pyproject.toml`:
- Test discovery patterns
- Strict mode enforcement
- Verbose output by default

## Why This Testing Approach

### 1. **Reliability**: Comprehensive test coverage ensures the application works correctly under various conditions
### 2. **Maintainability**: Well-structured tests make it safe to refactor and add features
### 3. **Documentation**: Tests serve as living documentation of expected behavior
### 4. **Regression Prevention**: Automated tests catch breaking changes early
### 5. **Security**: Testing validates that sensitive data (API keys) is handled securely
### 6. **User Experience**: Error handling tests ensure users receive helpful error messages

## Coverage Goals

The test suite aims for:
- **High code coverage** (>90%) across all modules
- **Complete error path coverage** for all exception scenarios
- **Edge case testing** for boundary conditions
- **Integration testing** of component interactions

This comprehensive testing approach ensures the weather CLI application is robust, secure, and reliable for end users.
