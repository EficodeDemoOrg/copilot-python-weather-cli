# OpenWeatherMap API Documentation

## API Overview

The OpenWeatherMap API provides current weather data for any location worldwide. This application uses the Current Weather Data API endpoint.

## API Endpoint

**Base URL:** `https://api.openweathermap.org/data/2.5`

**Endpoint:** `/weather`

**Method:** GET

## Required Parameters

- `q`: City name (e.g., "London", "New York")
- `appid`: Your API key
- `units`: Units of measurement (use "metric" for Celsius)

## Example Request

```
GET https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY&units=metric
```

## Example Response

```json
{
  "coord": {
    "lon": -0.1257,
    "lat": 51.5085
  },
  "weather": [
    {
      "id": 300,
      "main": "Drizzle",
      "description": "light intensity drizzle",
      "icon": "09d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 280.32,
    "pressure": 1012,
    "humidity": 81,
    "temp_min": 279.15,
    "temp_max": 281.15
  },
  "wind": {
    "speed": 4.1,
    "deg": 80
  },
  "clouds": {
    "all": 90
  },
  "dt": 1485789600,
  "sys": {
    "type": 1,
    "id": 5091,
    "message": 0.0103,
    "country": "GB",
    "sunrise": 1485762037,
    "sunset": 1485794875
  },
  "id": 2643743,
  "name": "London",
  "cod": 200
}
```

## Response Fields Used by Application

- `name`: City name
- `main.temp`: Current temperature in Celsius
- `weather[0].description`: Weather description

## Error Responses

### 401 Unauthorized
```json
{
  "cod": 401,
  "message": "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."
}
```

### 404 Not Found
```json
{
  "cod": "404",
  "message": "city not found"
}
```

### 429 Too Many Requests
```json
{
  "cod": 429,
  "message": "Your account is temporary blocked due to exceeding of requests limitation of your subscription type. Please choose the proper subscription http://openweathermap.org/price"
}
```

## Rate Limits

- Free tier: 60 calls/minute, 1,000 calls/day
- For higher limits, consider upgrading your subscription

## API Key Setup

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Set the `OPENWEATHERMAP_API_KEY` environment variable

## Security Considerations

- Never hardcode API keys in source code
- Use environment variables for configuration
- Implement proper input validation for city names
- Use HTTPS for all API requests
- Handle rate limiting gracefully
