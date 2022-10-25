import argparse


def process_command_line():
    """Command line processor

    :return: name of file with list of hostnames to check
    """
    cmdparser = argparse.ArgumentParser(prog='reward_summary',
                                        usage='%(prog)s [options] path',
                                        description='Report summary of Ardor/NXT Node rewards for specific wallet.')
    cmdparser.version = "0.1"

    cmdparser.add_argument("-a", "--account",
                           type=str,
                           nargs=1,
                           action="store",
                           dest="account",
                           required=True,
                           help="specifies file with list of nodes to check")

    cmdparser.add_argument("-v", "--version", action="version")

    args = cmdparser.parse_args()

    return args.account[0]
