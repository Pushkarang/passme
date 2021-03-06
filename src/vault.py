import passmeIO
import json
import os
from passmeEncryption import decrypt, encrypt
from constants import BASE_FILE_PATH, INTI_ALREADY_DONE_ERROR, KEY_NOT_EXISTS, NOT_INITIALIZATION_ERROR

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
    try:
        return vault[key]
    except:
        passmeIO.logErrorAndExit(KEY_NOT_EXISTS)

def checkIfInitialized(force):
    if (os.path.exists(BASE_FILE_PATH + PASSWORD_VAULT_FILE_NAME) and not force):
        passmeIO.logErrorAndExit(INTI_ALREADY_DONE_ERROR)

def verifyInit():
    if not os.path.exists(BASE_FILE_PATH + PASSWORD_VAULT_FILE_NAME):
        passmeIO.logErrorAndExit(NOT_INITIALIZATION_ERROR)

def listVault(masterPassword):
    vault = __decryptVault(masterPassword)
    return vault.keys()

def updateInVault(masterPassword, key, password):
    vault = __decryptVault(masterPassword)
    if key in vault:
        vault[key] = password
        __writeVault(masterPassword, vault)
    else:
        passmeIO.logErrorAndExit(KEY_NOT_EXISTS)

def deleteFromVault(masterPassword, key):
    vault = __decryptVault(masterPassword)
    if key in vault:
        vault.pop(key)
        __writeVault(masterPassword, vault)
    else:
        passmeIO.logErrorAndExit(KEY_NOT_EXISTS)