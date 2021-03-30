from constants import KEY_LENGTH_IN_BYTES, HASH_SALT, HASH_ITERATIONS
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import b64decode

def getUnlockKey(masterPassword):
    return PBKDF2HMAC(hashes.SHA256(), KEY_LENGTH_IN_BYTES, b64decode(HASH_SALT), HASH_ITERATIONS).derive(masterPassword)