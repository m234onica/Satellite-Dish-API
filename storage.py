from config import BUCKET_NAME
from google.cloud import storage

def upload_file(file_stream, filename, content_type):
  
  client = storage.Client()
  bucket = client.get_bucket(BUCKET_NAME)
  blob = bucket.blob(filename)

  blob.upload_from_string(
      file_stream,
      content_type=content_type)

  url = blob.public_url

  return url
