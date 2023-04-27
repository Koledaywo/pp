import requests
import json
from json.decoder import JSONDecodeError
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings, exceptions
disable_warnings(exceptions.InsecureRequestWarning)

basic = HTTPBasicAuth('admin', '123456')
response = requests.get(url='https://10.3.1.69:5010/login', auth=basic, verify=False)
print(response.text)
