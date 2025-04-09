import ujson as json
import time

data = {
    "wifi_name": "mynetwork",
    "wifi_password": 12345678
}

with open("config.json", "w") as file:
    json.dump(data, file)
time.sleep(1)

with open("config.json", "r") as file:
    data = json.load(file)
print(data["wifi_name"])
print(data["wifi_password"])