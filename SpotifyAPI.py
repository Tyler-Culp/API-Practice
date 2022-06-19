import requests
import json

response = requests.get('https://api.spotify.com/v1')
#response = requests.get('https://api.covid19india.org/state_district_wise.json')
print(response.status_code)
data = response.text
parsed = json.loads(data)

print(data)


