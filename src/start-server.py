from lib.params.serverParamsValidation import ServerParams
from lib.serverConection.serverConection import ServerConection
from threading import Thread
import socket


def main():
    host, port, sPath, verbose, quiet, helpParam = ServerParams.validate()
    if helpParam:
        return printHelp()
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server socket successfully created")
    try:
        serverSocket.bind((host, port))
        print("Socket binded to host:" + host + " and port:" + str(port))
    except socket.error:
        print("Error binding socket. Host: " + host + ", port: " + str(port))
        return
    serverSocket.listen(10)
    print("Server socket listening conections")
    while True:
        c, addr = serverSocket.accept()
        print('Client connected from ', addr)
        t = Thread(target=new_connection, args=(c, sPath, verbose, quiet))
        t.start()
    serverSocket.close()


def new_connection(c, sPath, verbose, quiet):
    ServerConection.new_client_connected(c, sPath, verbose, quiet)


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
