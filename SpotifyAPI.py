import requests
import json

response = requests.get('https://api.spotify.com/v1/albums/4aawyAB9vmqN3uQ7FjRGTy')
#response = requests.get('https://api.covid19india.org/state_district_wise.json')
print(response.status_code)
print(response.content)
#data = response.text
#parsed = json.loads(data)

#print(data)


