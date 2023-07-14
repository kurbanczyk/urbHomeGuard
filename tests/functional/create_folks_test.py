import sys
sys.path.append('./../tests')

import requests

from tests.utils.common import generate_random_string

BASE_APP_URL = 'http://localhost:5000/'

def test_create_new_folk():
    new_folk_name: str = generate_random_string(10)

    response = requests.post(
        f'{BASE_APP_URL}/coach/folks/{new_folk_name}',
        files = {'file': open('tests/functional/cr7.jpg', 'rb')}
    )

    assert response.status_code == 201
    assert response.json()['message'] == 'Resource created'