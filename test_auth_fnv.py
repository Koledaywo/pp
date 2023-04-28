import requests
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)


def test_status_code():
    auth = HTTPBasicAuth('admin', '123456')
    response = requests.get(url='https://10.3.1.69:5010/login', auth=auth, verify=False)
    status_code = response.status_code
    assert status_code == 200, "status code is ok"
    assert status_code != 300, f"status code {status_code}"

    data = response.json()
    assert data, "empty response"
    assert data.get("actions"), "actions not found"
    assert data.get("access_token"), "no access_token token in response"
    assert data.get("refresh_token"), "no refresh_token token in response"