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
    return False

  if is_base64_code(data) != False:
    if ext in ALLOWED_EXTENSIONS:
      img = base64.urlsafe_b64decode(data)
      filename = "{}.{}".format(id, ext)

      public_url = upload_to_storage(img, filename, "image/"+ext)
      return public_url
    else:
      return False
  else:
    return False

def upload_to_storage(file_stream, filename, content_type):
  
  client = storage.Client()
  bucket = client.get_bucket(BUCKET_NAME)
  blob = bucket.blob(filename)

  blob.upload_from_string(
      file_stream,
      content_type=content_type)

  url = blob.public_url

  return url


def is_base64_code(s):
    # Check s is Base64.b64encode
    if not isinstance(s, str) or not s:
        return False

    _base64_code = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
                    'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',
                    '2', '3', '4', '5', '6', '7', '8', '9', '+',
                    '/', '=']

    # Check base64 OR codeCheck % 4
    code_fail = [i for i in s if i not in _base64_code]
    if code_fail or len(s) % 4 != 0:
        return False
    return True
