import smtplib
import os

my_email = "benlinn26@gmail.com"
password = os.environ.get("EMAIL_PASSWORD")

print("Setting up the connection...")

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()

print(f"Logging in as {my_email}...")
connection.login(user=my_email, password=password)

subject = "Hello"
body = "Say Hello"
msg = f"Subject: {subject}\n\n{body}"

print(f"Sending email to createdbybenlinn@gmail.com...")
connection.sendmail(from_addr=my_email,
                    to_addrs="createdbybenlinn@gmail.com", msg=msg)

print("Email sent successfully!")
connection.quit()
