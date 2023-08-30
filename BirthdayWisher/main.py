from datetime import datetime
import pandas as pd
import random
import smtplib
import os

# Configuration
MY_EMAIL = "benlinn26@gmail.com"
MY_PASSWORD = os.environ.get("EMAIL_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # Port for SSL/TLS

# Check today's date
today = datetime.now()
today_tuple = (today.month, today.day)
print(f"Today's date: {today_tuple}")

# Load birthdays data
data = pd.read_csv(
    "/Users/benlinn/Python Course/100DaysOfCode/BirthdayWisher/birthdays.csv")

birthdays_dict = {(row["month"], row["day"]): row for _, row in data.iterrows()}
print("Birthday data loaded.")

# If today's date is in the birthdays dictionary
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    print(f"It's {birthday_person['name']}'s birthday!")

    # Pick a random letter template
    base_directory = "/Users/benlinn/Python Course/100DaysOfCode/BirthdayWisher/"
    file_path = f"{base_directory}letter_templates/letter_{random.randint(1,3)}.txt"

    # Read the template and replace the placeholder with the birthday person's name
    with open(file_path, 'r') as letter_file:
        contents = letter_file.read().replace("[NAME]", birthday_person["name"])
    print(f"Letter for {birthday_person['name']} prepared.")

    # Send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
    print(f"Email sent to {birthday_person['email']}!")
else:
    print("No birthdays today.")
