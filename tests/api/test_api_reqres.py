import pytest
import requests
import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("API_USER")
password = os.getenv("API_PASS")

BASE_URL = "https://reqres.in/api"

HEADERS = {
    "x-api-key": "free_user_3ConRNAr2WgFtDRdJn1fnhP6EPo"
}

class Color(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str

@pytest.fixture(scope='function')
def colors():
    response = requests.get(f"{BASE_URL}/unknown", headers = HEADERS)
    data = response.json()["data"]
    colors = [Color(**item) for item in data]
    yield colors

def test_colors_years(colors):
    assert all(color.year >= 2000 for color in colors)
    
def test_colors_names(colors):
    assert all(color.name and color.name.strip() for color in colors)

def test_page_2():
    response = requests.get(f"{BASE_URL}/users?page=2 ", headers = HEADERS)
    data = response.json()["data"]
    assert len(data) == 6

def test_login_normal():
    payload = {
        "email" : username,
        "password" : password
    }
    response = requests.post(
        f"{BASE_URL}/login",
        json = payload,
        headers = HEADERS
    )
    data = response.json()
    
    assert response.status_code == 200
    assert 'token' in data


def test_login_without_password():
    payload = {
        "email": username
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json = payload,
        headers = HEADERS
    )

    data = response.json()
    assert response.status_code == 400
    assert 'error' in data

