```json
                          
{
   "coord": {
      "lon": 7.367,
      "lat": 45.133
   },
   "weather": [
      {
         "id": 501,
         "main": "Rain",
         "description": "moderate rain",
         "icon": "10d"
      }
   ],
   "base": "stations",
   "main": {
      "temp": 284.2,
      "feels_like": 282.93,
      "temp_min": 283.06,
      "temp_max": 286.82,
      "pressure": 1021,
      "humidity": 60,
      "sea_level": 1021,
      "grnd_level": 910
   },
   "visibility": 10000,
   "wind": {
      "speed": 4.09,
      "deg": 121,
      "gust": 3.47
   },
   "rain": {
      "1h": 2.73
   },
   "clouds": {
      "all": 83
   },
   "dt": 1726660758,
   "sys": {
      "type": 1,
      "id": 6736,
      "country": "IT",
      "sunrise": 1726636384,
      "sunset": 1726680975
   },
   "timezone": 7200,
   "id": 3165523,
   "name": "Province of Turin",
   "cod": 200
}                    
````

- coord
    - lon: Longitude of the location
    - lat: Latitude of the location
- weather (array)
    - id: Weather condition id
    - main: Group of weather parameters (Rain, Snow, Clouds etc.)
    - description: Weather condition within the group
    - icon: Weather icon id
- base: Internal parameter
- main
    - temp: Temperature (Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit)
    - feels_like: Temperature accounting for human perception (Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit)
    - pressure: Atmospheric pressure on the sea level, hPa
    - humidity: Humidity, %
    - temp_min: Minimum temperature at the moment (Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit)
    - temp_max: Maximum temperature at the moment (Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit)
    - sea_level: Atmospheric pressure on the sea level, hPa
    - grnd_level: Atmospheric pressure on the ground level, hPa
- visibility: Visibility, meter (max 10 km)
- wind
    - speed: Wind speed (Default: meter/sec, Metric: meter/sec, Imperial: miles/hour)
    - deg: Wind direction, degrees (meteorological)
    - gust: Wind gust (Default: meter/sec, Metric: meter/sec, Imperial: miles/hour)
- clouds
    - all: Cloudiness, %
- rain
    - 1h: Precipitation, mm/h (if available)
- snow
    - 1h: Precipitation, mm/h (if available)
- dt: Time of data calculation, unix, UTC
- sys
    - type: Internal parameter
    - id: Internal parameter
    - message: Internal parameter
    - country: Country code (GB, JP etc.)
    - sunrise: Sunrise time, unix, UTC
    - sunset: Sunset time, unix, UTC
- timezone: Shift in seconds from UTC
- id: City ID
- name: City name
- cod: Internal parameter