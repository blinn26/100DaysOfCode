import os
import requests
from twilio.rest import Client

def request_current_weather(lat, lng, api_key):
    api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
    payload = {'lat': lat, 'lon': lng, 'appid': api_key}
    response = requests.get(url=api_endpoint, params=payload)
    
    # Debug: Print the server response
    print("Server response:", response.text)
    
    response.raise_for_status()
    data = response.json()
    return data

def send_sms(to_number, from_number, msg):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=msg, from_=from_number, to=to_number)
    print(message.status)

# Read and print environment variables for debugging
MY_LAT = float(os.environ.get('MY_LAT', '0'))
MY_LONG = float(os.environ.get('MY_LONG', '0'))
OWM_API_KEY = os.environ.get('OWM_API_KEY')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
OWN_PHONE_NUMBER = os.environ.get('OWN_PHONE_NUMBER')

print("Debugging Info:")
print("Latitude:", MY_LAT)
print("Longitude:", MY_LONG)
print("OWM API Key:", OWM_API_KEY)

try:
    # Get and print the weather data for debugging
    weather_data = request_current_weather(MY_LAT, MY_LONG, OWM_API_KEY)
    print("Weather data:", weather_data)
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
    response = e.response
    print("Server says:", response.text)

# Uncomment the following lines if you still want to send an SMS
print("Sending SMS regardless of weather.")
send_sms(OWN_PHONE_NUMBER, TWILIO_PHONE_NUMBER, "Test the Phone for Wetness.")

