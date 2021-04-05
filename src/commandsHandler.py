import getpass
from constants import MASTER_PASSWORD_PROMPT
from passmeEncryption import initializePassmeKeys, decrypt
import passmeIO
import vault

def init(force):
    vault.checkIfInitialized(force)
    masterPassword = passmeIO.promptMasterPassword()
    initializePassmeKeys(masterPassword)
    vault.writeEmptyVault(masterPassword)

def __getMasterPassword():
    vault.verifyInit()
    return passmeIO.promptMasterPassword()

def addToVault(key):
    masterPassword = __getMasterPassword()
    password = passmeIO.promptPassword(key)
    vault.addToVault(masterPassword, key, password)

def getFromVault(key):
    masterPassword = __getMasterPassword()
    password = vault.getFromVault(masterPassword, key)
    print(password)

def listVault():
    masterPassword = __getMasterPassword()
    for key in vault.listVault(masterPassword):
        print(key)

def updateInVault(key):
    masterPassword = __getMasterPassword()
    password = passmeIO.promptPassword(key)
    vault.updateInVault(masterPassword, key, password)

def deleteFromVault(key):
    masterPassword = __getMasterPassword()
    vault.deleteFromVault(masterPassword, key)