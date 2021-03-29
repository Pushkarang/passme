from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import ENCPrivateKey

def generateRandomAESEncryptionKey(keyLength):
    return get_random_bytes(keyLength)

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    return ENCPrivateKey.encode(cipher.encrypt(pad(data, AES.block_size)), cipher.iv)

def decrypt(encData, key):
    data, iv = ENCPrivateKey.decode(encData)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data), AES.block_size)