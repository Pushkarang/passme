from constants import KEY_LENGTH_IN_BYTES, HASH_SALT, HASH_ITERATIONS, ENCRYPTION_KEY_FILE_NAME, KEY_LENGTH_IN_BYTES
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from base64 import b64encode, b64decode
from ioHelper import writeFile
import json

def initializePassmecliKeys(masterPassword):
    unlockKey = __getUnlockKey(masterPassword)
    encryptionKey = __getRandomEncryptionKey()
    publicKey, privateKey = __getRSAKeys()
    __encryptEncryptionKey(encryptionKey, publicKey)
    __encryptPrivateKey(privateKey.exportKey(), unlockKey)
    # cleanVariables()


def __getUnlockKey(masterPassword):
    return PBKDF2HMAC(hashes.SHA256(), KEY_LENGTH_IN_BYTES, b64decode(HASH_SALT), HASH_ITERATIONS).derive(masterPassword)

def __getRandomEncryptionKey():
    return get_random_bytes(KEY_LENGTH_IN_BYTES)

def __getRSAKeys():
    rsaKey = RSA.generate(2048)
    return rsaKey.publickey(), rsaKey

def __encryptEncryptionKey(encryptionKey, publicKey):
    writeFile(ENCRYPTION_KEY_FILE_NAME, __rsaEncrypt(encryptionKey, publicKey))

def __rsaEncrypt(data, publicKey):
    return PKCS1_OAEP.new(publicKey).encrypt(data)

def __encryptPrivateKey(privateKey, unlockKey):
    writeFile(PRIVATE_KEY_FILE_NAME, __aesEncrypt(privateKey, unlockKey))

def __aesEncrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    encryptedData = cipher.encrypt(pad(data, KEY_LENGTH_IN_BYTES))
    iv = b64encode(cipher.iv).decode('utf-8')
    encodedData = b64encode(encryptedData).decode('utf-8')
    return json.dumps({data: encodedData, iv: iv, })


initializePassmecliKeys(b'PUSHKARA')
