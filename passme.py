import sys
import os
from cliParser import parse
from commandsHandler import init, addToVault, getFromVault, listVault, updateInVault

commands = parse(sys.argv[1:])

commandHandlerMap = {
    'init': lambda : init(commands['force']),
    'add': lambda : addToVault(commands['key'], commands['password']),
    'get': lambda : getFromVault(commands['key']),
    'list': lambda: listVault(),
    'update': lambda: updateInVault(commands['key'], commands['password'])
}
commandHandlerMap[commands['action']]()
