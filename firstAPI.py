import requests

response = requests.get("https://api.thedogapi.com/v1/breeds/1")

request = response.request

#print(response.headers.get("Content-Type"))
# print(response.json())
# print(response.json()["name"])

headers = {"X-Request-Id": "<my-request-id>"}
response2 = requests.get("https://example.org", headers=headers)


response3 = requests.get("https://api.lorem.space/image/game?w=150&h=220")
print(response3.headers.get("Content-Type"))

file = open("video-game.jpeg", "wb")
file.write(response3.content)
file.close()