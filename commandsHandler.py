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

def addToVault(key, password):
    masterPassword = passmeIO.promptMasterPassword()
    vault.addToVault(masterPassword, key, password)

def getFromVault(key):
    masterPassword = passmeIO.promptMasterPassword()
    password = vault.getFromVault(masterPassword, key)
    print(password)

def listVault():
    masterPassword = passmeIO.promptMasterPassword()
    for key in vault.listVault(masterPassword):
        print(key)

def updateInVault(key, password):
    masterPassword = passmeIO.promptMasterPassword()
    vault.updateInVault(masterPassword, key, password)