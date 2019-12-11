from config import BUCKET_NAME
from google.cloud import storage
import six



def upload_file(file_stream, filename, content_type):
    
    # filename = _safe_filename(filename)

    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(filename)

    blob.upload_from_string(
        file_stream,
        content_type=content_type)

    url = blob.public_url

    if isinstance(url, six.binary_type):
        url = url.decode('utf-8')

    return url
