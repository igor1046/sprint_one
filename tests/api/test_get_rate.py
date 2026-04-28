import requests
import responses
from pytest_mock import MockerFixture


def get_rate():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    return data["rates"]["JPY"]


fake_response = {"rates": {"JPY": 200.0}}


def test_get_rate_with_patch(mocker: MockerFixture):

    mock_get = mocker.patch("requests.get", autospec=True)
    mock_get.return_value.json.return_value = fake_response

    rate = get_rate()
    assert rate == 200.0


@responses.activate
def test_get_rate_with_responses():
    responses.add(
        method=responses.GET,
        url="https://api.exchangerate-api.com/v4/latest/USD",
        json=fake_response,
        status=200,
    )

    rate = get_rate()
    assert rate == 200.0
