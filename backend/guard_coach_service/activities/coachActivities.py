import face_recognition
import json
import os
import pickle
import tempfile

from flask import jsonify, make_response, request
from guard_coach_service.dao.s3_client import S3Client
from http import HTTPStatus
from pathlib import Path

DEFAULT_ENCODINGS_PATH = Path('encodings.pkl')

class CoachActivities:
    def __init__(self) -> None:
        self.dao = S3Client()

    def load_image_from_s3(self, folk_name: str, photo_name: str):
        with tempfile.TemporaryDirectory() as temp_dir:
            local_file_path = os.path.join(temp_dir, os.path.basename(f'{folk_name}/{photo_name}'))
            self.dao.download_folk_photo(folk_name, photo_name, local_file_path)

            image = face_recognition.load_image_file(local_file_path)

        return image

    def train(self, model: str = 'hog') -> json:
        names = []
        encodings = []

        for folk_name in self.dao.list_existing_folks():
            for folk_photo in self.dao.list_folk_photos(folk_name):
                image_data = self.load_image_from_s3(folk_name, folk_photo['Key'])

                face_locations = face_recognition.face_locations(image_data, model=model)
                face_encodings = face_recognition.face_encodings(image_data, face_locations)

                for encoding in face_encodings:
                    names.append(folk_name)
                    encodings.append(encoding)

        name_encodings = {"names": names, "encodings": encodings}
                
        with DEFAULT_ENCODINGS_PATH.open(mode="wb") as f:
            pickle.dump(name_encodings, f)

        return make_response(
            jsonify({
                'message': 'Model accepted. Trainig has been completed!'
            }),
            HTTPStatus.ACCEPTED,
            {
                'Content-Type': 'application/json'
            }
        )