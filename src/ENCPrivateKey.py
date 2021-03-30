from base64 import b64encode, b64decode
import json

DATA_FIELD_NAME = 'data'
IV_FIELD_NAME = 'iv'

def encode(encPrivateKey, iv):
    iv = b64encode(iv).decode('utf-8')
    encodedData = b64encode(encPrivateKey).decode('utf-8')
    return json.dumps({DATA_FIELD_NAME: encodedData, IV_FIELD_NAME: iv })

def decode(encodedData):
    encodedPrivateKey = json.loads(encodedData)
    iv = b64decode(encodedPrivateKey[IV_FIELD_NAME])
    data = b64decode(encodedPrivateKey[DATA_FIELD_NAME])
    return data, iv