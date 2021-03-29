import sys
from cliParser import parse
from commandsHandler import init, addToVault, getFromVault

commands = parse(sys.argv[1:])

commandHandlerMap = {
    'init': lambda : init(commands['force']),
    'add': lambda : addToVault(commands['key'], commands['password']),
    'get': lambda : getFromVault(commands['key'])
}

commandHandlerMap[commands['subCmd']]()
