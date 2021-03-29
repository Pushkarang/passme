import json
import RSA
import AES
import PBKDF2
import ENCPrivateKey
import constants 
import passmeIO

ENCRYPTION_KEY_FILE_NAME = 'encryptionKey.enc'
PRIVATE_KEY_FILE_NAME = 'privateKey.json'

def initializePassmeKeys(masterPassword):
    unlockKey = PBKDF2.getUnlockKey(masterPassword)
    encryptionKey = AES.generateRandomAESEncryptionKey(constants.KEY_LENGTH_IN_BYTES)
    publicKey, privateKey = RSA.generateRSAKeys()
    writeEncryptionKey(RSA.encrypt(encryptionKey, publicKey))
    writePrivateKey(AES.encrypt(privateKey, unlockKey))

def encrypt(masterPassword, data):
    return AES.encrypt(data, __getEncryptionKey(PBKDF2.getUnlockKey(masterPassword)))

def decrypt(masterPassword, encData):
    return AES.decrypt(encData, __getEncryptionKey(PBKDF2.getUnlockKey(masterPassword)))
    
def __getEncryptionKey(unlockKey):
    privateKey = AES.decrypt(readPrivateKey(), unlockKey)
    encryptionKey = RSA.decrypt(readEncryptionKey(), privateKey)
    return encryptionKey

def writeEncryptionKey(encKey):
    passmeIO.writeFile(ENCRYPTION_KEY_FILE_NAME, encKey)

def writePrivateKey(privateKey):
    passmeIO.writeFile(PRIVATE_KEY_FILE_NAME, privateKey)

def readEncryptionKey():
    return passmeIO.readFile(ENCRYPTION_KEY_FILE_NAME)

def readPrivateKey():
    return passmeIO.readFile(PRIVATE_KEY_FILE_NAME)
