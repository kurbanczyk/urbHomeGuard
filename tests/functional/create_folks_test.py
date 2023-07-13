import sys
sys.path.append('./../tests')

import requests

from tests.utils.common import generate_random_string

BASE_APP_URL = 'http://localhost:5000/'

def test_create_new_folk():
    new_folk_name: str = generate_random_string(10)

    with open('tests/functional/test_file.txt', 'rb') as f:
        data = {
            'file': (f, 'tests/functional/test_file.txt')
        }

        response = requests.post(
            f'{BASE_APP_URL}/coach/folks/{new_folk_name}',
            data=data
        )

    assert response.status_code == 200
    assert response.data == b'File uploaded successfully'