# Weather App

A simple Python application that fetches and displays current weather information for any location using the WeatherAPI service.

## Features

- Fetch real-time weather data for any city or location
- Display comprehensive weather information including temperature, wind, humidity, and more
- Error handling for invalid inputs and network issues
- Clean, formatted output with location details

## Prerequisites

- Python 3.6 or higher
- `requests` library
- WeatherAPI.com API key (free registration required)

## Installation

1. **Install the required dependency:**
   ```bash
   pip install requests
   ```

2. **Get your API key:**
   - Visit [WeatherAPI.com](https://www.weatherapi.com/)
   - Sign up for a free account
   - Copy your API key from the dashboard

3. **Configure the application:**
   - Open the Python file
   - Replace `"YOUR_API_KEY"` with your actual API key from WeatherAPI.com

## Usage

Run the application:
```bash
python weather_app.py
```

When prompted, enter a location in one of these formats:
- City name: `Cairo`
- City, Country: `Cairo, Egypt`
- City, Country Code: `Cairo, EG` (recommended for accuracy)
- Coordinates: `30.0444,31.2357`

## Sample Output

```
Enter a location (e.g., 'Cairo, Egypt', or 'Cairo, EG' for more accurate results): Cairo, EG
________________________________________
Weather in Cairo - Cairo - Egypt
________________________________________
Celsius Temperature : 28.0 °C
Condition           : Partly cloudy
Wind Speed (kph)    : 15.0 kph
Wind Degree         : 270°
Wind Direction      : W
Pressure            : 1013.0 mb
Humidity            : 65%
Cloud Coverage      : 25%
Heat Index          : 30.2 °C
```

## API Information

This application uses the [WeatherAPI.com](https://www.weatherapi.com/) current weather endpoint:
- **Endpoint:** `https://api.weatherapi.com/v1/current.json`
- **Documentation:** [WeatherAPI Docs](https://www.weatherapi.com/docs/)

## Error Handling

The application handles:
- Invalid location names
- Network connection issues
- API errors (invalid key, rate limits, etc.)

## Code Structure

- `get_weather()`: Handles user input and API requests
- `display_weather_info()`: Formats and displays weather data

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.