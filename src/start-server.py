from lib.params.serverParamsValidation import ServerParams
from lib.logger.logger import Logger
from lib.serverConection.serverConection import ServerConection
from threading import Thread
import socket

MAX_CONNECTIONS = 10


def main():
    host, port, sPath, verbose, quiet, helpParam = ServerParams.validate()

    if helpParam:
        return printHelp()

    Logger.log("Server started in host: " + host + " and port: " + str(port))

    srvSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Logger.logIfNotQuiet(quiet, "Server socket successfully created")

    try:
        srvSock.bind((host, port))
        Logger.logIfVerbose(verbose, "Server socket binded")
    except socket.error:
        Logger.log("Error binding socket")
        return

    srvSock.listen(MAX_CONNECTIONS)
    Logger.logIfNotQuiet(quiet, "Server socket listening conections")

    t = Thread(target=waitConnections, args=(srvSock, sPath, verbose, quiet))
    t.start()

    serverOn = True
    while serverOn:
        value = input()
        if value == 'exit':
            serverOn = False

    srvSock.close()
    t.join()
    Logger.log('Server closed')


def connect(c, sPath, addr, verbose, quiet):
    ServerConection.new_client_connected(c, sPath, addr, verbose, quiet)


def waitConnections(serverSocket, sPath, verbose, quiet):
    activeThreads = []
    try:
        while True:
            c, addr = serverSocket.accept()
            Logger.log('Client connected from ' + str(addr))
            t = Thread(target=connect, args=(c, sPath, addr, verbose, quiet))
            activeThreads.append(t)
            t.start()
    except Exception:
        Logger.logIfVerbose(verbose, 'Closing server...')
        for pos, thread in enumerate(activeThreads):
            Logger.logIfVerbose(verbose, 'Joining thread #' + str(pos+1))
            thread.join()


def printHelp():
    print('usage: start-server.py [-h] [-v|-q] [-H ADDR] [-p PORT] [-s DIRPATH]')
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
