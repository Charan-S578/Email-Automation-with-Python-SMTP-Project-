import smtplib

my_email = "charan2002cse@gmail.com"
password = "bdlhsgjwsgkqstmz"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="charanrs2002@gmail.com",
        msg="Subject:Hello this is Charan\n\nThis is the body of my email."
    )


import smtplib
import datetime as dt
import random

MY_EMAIL = "charan2002cse@gmail.com"
MY_PASSWORD = "pskzvoccytyfbblu"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="charanrs2002@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

# from datetime import datetime
# from smtplib import SMTPConnectError
#
# import pandas
# import random
# import smtplib
#
# MY_EMAIL = "charan2002cse@gmail.com"
# MY_PASSWORD = "pskzvoccytyfbblu"
#
# today = datetime.now()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
#
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[Name]", birthday_person["name"])
#
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )
