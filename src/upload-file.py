from lib.serverParamsValidation import Params
import os


def main():
    host, port, sPath, verbose, quiet, helpParam = Params.validateParams()
    if helpParam:
        return printHelp()

    file = open("prueba.txt", "rb")
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0, os.SEEK_SET)





def printHelp():
    print('usage: start-server [-h] [-v|-q] [-H ADDR] [-p PORT] [-s DIRPATH]')
    print('')
    print('<command description>')
    print('')
    print('optional arguments:')
    print('-h, --help       show this help message and exit')
    print('-v, --verbose    increase output verbosity')
    print('-q, --quiet      decrease output verbosity')
    print('-H, --host       server IP address')
    print('-p, --port       server port')
    print('-s, --src        source file path')
    print('-n, --name       file name')


if __name__ == "__main__":
    main()
