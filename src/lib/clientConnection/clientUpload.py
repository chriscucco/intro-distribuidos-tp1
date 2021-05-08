from lib.constants import Constants
from lib.fileTransfer.fileTransfer import FileTransfer
from lib.logger.logger import Logger


class ClientUpload:

    def __validateConfirmation(self, file, confirmation, errorMsge):

        if (confirmation != Constants.okProtocol()):
            Logger.log(errorMsge)
            file.close()
            return False

        return True

    def upload(self, sckt, file, fName, verbose, quiet):
        Logger.logIfVerbose(verbose, "Sending upload code to server")
        sckt.send(Constants.uploadProtocol().encode())
        data = sckt.recv(Constants.bytesChunk())
        confirmation = data.decode()

        if (confirmation != Constants.okProtocol()):
            Logger.log("Server cant process upload work")
            return

        Logger.logIfVerbose(verbose, "Sending name of file to server")
        sckt.send(fName.encode())
        data = sckt.recv(Constants.bytesChunk())

        confirmation = data.decode()

        validation = self.__validateConfirmation(file, confirmation,
                                                 "Server cant work with file: "
                                                 + fName)

        if (validation is False):
            return

        Logger.logIfVerbose(verbose, "Sending size of file")
        FileTransfer.sendFileSize(sckt, file, verbose, quiet)
        data = sckt.recv(Constants.bytesChunk())
        confirmation = data.decode()

        validation = self.__validateConfirmation(file, confirmation,
                                                 "Server cant process file" +
                                                 " size")

        if (validation is False):
            return

        Logger.logIfNotQuiet(quiet, "Sending file to server...")
        FileTransfer.sendFile(sckt, file, Constants.bytesChunk())

        data = sckt.recv(Constants.bytesChunk())
        confirmation = data.decode()

        if (confirmation != Constants.okProtocol()):
            Logger.log("Server cant save file.")

        file.close()

        return
