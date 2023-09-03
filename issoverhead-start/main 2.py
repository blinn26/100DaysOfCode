import requests
from datetime import datetime
import smtplib
import time
import os 

MY_EMAIL = "benlinn26@gmail.com"
MY_PASSWORD = "wkjyqfikcsldqies" 
MY_LAT = 33.556660  # Your latitude
MY_LONG = -117.723500  # Your longitude

def is_iss_overhead():
    print("Checking ISS position...")
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(f"ISS Position Data: {data}")
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        print("ISS is overhead:", True)
        return True
    print("ISS is overhead:", False)
    return False

def is_night():
    print("Checking time...")
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(f"Sunrise-Sunset Data: {data}")

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        print("It is night:", True)
        return True
    print("It is night:", False)
    return False

while True:
    if is_iss_overhead() and is_night():
        try:
            print("Sending email...")
            connection = smtplib.SMTP("smtp.gmail.com", 587)
            connection.starttls()
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )
            print("Email sent!")
        except Exception as e:
            print(f"An error occurred: {e}")
    time.sleep(10)
