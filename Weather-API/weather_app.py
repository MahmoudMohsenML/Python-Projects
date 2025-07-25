import requests

# Your personal API key from weatherapi.com
api_key = "YOUR_API_KEY"

# Base endpoint URL with placeholders for API key and location
base_end_point = "https://api.weatherapi.com/v1/current.json?key={}&q={}"

def get_weather():
    """
    Fetch current weather data for a user-provided location.

    Returns:
        dict: Parsed JSON data containing weather information if the request is successful.
        None: If there is an error during the request or invalid input.
    """
    try:
        location = input("Enter a location (e.g., 'Cairo, Egypt', or 'Cairo, EG' for more accurate results)")
        end_point = base_end_point.format(api_key, location)
        response = requests.get(end_point)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except ValueError as ve:
        print(f"[Input Error] Invalid input: {ve}")
    except requests.exceptions.RequestException as e:
        print(f"[Request Error] Failed to fetch weather data: {e}")
    
    return None

def display_weather_info(json_data):
    """
    Display formatted weather details based on the JSON response.

    Args:
        json_data (dict): The JSON object containing weather information.
    """
    if not json_data:
        print("No weather data to display.")
        return

    print("_" * 40)
    print(f"Weather in {json_data['location']['name']} - {json_data['location']['region']} - {json_data['location']['country']}")
    print("_" * 40)
    print(f"Celsius Temperature : {json_data['current']['temp_c']} °C")
    print(f"Condition           : {json_data['current']['condition']['text']}")
    print(f"Wind Speed (kph)    : {json_data['current']['wind_kph']} kph")
    print(f"Wind Degree         : {json_data['current']['wind_degree']}°")
    print(f"Wind Direction      : {json_data['current']['wind_dir']}")
    print(f"Pressure            : {json_data['current']['pressure_mb']} mb")
    print(f"Humidity            : {json_data['current']['humidity']}%")
    print(f"Cloud Coverage      : {json_data['current']['cloud']}%")
    print(f"Heat Index          : {json_data['current']['heatindex_c']} °C")

if __name__ == "__main__":
    weather_data = get_weather()
    display_weather_info(weather_data)
