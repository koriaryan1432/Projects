import requests
import json
import tkinter as tk

# Enter your OpenWeatherMap API key here
api_key = "d8a99e7f424af1f0b1fa3ac44c59f1f4"

def get_weather(city, country):
    # Construct the URL for the API request
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"

    # Send a GET request to the API and retrieve the JSON response
    response = requests.get(url)
    data = json.loads(response.text)

    # Parse the JSON response and extract the relevant weather data
    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    temp_celsius = round(temp - 273.15, 2)
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    # Return the weather data as a dictionary
    return {
        "city": city,
        "country": country,
        "description": description,
        "temp": temp_celsius,
        "humidity": humidity,
        "wind_speed": wind_speed
    }

def display_weather():
    # Get the user input for city and country
    city = city_entry.get()
    country = country_entry.get()

    # Call the get_weather function to retrieve the weather data
    weather_data = get_weather(city, country)

    # Clear any previous weather data on the output label
    output_label.config(text="")

    # Display the weather data on the output label
    if "error" in weather_data:
        output_label.config(text=weather_data["error"], fg="red")
    else:
        output_text = f"Current weather in {weather_data['city']}, {weather_data['country']}:\n"
        output_text += f"Description: {weather_data['description']}\n"
        output_text += f"Temperature: {weather_data['temp']} °C\n"
        output_text += f"Humidity: {weather_data['humidity']}%\n"
        output_text += f"Wind Speed: {weather_data['wind_speed']} m/s"
        output_label.config(text=output_text)

# Create the GUI window
window = tk.Tk()
window.title("Weather App")

# Create the input labels and entries
city_label = tk.Label(window, text="City:")
city_entry = tk.Entry(window)
country_label = tk.Label(window, text="Country:")
country_entry = tk.Entry(window)

# Create the output label
output_label = tk.Label(window, text="", font=("Arial", 12))

# Create the submit button
submit_button = tk.Button(window, text="Get Weather", command=display_weather)

# Add the input elements to the window using grid layout
city_label.grid(row=0, column=0, padx=10, pady=10)
city_entry.grid(row=0, column=1, padx=10, pady=10)
country_label.grid(row=1, column=0, padx=10, pady=10)
country_entry.grid(row=1, column=1, padx=10, pady=10)
submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
output_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI window
window.mainloop()
