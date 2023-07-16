import json
from flask import jsonify, make_response, request
from http import HTTPStatus

from guard_coach_service.dao.s3_client import S3Client

class FolksActivities:
    def __init__(self) -> None:
        self.dao = S3Client()

    def create_folks(self, folk_name: str) -> json: # TODO: error handling
        for attached_file in request.files:
            self.dao.upload_folk_photo(folk_name.lower(), request.files[attached_file])

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