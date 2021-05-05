import os
import socket

from lib.params.uploadClientParamsValidation import UploadClientParams


def main():
    host, port, fName, fSource, verb, quiet, h = UploadClientParams.validate()
    if h:
        return printHelp()

    try:
        file = open(fSource + fName, "rb")
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0, os.SEEK_SET)

        # Se inicializa cliente
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sckt.connect((host, port))

        # Se cierra archivo y socket
        file.close()
        sckt.close()
    except OSError:
        print("El archivo a enviar no existe")


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
    print('-H, --host       server IP address')
    print('-p, --port       server port')
    print('-s, --src        source file path')
    print('-n, --name       file name')


if __name__ == "__main__":
    main()
