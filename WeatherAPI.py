# Import necessary libraries
import requests
import json
import win32com.client

# Get user input for the city
city = input("Enter your city: ")

# Create the API URL using the WeatherAPI service
url = f"https://api.weatherapi.com/v1/current.json?key=e47e489e04ad4c4bbb580527242001&q={city}"

# Make a request to the API and parse the JSON response
r = requests.get(url)
data = json.loads(r.text)

# Extract the current temperature in Celsius from the API response
temperature_c = data["current"]["temp_c"]

# Print the temperature to the console
print(f"The temperature is {temperature_c} degrees Celsius.")

# Use win32com to initialize a text-to-speech engine and speak the temperature
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(f"The temperature is {temperature_c} degrees Celsius.")
