import argparse
import constants

def __initParser():
    parser = argparse.ArgumentParser(prog=constants.CLI_NAME, description=constants.CLI_DESCRIPTION)
    subParser = __getSubParser(parser)

    __addInitArgument(subParser)
    __addAddArgument(subParser)
    __addGetArgument(subParser)
    __addListArgument(subParser)
    __addUpdateArgument(subParser)
    __addDeleteArgument(subParser)
    return parser


def __addInitArgument(subParser):
    initParser = subParser.add_parser('init', help=constants.INIT_CLI_DESCRIPTION)
    initParser.add_argument('-f', '--force', action='store_true', help=constants.FORCE_CLI_DESCRIPTION)

def __getSubParser(parser):
    return parser.add_subparsers(required=True, dest='action')

def __addAddArgument(subParser):
    appendParser = subParser.add_parser('add', help=constants.ADD_CLI_DESCRIPTION)
    appendParser.add_argument('-k', '--key', required=True , help=constants.KEY_CLI_DESCRIPTION)

def __addGetArgument(subParser):
    appendParser = subParser.add_parser('get', help=constants.GET_CLI_DESCRIPTION)
    appendParser.add_argument('-k', '--key', required=True , help=constants.KEY_CLI_DESCRIPTION)

def __addListArgument(subParser):
    listParser = subParser.add_parser('list', help=constants.LIST_CLI_DESCRIPTION)

def __addUpdateArgument(subParser):
    updateParser = subParser.add_parser('update', help=constants.UPDATE_CLI_DESCRIPTION)
    updateParser.add_argument('-k', '--key', required=True , help=constants.KEY_CLI_DESCRIPTION)

def __addDeleteArgument(subParser):
    deleteParser = subParser.add_parser('delete', help=constants.DELETE_CLI_DESCRIPTION)
    deleteParser.add_argument('-k', '--key', required=True , help=constants.KEY_CLI_DESCRIPTION)

def parse(args):
    return vars(__initParser().parse_args(args))