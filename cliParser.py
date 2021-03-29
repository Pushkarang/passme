import argparse
import constants

def __initParser():
    parser = argparse.ArgumentParser(prog=constants.CLI_NAME, description=constants.CLI_DESCRIPTION)
    subParser = __getSubParser(parser)

    __addInitArgument(parser)
    __addADDArgument(subParser)
    __addGETArgument(subParser)
    return parser


def __addInitArgument(parser):
    parser.add_argument('-i', '--init', action='store_true', help=constants.INIT_CLI_DESCRIPTION)

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

