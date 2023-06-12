import json
import requests
from config import BASE_URL, USER_EMAIL, USER_PASSWORD, USER_ID, JobList
from requests import Response


def test_success_register_user():
    request_json = {
        "email": USER_EMAIL,
        "password": USER_PASSWORD
    }
    send_reg_req: Response = requests.post(BASE_URL + 'register', json=request_json)
    assert send_reg_req.status_code == 200
    assert send_reg_req.json()['token'] is not None


def test_unsuccess_register_user():
    request_json = {
        "email": USER_EMAIL
    }
    send_reg_req: Response = requests.post(BASE_URL + 'register', json=request_json)
    assert send_reg_req.status_code == 400
    assert send_reg_req.json()['error'] == 'Missing password'


def test_unsuccess_login():
    request_json = {
        "email": USER_EMAIL,
    }
    send_reg_req: Response = requests.post(BASE_URL + 'login', json=request_json)
    assert send_reg_req.status_code == 400
    assert send_reg_req.json()['error'] == 'Missing password'


def test_assign_user_on_job():
    request_json = {
        "name": USER_EMAIL,
        "job": json.dumps(JobList.manager)
    }
    send_reg_req: Response = requests.post(BASE_URL + 'user', json=request_json)
    assert send_reg_req.status_code == 201
    assert send_reg_req.json()['job'] == json.dumps(JobList.manager)


def test_get_user_list():
    send_reg_req: Response = requests.get(BASE_URL + 'user', params={'page': 2})
    data = json.loads(send_reg_req.content)
    data_length = len(data['data'])
    assert send_reg_req.status_code == 200
    assert send_reg_req.json()['per_page'] == data_length


def test_get_user_by_id():
    send_reg_req: Response = requests.get(BASE_URL + 'user/' + str(USER_ID))
    assert send_reg_req.status_code == 200
    assert send_reg_req.json()['data']['id'] == USER_ID


def test_delete_user_by_id():
    send_reg_req: Response = requests.delete(BASE_URL + 'user/' + str(USER_ID))
    assert send_reg_req.status_code == 204
    assert send_reg_req.text is ''


def test_success_logout():
    send_reg_req: Response = requests.delete(BASE_URL + 'logout')
    assert send_reg_req.status_code == 204
    assert send_reg_req.text is ''


def test_resource_not_found():
    send_reg_req: Response = requests.get(BASE_URL + 'unknown/23')
    assert send_reg_req.status_code == 404
    assert send_reg_req.text == '{}'


def test_get_single_resource():
    send_reg_req: Response = requests.get(BASE_URL + 'unknown/2')
    assert send_reg_req.status_code == 200
    assert send_reg_req.json()['data']['year'] == 2001
