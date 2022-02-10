import requests
from twilio.rest import Client

account_sid = "AC5b1b978b0486c34cee2843eca5d5bab3"
auth_token = "a90135de2d6352670c407e5e0574535e"

para = {
    "appid": "2121b968590731cfe277b69ff606c2e9",
    "lat": 024.860735,
    "lon": 67.001137,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=para)
response.raise_for_status()
we_data = response.json()
we_slice = we_data["hourly"][:12]

is_raining = False

for hour_data in we_slice:
    data = hour_data["weather"][0]["id"]
    if int(data) < 700:
        is_raining = True

if is_raining:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Kanak luvs shurem",
        from_="+14156492104",
        to="+923403553839"
    )
    print(message.status)
