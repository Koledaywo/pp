from json.decoder import JSONDecodeError
import requests


response = requests.get("https://playground.learnqa.ru/api/get_text", params={"name":"User"})
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text)

except JSONDecodeError:
    print("Response in not a json format")
#payload = {"name":"padla"}
#response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
#print(response.text)