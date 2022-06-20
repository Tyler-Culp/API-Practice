import requests

response = requests.get("https://api.thedogapi.com/v1/breeds/1")

request = response.request

#print(response.headers.get("Content-Type"))
# print(response.json())
# print(response.json()["name"])

headers = {"X-Request-Id": "<my-request-id>"}
response2 = requests.get("https://example.org", headers=headers)


response3 = requests.get("https://api.lorem.space/image/game?w=150&h=220")
# print(response3.headers.get("Content-Type"))

# file = open("video-game.jpeg", "wb")
# file.write(response3.content)
# file.close()

query_params = {"gender": "female", "nat": "de"}
randomUser = requests.get("https://randomuser.me/api/", params = query_params).json()
# randomUser = requests.get("https://randomuser.me/api/?gender=female&nat=de").json()


#print(randomUser)


endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
Nasa_api_key = "DEMO_KEY"
Nasa_query_params = {"api_key": Nasa_api_key, "earth_date": "2020-07-01"}
Nasa_response = requests.get(endpoint, params=query_params)
print(Nasa_response)