import smtplib

my_email="ankush@outlook.com"
my_pass="password"

with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_pass)
    connection.sendmail(from_addr=my_email, to_addrs="ankushchudiwal1008@gmail.com",msg="Subject:hello\n\nThis message is sent from python app")


import datetime as dt

birthday=dt.datetime(year=2004,month=3,day=1)