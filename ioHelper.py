from constants import BASE_FILE_PATH

def writeFile(path, data):
    openedFile = open(BASE_FILE_PATH + path, 'w')
    openedFile.write(data)
    openedFile.close()


