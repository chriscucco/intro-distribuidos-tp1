from lib.params.serverParamsValidation import ServerParams
from lib.logger.logger import Logger
from lib.serverConection.serverConection import ServerConection
from threading import Thread
import socket


def main():
    host, port, sPath, verbose, quiet, helpParam = ServerParams.validate()
    if helpParam:
        return printHelp()
    Logger.log("Server started in host: " + host + "and port: " + str(port))
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Logger.logIfVerbose(verbose, "Server socket successfully created")
    try:
        serverSocket.bind((host, port))
        Logger.logIfVerbose(verbose, "Server socket binded")
    except socket.error:
        Logger.log("Error binding socket")
        return
    serverSocket.listen(10)
    Logger.logIfNotQuiet(quiet, "Server socket listening conections")
    while True:
        c, addr = serverSocket.accept()
        Logger.log('Client connected from ', addr)
        t = Thread(target=connection, args=(c, sPath, addr, verbose, quiet))
        t.start()
    serverSocket.close()


def connection(c, sPath, addr, verbose, quiet):
    ServerConection.new_client_connected(c, sPath, addr, verbose, quiet)


def printHelp():
    print('usage: start-server [-h] [-v|-q] [-H ADDR] [-p PORT] [-s DIRPATH]')
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
