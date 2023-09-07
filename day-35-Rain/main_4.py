import requests
from twilio.rest import Client

# Hardcoded API credentials
api_key = "3dd8fedbe0327e8771ffc596a39c13a8"
account_sid = "ACaba12f624ddd79ec22dffd96a7cfaa36"
auth_token = "a7b3830627a8e05250000ccd356a422d"

# Initialize the OpenWeatherMap endpoint and parameters
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": "33.556660",
    "lon": "-117.723503",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# Request weather data from OpenWeatherMap
try:
    response = requests.get(OWM_Endpoint, params=weather_params)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    print(f"Response Text: {response.text}")
    exit()

# Process the received weather data
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False

# Check if it will rain in the next 12 hours
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# If it will rain, send an SMS via Twilio
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="18336372772",  # Replace with your own number
        to="19492924144"  # Replace with your own number
    )
    print(message.status)



