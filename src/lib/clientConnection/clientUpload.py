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

    def upload(self, sckt, fSource, fName, verbose, quiet):
        sckt.send(Constants.uploadProtocol().encode())
        data = sckt.recv(Constants.bytesChunk())
        confirmation = data.decode()

        if (confirmation != Constants.okProtocol()):
            Logger.log("Server cant process upload work")
            return

        try:
            file = open(fSource + fName, "rb")
        except OSError:
            Logger.log("Error opening file " + fSource + fName)
            return

        sckt.send(fName.encode())
        data = sckt.recv(Constants.bytesChunk())
        confirmation = data.decode()

        validation = self.__validateConfirmation(file, confirmation,
                                                 "Server cant work with file: "
                                                 + fName)

        if (validation is False):
            return

        FileTransfer.sendFileSize(sckt, file, verbose, quiet)
        data = sckt.recv(Constants.bytesChunk())
        confirmation = data.decode()

        validation = self.__validateConfirmation(file, confirmation,
                                                 "Server cant process file" +
                                                 " size")

        if (validation is False):
            return

        FileTransfer.sendFile(sckt, file, Constants.bytesChunk(),
                              verbose, quiet)

        data = sckt.recv(Constants.bytesChunk())
        confirmation = data.decode()

        if (confirmation != Constants.okProtocol()):
            Logger.log("Server cant save file.")

        file.close()

        return
