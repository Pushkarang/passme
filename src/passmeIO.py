from constants import BASE_FILE_PATH, MASTER_PASSWORD_PROMPT, PASSWORD_PROMPT
import os
import getpass

def writeFile(path, data):
    __createBaseDir()
    openedFile = open(BASE_FILE_PATH + path, 'w')
    openedFile.write(data)
    openedFile.close()

def __createBaseDir():
    if not os.path.exists(BASE_FILE_PATH):
        os.makedirs(BASE_FILE_PATH)

def readFile(path):
    return open(BASE_FILE_PATH + path, 'r').read()

def promptMasterPassword():
    return bytes(getpass.getpass(MASTER_PASSWORD_PROMPT), 'utf-8')

def promptPassword(key):
    return getpass.getpass(PASSWORD_PROMPT + 'for ' + key)

def logErrorAndExit(message):
    print(message); os._exit(-1)