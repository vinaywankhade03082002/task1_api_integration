# simple_weather_fetch.py
import requests
import pandas as pd

# Define API Key and URL
API_KEY = '1afd0db2095366fb2960452a5233f605'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# City Name
city = 'London'

# Construct the full API request URL
url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'

# Fetch the data from the API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Extract data for visualization
    main_data = data['main']
    weather_data = data['weather'][0]
    wind_data = data['wind']

    # Creating a DataFrame for further analysis
    weather_info = {
        'Temperature (°C)': main_data['temp'],
        'Pressure (hPa)': main_data['pressure'],
        'Humidity (%)': main_data['humidity'],
        'Weather': weather_data['description'],
        'Wind Speed (m/s)': wind_data['speed']
    }

    df = pd.DataFrame([weather_info])

    print(df)
else:
    print('Failed to retrieve data:', response.status_code)
