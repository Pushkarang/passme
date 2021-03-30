from Crypto.PublicKey import RSA
from base64 import b64encode, b64decode
from Crypto.Cipher import PKCS1_OAEP

def generateRSAKeys():
    rsaKey = RSA.generate(2048)
    return rsaKey.publickey(), rsaKey.exportKey()

def encrypt(data, publicKey):
    return b64encode(PKCS1_OAEP.new(publicKey).encrypt(data)).decode('utf-8')

def decrypt(encData, privateKey):
    return PKCS1_OAEP.new(RSA.import_key(privateKey)).decrypt(b64decode(encData))