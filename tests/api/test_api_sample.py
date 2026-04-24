import requests
import random
import pytest

@pytest.fixture(scope='module')
def create_id():
    x = random.randint(100,999)
    yield x


def test_post_req(create_id):
    payload = {
    "id": create_id,
    "category": {
        "id": 100,
        "name": "TestCategory"
    },
    "name": "TestName",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
        "id": 100,
        "name": "TestTag"
        }
    ],
    "status": "available"
    }

    response = requests.post('https://petstore.swagger.io/v2/pet', json = payload).json()
    assert response['status'] == payload['status']


def test_get_req(create_id):
    response = requests.get(f'https://petstore.swagger.io/v2/pet/{create_id}')
    jsons = requests.get(f'https://petstore.swagger.io/v2/pet/{create_id}').json()
    print(jsons)
    assert response.status_code == 200

def test_put_req(create_id):
    payload = {
    "id": create_id,
    "category": {
        "id": random.randint(100,999),
        "name": "NEWTestCategory"
    },
    "name": "NEWTestName",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
        "id": random.randint(100,999),
        "name": "NEWTestTag"
        }
    ],
    "status": "available"
    }

    response = requests.put(
        'https://petstore.swagger.io/v2/pet', 
        json = payload
        ).json()
    print(response)
    assert response['id'] == payload['id']

def test_del_req(create_id):
    response = requests.delete(f'https://petstore.swagger.io/v2/pet/{create_id}')
    assert response.status_code == 200
