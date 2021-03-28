from getpass import getpass
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
import constants


def __getMasterPassword():
    return getpass(constants.MASTER_PASSWORD_PROMPT).strip()

def __getEncryptionKey():
    return get_random_bytes(constants.KEY_LENGTH_IN_BYTES)

def __getRSAKeys():
    
def __encryptEncryptionKey():
    rsaKey = RSA.generate(2048)

    
def intialize():
    masterPassword = __getMasterPassword()
    encryptionKey = __getEncryptionKey()



