# application programming interface
import requests as r
res=r.get(url="http://api.open-notify.org/iss-now.json")

res.raise_for_status()
data=res.json()

longitude=data["iss_position"]["longitude"]
latitude=data["iss_position"]["latitude"]

iss_position=(longitude,latitude)
print(iss_position)