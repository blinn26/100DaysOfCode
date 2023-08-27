import smtplib

my_email = "benlinn26@gmail.com"
password = "pjdseenkcqpasfnp"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_address=my_email,
                    to_address="createdbybenlinn@gmail.com", msg="Say Hello")
connection.close()
