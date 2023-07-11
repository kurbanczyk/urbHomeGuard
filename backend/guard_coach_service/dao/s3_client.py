import boto3

class S3Client:
    def __init__(self) -> None:
        self.client = boto3.client(
            's3',
            aws_access_key_id='minio',
            aws_secret_access_key='minio123'
        )
    
    def upload_file(self) -> bool:
        bucket_name = 'your-bucket-name'  # Replace with your bucket name
        file_name = 'path/to/your/file.txt'  # Replace with the path to your local file
        self.client.upload_file(
            file_name,
            bucket_name,
            'file.txt'
        )  # Replace 'file.txt' with the desired S3 key/name for the file

        return True # TODO: error handling
