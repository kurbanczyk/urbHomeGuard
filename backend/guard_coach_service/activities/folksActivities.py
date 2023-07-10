import json
from flask import make_response
from http import HTTPStatus

class FolksActivities:
    def get_folks(self) -> json:
        return make_response(
            [],
            HTTPStatus.OK,
            {
                'Content-Type': 'application/json'
            }
        )