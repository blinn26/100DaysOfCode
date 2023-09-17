import os
import requests
from datetime import datetime

# Fetch USERNAME and TOKEN from environment variables
USERNAME = os.getenv('PIXELA_USERNAME')
TOKEN = os.getenv('PIXELA_TOKEN')

if not USERNAME or not TOKEN:
    print("Environment variables for USERNAME and TOKEN are not set!")
    exit(1)

# Define a constant for the graph ID
GRAPH1 = "graph1"

# Base endpoint for Pixela
pixela_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH1}"

# Header for authentication
headers = {
    "X-USER-TOKEN": TOKEN
}

# Dates
day1 = datetime(year=2023, month=9, day=15)
day2 = datetime(year=2023, month=9, day=16)

# Data
pixel_data_day1 = {"date": day1.strftime("%Y%m%d"), "quantity": "4"}
pixel_data_day2 = {"date": day2.strftime("%Y%m%d"), "quantity": "5"}

# POST for day1
response1 = requests.post(url=pixela_endpoint, json=pixel_data_day1, headers=headers)
print(f"Response for day1: {response1.text}")

# POST for day2
response2 = requests.post(url=pixela_endpoint, json=pixel_data_day2, headers=headers)
print(f"Response for day2: {response2.text}")

# Today
today = datetime.now()

# PUT for today
update_endpoint = f"{pixela_endpoint}/{today.strftime('%Y%m%d')}"
update_response = requests.put(url=update_endpoint, json={"quantity": "8"}, headers=headers)
print(f"Update response: {update_response.text}")

# GET for today
response = requests.get(url=update_endpoint, headers=headers)
print(f"Response: {response.text}")
