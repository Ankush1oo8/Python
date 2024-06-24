import requests as r
from datetime import datetime
import smtplib
import time
my_latitude=17.927910
my_longitude=78.499250

def is_iss_overhead():
    res=r.get(url="http://api.open-notify.org/iss-now.json")

    res.raise_for_status()
    data=res.json()

    longitude=float(data["iss_position"]["longitude"])
    latitude=float(data["iss_position"]["latitude"])


    # your position is within +5 or -5 degree of iss position
    if my_latitude-5<=latitude<=my_latitude+5 and my_longitude-5<=longitude<=my_longitude+5:
        return True


def is_night():
    parameter={
        "lat":latitude,
        "lng":longitude,
        "formatted":0,
    }

    res=r.get(url="https://api.sunrise-sunset.org/json",params=parameter)
    res.raise_for_status() 
    data=res.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now=datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True



while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection=smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        connection.starttls()
        connection.login("ankush@outlook.com","password")
        connection.sendmail(from_addr="ankush@outlook.com",to_addrs="ankushchudiwal@gmail.com",msg="Subject:Look Up \n\n ISS is above you")