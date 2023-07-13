import json
from flask import jsonify, make_response
from http import HTTPStatus

from guard_coach_service.dao.s3_client import S3Client

class FolksActivities:
    def __init__(self) -> None:
        self.dao = S3Client()

    def create_folks(self, folk_name: str) -> json: # TODO: error handling
        
        return make_response(
            jsonify({
                'message': 'Resource created'
            }),
            HTTPStatus.CREATED,
            {
                'Content-Type': 'application/json'
            }
        )

    def get_folks(self) -> json:
        return make_response(
            [], # TODO: read folks from S3
            HTTPStatus.OK,
            {
                'Content-Type': 'application/json'
            }
        )