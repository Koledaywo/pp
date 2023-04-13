from json.decoder import JSONDecodeError
import requests

#payload = {"name": "User"}
#response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
#print(response.text)

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_responce_text = response.json()
    print(parsed_responce_text)
except JSONDecodeError:
    print("Response is not a Json error")