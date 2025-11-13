import datetime as dt
import smtplib
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_month = now.day
day_of_week = now.weekday()

day_names = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

day_name_now = day_names[day_of_week]

list_of_quotes = []

with open("quotes.txt", "r") as quote_file:
    for quotes in quote_file:
        quotes_for_people = quotes.strip()
        list_of_quotes.append(quotes_for_people)


my_email = "agabarda451@gmail.com"
password = "zjkx unua ivup ejbz"

'''
This app is sending from gmail to yahoo account
'''
daily_quotes = random.choice(list_of_quotes)
#using "with" keyword to close the connection
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()#transport layer security
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="gelo.gabarda@yahoo.com",
        msg=f"Subject:Quote of the Day({day_name_now})\n\n{month}/{day_month}/{year}\n\n{daily_quotes}"
    )










