import getpass
from constants import MASTER_PASSWORD_PROMPT
from passmeEncryption import initializePassmeKeys, decrypt
import passmeIO
import vault

def init():
    masterPassword = passmeIO.promptMasterPassword()
    print('Generating keys please wait ...')
    initializePassmeKeys(masterPassword)
    vault.writeEmptyVault(masterPassword)
    print('Done!.')

def addToVault(key, password):
    masterPassword = passmeIO.promptMasterPassword()
    # verification TBD
    print('Adding %s into vault...' %key)
    vault.addToVault(masterPassword, key, password)
    print('Added %s successfully!.' %key)

def getFromVault(key):
    masterPassword = passmeIO.promptMasterPassword()
    # verification TBD
    password = vault.getFromVault(masterPassword, key)
    print(password)
