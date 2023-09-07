import os
import requests
from twilio.rest import Client

def request_current_weather(lat, lng, api_key):
    api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
    payload = {'lat': lat, 'lon': lng, 'appid': api_key}
    response = requests.get(url=api_endpoint, params=payload)
    response.raise_for_status()
    data = response.json()
    return data

def send_sms(to_number, from_number, msg):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=msg, from_=from_number, to=to_number)
    print(message.status)

# Read environment variables
MY_LAT = float(os.environ.get('MY_LAT', '0'))  # Provide a default value of '0' if not set
MY_LONG = float(os.environ.get('MY_LONG', '0'))
OWM_API_KEY = os.environ.get('OWM_API_KEY')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
OWN_PHONE_NUMBER = os.environ.get('OWN_PHONE_NUMBER')

# Get the weather data
weather_data = request_current_weather(MY_LAT, MY_LONG, OWM_API_KEY)

# Print weather data (for debugging)
print("Weather data:", weather_data)

# Always send SMS and print message
print("Sending SMS regardless of weather.")
send_sms(OWN_PHONE_NUMBER, TWILIO_PHONE_NUMBER, "Test the Phone for Wetness.")
