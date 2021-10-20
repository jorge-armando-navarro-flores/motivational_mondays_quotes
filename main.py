import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day_of_week = now.weekday()
from_email = "[from email]"
from_password = "[from password]"
to_email = "[to email]"

if day_of_week == 0:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
    day_quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject:Happy week!\n\n{day_quote}"
        )



