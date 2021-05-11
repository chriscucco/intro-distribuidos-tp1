from lib.constants import Constants
from lib.fileTransfer.fileTransfer import FileTransfer
from lib.logger.logger import Logger


class ClientDownload:
    def download(self, downloadSocket, fName, fDest, verb, quiet):
        Logger.logIfVerbose(verb, "Sending download code to server")
        downloadSocket.send(Constants.downloadProtocol().encode())

        # "Server ready to download" validation:
        data = downloadSocket.recv(Constants.bytesChunk())
        if data.decode() == 'OK':
            Logger.logIfVerbose(verb, "Server ready to download")
            downloadSocket.send(fName.encode())
            Logger.logIfVerbose(verb, "Sending file name to server")
        elif data.decode() == 'ERROR':
            Logger.log("Server could not resolve the request")
            downloadSocket.close()
            return

        # Filename validation:
        data = downloadSocket.recv(Constants.bytesChunk())
        if data == 'OK':
            Logger.logIfVerbose(verb, "Server found the file")
        elif data.decode() == 'ERROR':
            Logger.log("The file does not exist on the server")
            downloadSocket.close()
            return

        # Size validation:
        try:
            size = downloadSocket.recv(Constants.bytesChunk()).decode()
            int(size)
        except Exception:
            Logger.log("Invalid file size")
            return

        try:
            file = open(fDest + fName, "wb")
        except OSError:
            Logger.log("Client could not create the file on: " + fDest + fName)
        FileTransfer.recieveFile(downloadSocket, file, fName, size,
                                 Constants.bytesChunk(), verb, quiet)
        Logger.log("File downloaded successfully in: " + fDest + fName)

        file.close()
        return
