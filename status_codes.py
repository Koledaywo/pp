import requests

#response = requests.post("https://playground.learnqa.ru/api/get_5000")
#print(response.status_code)
#print(response.text)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# allow_redirects примает true or false
first_response = response.history[0]
# Видимо нужно обязательно указывать [0]
second_response = response

print(first_response.url)
print(second_response.url)