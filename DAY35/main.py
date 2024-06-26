import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

my_lat=17.927910
my_lng=78.499252

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("4292924e11e28269b68a189ac7e5e159")
account_sid = "AC700b49893312cc81c0b92ec364daf0b2"
auth_token = os.environ.get("1536f6411121ca210ec21fefcf729699")

weather_params = {
    "lat": my_lat,
    "lon": my_lng,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+12515729886",
        to="+918010017202"
    )
    print(message.status)
