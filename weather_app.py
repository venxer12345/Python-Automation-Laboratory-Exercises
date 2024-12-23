import requests

def get_weather(city):
    """
    Fetches and displays the current weather for a specified city.

    Parameters:
    city (str): The name of the city to fetch the weather for.
    """
    api_key = '4c42991459924c033d9c10a734af572c'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get('cod') == 200:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            print(f'\nWeather in {city.title()}:')
            print(f'  - Condition: {weather.capitalize()}')
            print(f'  - Temperature: {temp}°C')
        else:
            print(f'\nCity "{city}" not found. Please check the spelling or try another city.')
    except requests.exceptions.RequestException as e:
        print(f'\nError fetching weather data: {e}')

# Example usage
if __name__ == '__main__':
    city_name = input("Enter the city name to get weather info: ").strip()

    if city_name:
        get_weather(city_name)
    else:
        print("No city entered. Please try again.")
