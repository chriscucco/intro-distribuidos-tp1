from lib.serverParamsValidation import *

def main():
    host, port, storagePath, verboseParam, quietParam, helpParam = ServerParamValidations.validateParams()
    if helpParam:
        return printHelp()

def printHelp():
    print('usage: start-server [-h] [-v | -q] [-H ADDR] [-p PORT] [-s DIRPATH]')
    print('')
    print('<command description>')
    print('')
    print('optional arguments:')
    print('-h, --help       show this help message and exit')
    print('-v, --verbose    increase output verbosity')
    print('-q, --quiet      decrease output verbosity')
    print('-H, --host       service IP address')
    print('-p, --port       service port')
    print('-s, --storage    storage dir path')

if __name__ == "__main__":
    main()
