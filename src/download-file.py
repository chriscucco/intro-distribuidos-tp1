from lib.params.downloadClientParamsValidation import DownloadClientParams
from lib.logger.logger import Logger
from lib.clientConnection.clientDownload import ClientDownload
import socket


def main():
    host, port, fName, fDest, verb, quiet, h = DownloadClientParams.validate()
    if h:
        return printHelp()

    downloadSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Logger.logIfVerbose(verb, "Download-client socket successfully created")
    try:
        downloadSocket.connect((host, port))
    except socket.error:
        downloadSocket.close()
        Logger.log("Could not connect to server")
        return

    Logger.log("Client connected with host: " + str(host) + " and port: "
               + str(port))

    clientDownload = ClientDownload()
    clientDownload.download(downloadSocket, fName, fDest, verb, quiet)

    downloadSocket.close()
    Logger.log("Client closed")
    return


def printHelp():
    print('usage: download-file.py [-h] [-v | -q] [-H ADDR] [-p PORT]')
    print('[-d FILEPATH] [-n FILENAME]')
    print('')
    print('<command description>')
    print('')
    print('optional arguments:')
    print('-h, --help       show this help message and exit')
    print('-v, --verbose    increase output verbosity')
    print('-q, --quiet      decrease output verbosity')
    print('-H, --host       service IP address')
    print('-p, --port       service port')
    print('-d, --dst        destination file path')
    print('-n, --name       file name')


if __name__ == "__main__":
    main()
