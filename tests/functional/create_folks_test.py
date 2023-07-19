import pytest
import requests

from flask import Response
from tests.utils.common import generate_random_string
from typing import List

BASE_APP_URL = 'http://localhost:5000/'

def test_create_new_folk():
    new_folk_name: str = generate_random_string(10)

    response: Response = requests.post(
        f'{BASE_APP_URL}/coach/folks/{new_folk_name}',
        files = {'file': open('tests/functional/cr7.jpg', 'rb')}
    )

    assert response.status_code == 201
    assert response.json()['message'] == 'Resource created'

@pytest.mark.skip(reason="Skipping this test, because I want to keep data private")
def test_create_real_folks():
    folks: List(str) = ['Sonia', 'Karol', 'Wanda', 'Jagna']

    for name in folks:
        for photo in range (1, 3):
            response: Response = requests.post(
                f'{BASE_APP_URL}/coach/folks/{name}',
                files = {'file': open(f'tests/real/{name}/{photo}.jpg', 'rb')}
            )

            assert response.status_code == 201