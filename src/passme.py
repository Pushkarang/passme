import sys
import os
from cliParser import parse
from commandsHandler import init, addToVault, getFromVault, listVault, updateInVault, deleteFromVault

commands = parse(sys.argv[1:])

commandHandlerMap = {
    'init': lambda : init(commands['force']),
    'add': lambda : addToVault(commands['key']),
    'get': lambda : getFromVault(commands['key']),
    'list': lambda: listVault(),
    'update': lambda: updateInVault(commands['key']),
    'delete': lambda: deleteFromVault(commands['key'])
}
commandHandlerMap[commands['action']]()
