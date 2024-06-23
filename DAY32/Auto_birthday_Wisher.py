import pandas as p
import smtplib as s
import datetime as dt
import random
my_email="ankushchudiwal@outlook.com"
my_pass="Ankush@2004"
today=dt.datetime.now()
today_tuple=(today.month,today.day)

data = p.read_csv("DAY32/birtdays.csv")

birthday_dict={
    (data_row["month"], data_row["day"]):data_row for (index,data_row) in data.iterrows()
}

if today_tuple in birthday_dict:
    file_path=f"Day32/letter/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents=letter.read()
        contents=contents.replace("[NAME]",birthday_dict[today_tuple]["name"])

with s.SMTP(host='smtp-mail.outlook.com', port=587) as connection:
    connection.starttls()
    connection.login(my_email,my_pass)
    connection.sendmail(from_addr=my_email,
                        to_addrs=birthday_dict[today_tuple]["email"],
                        msg=f"Subject:Happy Birthday!!!\n\n{contents}")