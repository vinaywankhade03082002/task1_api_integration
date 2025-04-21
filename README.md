# task1_api_integration

Company Name : CodTech IT Solutions Pvt. Ltd.  
Name : Vinay Mahendra Wankhade  
Intern ID : CT12UCB  
Domain : Python Programming  
Duration : 8 Weeks  
Mentor : Neela Santosh

# Description
# Weather Data Visualization and API Integration

This project demonstrates how to fetch weather data from the OpenWeatherMap API, process it, and visualize the data using Python's **Matplotlib**, **Seaborn**, and **Streamlit**. The purpose of this project is to showcase how API data can be used to create interactive visualizations and dashboards that provide meaningful insights about weather patterns.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [API Key Setup](#api-key-setup)
- [Fetching and Processing Data](#fetching-and-processing-data)
- [Visualizing the Data](#visualizing-the-data)
- [Streamlit Dashboard](#streamlit-dashboard)
- [Running the Application](#running-the-application)

## Introduction

In this project, we leverage the OpenWeatherMap API to fetch real-time weather data for a specified city. The data includes essential weather parameters such as temperature, humidity, pressure, and weather description. Once we fetch the data, we process and organize it using **Pandas**, followed by creating visualizations using **Matplotlib** and **Seaborn**. Additionally, we build an interactive dashboard using **Streamlit** for dynamic user input and visualization rendering.

This approach allows us to present weather data in an informative, user-friendly way, while also demonstrating API integration, data processing, and visualization techniques using Python.

## Prerequisites

To successfully run the project, you need the following tools and libraries:

- **Python 3.x** – This project was developed with Python 3.x.
- **Libraries**: The following libraries are required for running the scripts:
  - `requests` – For sending HTTP requests to the OpenWeatherMap API.
  - `matplotlib` – For plotting static visualizations like bar plots and line charts.
  - `seaborn` – A Python data visualization library based on matplotlib, used for creating more aesthetically pleasing and complex visualizations.
  - `pandas` – For processing and organizing the weather data into a DataFrame, making it easier to manipulate and visualize.
  - `streamlit` – For building a web-based dashboard to display the data and visualizations interactively.

Install these libraries using the following command:

pip install requests matplotlib seaborn pandas streamlit

## Setup and Installation

1. **Clone this repository** to your local machine:

git clone https://github.com/your-username/weatherapp.git

2. **Navigate to the project directory**:

cd weatherapp

## API Key Setup

To interact with the OpenWeatherMap API, you need to sign up at [OpenWeatherMap](https://openweathermap.org/) and get your **API Key**. Once you have your API key, replace the placeholder `"YOUR_API_KEY"` in the scripts with your actual API key.

## Fetching and Processing Data

The weather data is fetched through a simple HTTP GET request to the OpenWeatherMap API. The script sends a request using the city name and the API key and retrieves the weather data in JSON format. 

In the Python script, we process this JSON data to extract key weather parameters such as:

- **Temperature (°C)**
- **Humidity (%)**
- **Pressure (hPa)**
- **Weather Description** (e.g., Clear, Rainy, etc.)

We use **Pandas** to organize this data into a structured format, making it easy to manipulate and visualize later.

## Visualizing the Data

Using **Matplotlib** and **Seaborn**, we create visualizations to display the weather data effectively. The visualizations include:

- **Bar plots for Temperature and Humidity**: These plots show the current temperature and humidity for the selected city. We use Seaborn's `barplot` function to display the data in an aesthetically pleasing manner.
- **Line charts (optional)**: You can extend the project to include time series data by fetching weather data for multiple days and visualizing trends.

The use of Seaborn allows us to enhance the appearance of the plots with minimal code, providing insights that are easy to interpret.

## Streamlit Dashboard

To make the application interactive, we use **Streamlit**. Streamlit is a Python library that allows us to build web applications for data science projects with minimal effort.

In this project, the Streamlit dashboard includes:

- **City input field**: The user can enter the name of any city.
- **Fetch Weather Button**: When clicked, the app fetches weather data for the entered city from the OpenWeatherMap API.
- **Display of weather data and visualizations**: The dashboard dynamically displays the weather data in a table and generates visualizations (such as bar plots) to illustrate the temperature and humidity for the specified city.

## Running the Application

After completing the setup, you can run the script or the Streamlit dashboard:

### Running the Script:

To run the script that fetches data and visualizes it locally, execute:

python fetch_weather_data.py

### Running the Streamlit App:

To start the interactive web dashboard, use Streamlit by running:

streamlit run weather_dashboard.py

This will open the Streamlit app in your default browser, where you can input a city and visualize the weather data.

# OUTPUT
