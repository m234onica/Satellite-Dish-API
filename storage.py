from config import BUCKET_NAME, ALLOWED_EXTENSIONS
from google.cloud import storage
import base64
import re
import os

def decode_and_get_url(src, id):
  if src == "":
    public_url = None
    return public_url

  result = re.search(
      "data:image/(?P<ext>.*?);base64,(?P<data>.*)", src, re.DOTALL)
  if result:
    ext = result.groupdict().get("ext")
    data = result.groupdict().get("data")

  else:
    raise Exception("Do not parse!")

  if ext in ALLOWED_EXTENSIONS:
    img = base64.urlsafe_b64decode(data)
    filename = "{}.{}".format(id, ext)

    public_url = upload_to_storage(img, filename, "image/"+ext)
    return public_url
  else:
    return "Wrong file type."

def upload_to_storage(file_stream, filename, content_type):
  
  client = storage.Client()
  bucket = client.get_bucket(BUCKET_NAME)
  blob = bucket.blob(filename)

  blob.upload_from_string(
      file_stream,
      content_type=content_type)

  url = blob.public_url

  return url
