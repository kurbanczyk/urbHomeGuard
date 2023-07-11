import pytest
import requests

BACKEND_SERVICE_NAME = 'Urb Home Guard'

def test_service_healthcheck():
    response_in_json = requests.get('http://localhost:5000/') # TODO: move URL to test config

    healthcheck_response = response_in_json.json()
    service = healthcheck_response['service']

    assert service['name'] == BACKEND_SERVICE_NAME