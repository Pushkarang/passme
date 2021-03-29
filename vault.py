import passmeIO
import json
from passmeEncryption import decrypt, encrypt

PASSWORD_VAULT_FILE_NAME = 'vault.enc'

def __writeVault(masterPassword, data):
    encVault = encrypt(masterPassword, bytes(json.dumps(data), 'utf-8'))
    passmeIO.writeFile(PASSWORD_VAULT_FILE_NAME, encVault)

def __readVault():
    return passmeIO.readFile(PASSWORD_VAULT_FILE_NAME)

def __decryptVault(masterPassword):
    return json.loads(decrypt(masterPassword, __readVault()))

def writeEmptyVault(masterPassword):
    __writeVault(masterPassword, {})

def addToVault(masterPassword, key, pwd):
    vault = __decryptVault(masterPassword)
    vault[key] = pwd
    __writeVault(masterPassword, vault)

def getFromVault(masterPassword, key):
    vault = __decryptVault(masterPassword)
    #  fuzzy search by key
    if vault[key]:
        return vault[key]
    else:
        raise Exception('Key not found')


