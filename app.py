import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_kry
}
params = {
    "term": "shop",
    "location": "Braunschweig"
}
responce = requests.get(url, headers=headers, params=params)
businesses = responce.json()["businesses"]
for business in businesses:
    print(business["name"])
