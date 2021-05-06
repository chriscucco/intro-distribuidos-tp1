from lib.params.downloadClientParamsValidation import DownloadClientParams
from lib.constants import Constants
from lib.fileTransfer.fileTransfer import FileTransfer
from lib.logger.logger import Logger
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
    downloadSocket.send("download".encode())

    # "Server ready to download" validation:
    data = downloadSocket.recv(Constants.bytesChunk())
    if data.decode() == 'OK':
        Logger.logIfVerbose(verb, "Server ready to download")
        downloadSocket.send(fName.encode())
    elif data.decode() == 'ERROR':
        Logger.log("Server could not resolve the request")
        downloadSocket.close()
        return

    # Filename validation:
    data = downloadSocket.recv(Constants.bytesChunk())
    if data.decode() == 'OK':
        Logger.logIfVerbose(verb, "Server found the file")
    elif data.decode() == 'ERROR':
        Logger.log("The file does not exist on the server")
        downloadSocket.close()
        return

    size = downloadSocket.recv(Constants.bytesChunk()).decode()
    try:
        f = open(fDest + fName, "wb")
    except Exception:
        Logger.log("Client could not create the file on: " + fDest + fName)
        downloadSocket.close()
        return
    FileTransfer.recieveFile(downloadSocket, f, fName, size,
                             Constants.bytesChunk(), verb, quiet)
    Logger.log("File downloaded successfully in: " + fDest + fName)
    f.close()
    downloadSocket.close()
    return


def printHelp():
    print('usage: file-download [-h] [-v | -q] [-H ADDR] [-p PORT]')
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
