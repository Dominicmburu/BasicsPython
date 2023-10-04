# import smtplib

my_email = "dommy@gmail.com"
password = "1234"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="shadow@gmail.com", 
#         msg="Subject:Hello\n\nThis is the body of my email.")


## DATETIME
# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# day = now.day
# month = now.month
# day_of_week = now.weekday()

# date_of_birth = dt.datetime(year=2000, month=2, day=21)
# print(date_of_birth)

import smtplib
import datetime as dt
import random
import pandas as pd

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 0:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)

#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email, 
#             to_addrs="shadow@gmail.com", 
#             msg=f"Subject:Monday Motivation\n\n{quote}"
#             )


## NORMAL STARTING PROJECT

#check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_turple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_turple in birthdays_dict:
    birthday_person = birthdays_dict[today_turple]
    file_path = f"letter_{random.randint(1,3).txt}"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday!\n\n{contents}"
            )















