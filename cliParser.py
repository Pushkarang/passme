import argparse
import constants

def __initParser():
    parser = argparse.ArgumentParser(description = constants.CLI_DESCRIPTION)
    __addInitArgument(parser)
    return parser


def __addInitArgument(parser):
    parser.add_argument('-i', '--init', action = 'store_true', help = constants.INIT_CLI_DESCRIPTION)

def parse(args):
    return __initParser().parse_args(args)


