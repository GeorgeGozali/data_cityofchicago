import requests as r

url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?year=2022"

response = r.get(url)
data = response.json()
