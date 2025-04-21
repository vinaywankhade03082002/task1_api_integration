# weather_dashboard.py
import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the Streamlit interface
st.title('Weather Data Visualization Dashboard')

# Add a textbox to input the city name
city = st.text_input('Enter the city name:', 'London')

if city:
    # Define API Key and URL
    API_KEY = '1afd0db2095366fb2960452a5233f605'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

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

        # Show the data in the Streamlit app
        st.write(df)

        # Plot the data
        st.subheader('Weather Data Visualizations')

        fig, ax = plt.subplots(2, 2, figsize=(10, 8))
        sns.set(style="whitegrid")

        # Temperature Plot
        ax[0, 0].barh(['Temperature'], df['Temperature (°C)'], color='tab:blue')
        ax[0, 0].set_title('Temperature (°C)')

        # Humidity Plot
        ax[0, 1].barh(['Humidity'], df['Humidity (%)'], color='tab:green')
        ax[0, 1].set_title('Humidity (%)')

        # Pressure Plot
        ax[1, 0].barh(['Pressure'], df['Pressure (hPa)'], color='tab:orange')
        ax[1, 0].set_title('Pressure (hPa)')

        # Wind Speed Plot
        ax[1, 1].barh(['Wind Speed'], df['Wind Speed (m/s)'], color='tab:red')
        ax[1, 1].set_title('Wind Speed (m/s)')

        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.error('Failed to retrieve data.')
