import sys
import os
from cliParser import parse, printHelp
from commandsHandler import init, addToVault, getFromVault

commands = parse(sys.argv[1:])

commandHandlerMap = {
    'init': lambda : init(commands['force']),
    'add': lambda : addToVault(commands['key'], commands['password']),
    'get': lambda : getFromVault(commands['key'])
}

if commands['subCmd'] not in commandHandlerMap:
    printHelp(); os._exit(-1)
commandHandlerMap[commands['subCmd']]()
