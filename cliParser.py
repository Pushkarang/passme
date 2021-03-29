import argparse
import constants

def __initParser():
    parser = argparse.ArgumentParser(prog=constants.CLI_NAME, description=constants.CLI_DESCRIPTION)
    subParser = __getSubParser(parser)

    __addInitArgument(subParser)
    __addADDArgument(subParser)
    __addGETArgument(subParser)
    return parser


def __addInitArgument(subParser):
    initParser = subParser.add_parser('init', help=constants.INIT_CLI_DESCRIPTION)
    initParser.add_argument('-f', '--force', action='store_true', help=constants.FORCE_CLI_DESCRIPTION)

def __getSubParser(parser):
    return parser.add_subparsers(dest='subCmd')

def __addADDArgument(subParser):
    appendParser = subParser.add_parser('add', help=constants.ADD_CLI_DESCRIPTION)
    appendParser.add_argument('-k', '--key', required=True , help=constants.KEY_CLI_DESCRIPTION)
    appendParser.add_argument('-p', '--password', required=True , help=constants.PASSWORD_CLI_DESCRIPTION)

def __addGETArgument(subParser):
    appendParser = subParser.add_parser('get', help=constants.GET_CLI_DESCRIPTION)
    appendParser.add_argument('-k', '--key', required=True , help=constants.KEY_CLI_DESCRIPTION)

def parse(args):
    return vars(__initParser().parse_args(args))

def printHelp():
    print(__initParser().print_help())