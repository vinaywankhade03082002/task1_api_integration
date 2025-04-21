# fetch_weather_data.py
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

    # Set the style for Seaborn
    sns.set(style="whitegrid")

    # Prepare data for plotting
    temperature = df['Temperature (°C)']
    humidity = df['Humidity (%)']
    pressure = df['Pressure (hPa)']
    wind_speed = df['Wind Speed (m/s)']

    # Plotting the data
    fig, ax = plt.subplots(2, 2, figsize=(10, 8))

    # Plot Temperature
    ax[0, 0].barh(['Temperature'], temperature, color='tab:blue')
    ax[0, 0].set_title('Temperature (°C)')

    # Plot Humidity
    ax[0, 1].barh(['Humidity'], humidity, color='tab:green')
    ax[0, 1].set_title('Humidity (%)')

    # Plot Pressure
    ax[1, 0].barh(['Pressure'], pressure, color='tab:orange')
    ax[1, 0].set_title('Pressure (hPa)')

    # Plot Wind Speed
    ax[1, 1].barh(['Wind Speed'], wind_speed, color='tab:red')
    ax[1, 1].set_title('Wind Speed (m/s)')

    # Layout adjustment
    plt.tight_layout()
    plt.show()
else:
    print('Failed to retrieve data:', response.status_code)
