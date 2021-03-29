import sys
from cliParser import parse, printHelp
from commandsHandler import init, addToVault, getFromVault

commands = parse(sys.argv[1:])

if commands['init']:
    init()
elif commands['subCmd'] == 'add':
    addToVault(commands['key'], commands['password'])
elif commands['subCmd'] == 'get':
    getFromVault(commands['key'])
else:
    printHelp()
