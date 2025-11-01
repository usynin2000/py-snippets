from dotenv import load_dotenv
from minio import Minio
from datetime import timedelta
import os


load_dotenv()

minio_client = Minio(
    os.getenv('MINIO_URL'),
    access_key=os.getenv('MINIO_ACCESS_KEY'),
    secret_key=os.getenv('MINIO_SECRET_KEY'),
    secure=True
)


url = minio_client.presigned_get_object(
    bucket_name=os.getenv('MINIO_BUCKET'),
    object_name='devices.Q1.csv',
    expires=timedelta(days=7)
)

print(url)