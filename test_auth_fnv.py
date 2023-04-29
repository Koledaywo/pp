import requests
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)

# tests for login, status code200 and 3 keys in response  "actoins, accers_token, refresh_token"
auth = HTTPBasicAuth("admin", "123456")
def test_status_code():
    response = requests.get(url="https://10.3.1.69:5010/login", auth=auth, verify=False)
    status_code = response.status_code
    assert status_code == 200, "status code is ok"
    assert status_code != 300, f"status code {status_code}" #not 300 status code in response

    data = response.json()

    assert data, "empty response"
    assert data.get("actions"), f"actions not found"
    assert data.get("access_token"), f"no access_token token in response"
    assert data.get("access_token") != "" #not empty access_token
    assert data.get("refresh_token"), f"no refresh_token token in response"
    assert data.get("refresh_token") != "" #not empty refresh_token
    assert data.get("actions") != "[]" # not empty array
    assert data.get("actions") == [
                                    "ACCESS_VMS_LIST_DEL_FNV",
                                    "ACCESS_PERSONS_LIST_DEL_FNV",
                                    "ACCESS_PERSONS_LIST_UPD_FNV",
                                    "ACCESS_EVENTS_ARCH_FNV",
                                    "ACCESSGL_FNV",
                                    "ACCESS_EXTERNAL_TABLES_FNV",
                                    "ACTION_TO_CHANGE_FNV",
                                    "ACCESS_CAMERAS_LIST_DEL_FNV",
                                    "ACCESS_VERIFICATION_FNV",
                                    "ACCESS_LIVE_EVENTS_FNV",
                                    "ACCESS_CAMERAS_LIST_FNV",
                                    "ACCESS_CAMERA_SWITCH_FNV",
                                    "ACCESS_FILE_SEARCH_FNV",
                                    "ACCESS_CAMERAS_LIST_UPD_FNV",
                                    "ACCESS_STATISTICS_FNV",
                                    "ACCESS_VMS_LIST_FNV",
                                    "ACCESS_PERSONS_LIST_FNV",
                                    "ACCESS_VMS_LIST_UPD_FNV"
                                    ]
    # values in response after login

def test_get_action():
    response_get_actions = requests.get(url="https://10.3.1.69:5010/api/get_actions", auth=auth, verify=False)
    status_code = response_get_actions.status_code
    data_get_actions = response_get_actions.json()

    assert status_code == 200, "status code is ok"
    assert data_get_actions.get("status"), "status  is ok"
    assert data_get_actions.get("status") == "OK"
    assert data_get_actions.get("data"), "data is ok"
    assert data_get_actions.get("data") != "[]"
