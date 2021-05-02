from lib.params.uploadClientParamsValidation import UploadClientParams


def main():
    host, port, fName, fSource, verb, quiet, h = UploadClientParams.validate()
    if h:
        return printHelp()


def printHelp():
    print('usage: file-upload [-h] [-v|-q] [-H ADDR] [-p PORT]')
    print('[-s FILEPATH] [-n FILENAME]')
    print('')
    print('<command description>')
    print('')
    print('optional arguments:')
    print('-h, --help       show this help message and exit')
    print('-v, --verbose    increase output verbosity')
    print('-q, --quiet      decrease output verbosity')
    print('-H, --host       service IP address')
    print('-p, --port       service port')
    print('-s, --src        source file path')
    print('-n, --name       file name')


if __name__ == "__main__":
    main()
