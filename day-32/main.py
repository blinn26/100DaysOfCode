import smtplib
import datetime as dt
import random
import os

MY_EMAIL = "benlinn26@gmail.com"
# Either retrieve the password from environment variable or hard-code for testing
MY_PASSWORD = os.environ.get("EMAIL_PASSWORD")
# MY_PASSWORD = "your_actual_password_here_for_testing"  # Uncomment for testing, comment it out once done

# Check if today is Monday
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:  # Note: Monday is 0, not 1
    # Retrieve a random quote from the quotes.txt file
    with open("quotes.txt", 'r') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # Setting up the email connection and sending the quote
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,  # Sending to your own email for testing
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
    print("Monday Motivation email sent!")
else:
    print("Today is not Monday, no email sent!")
