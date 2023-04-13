import requests

#response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "valueEe"})
# Для GET запросов params= обязательно фигурные скобки и внутри "key":values
response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "valueEe"})
# Для POST запросов используется data = {"key":value}
print(response.text)
