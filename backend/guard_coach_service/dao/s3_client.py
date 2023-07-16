import boto3
from typing import List

class S3Client:
    def __init__(self) -> None:
        self.client = boto3.client(
            's3',
            aws_access_key_id = 'minio',
            aws_secret_access_key = 'minio123',
            endpoint_url = 'http://s3:9000',
            region_name='us-east-1'
        )
    
    def check_folk_exists(self, bucket_name: str) -> bool:
        try:
            self.client.head_bucket(Bucket = bucket_name)
            return True
        except Exception:
            return False

    def list_existing_folks(self) -> List[str]:
        response = self.client.list_buckets()

        def get_bucket_name(bucket):
            return bucket['Name']

        return list(map(get_bucket_name, response['Buckets']))

    def upload_folk_photo(self, bucket_name: str, image_content) -> bool:
        if not self.check_folk_exists(bucket_name):
            self.client.create_bucket(
                Bucket = bucket_name
            )
        
        self.client.upload_fileobj(
            image_content,
            bucket_name, # folk name acts as bucket name
            image_content.filename
        ) 

        return True # TODO: error handling
