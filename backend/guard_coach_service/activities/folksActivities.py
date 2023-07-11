import json
from flask import make_response
from http import HTTPStatus

from guard_coach_service.dao.s3_client import S3Client

class FolksActivities:
    def __init__(self) -> None:
        self.dao = S3Client()

    def create_folks(self) -> HTTPStatus: # TODO: error handling
        
        return HTTPStatus.CREATED

    def get_folks(self) -> json:
        return make_response(
            [], # TODO: read folks from S3
            HTTPStatus.OK,
            {
                'Content-Type': 'application/json'
            }
        )