from lib.constants import Constants
from lib.fileTransfer.fileTransfer import FileTransfer
from lib.logger.logger import Logger


class ServerDownload:
    def download(s, sPath, addr, verbose, quiet):
        data = s.recv(Constants.bytesChunk())
        fileName = data.decode()
        Logger.logIfNotQuiet(quiet, "Client " + str(addr) +
                             " downloading: " + sPath + fileName)

        try:
            f = open(sPath + fileName, "rb")
        except Exception:
            Logger.log("Client " + str(addr) +
                       " error opening file: " + sPath + fileName)
            Logger.logIfVerbose(verbose, "Sending ERROR code to client")

            s.send("ERROR".encode())
            s.close()
            return

        Logger.logIfVerbose(verbose, "Client " + str(addr) + " file opened." +
                            "Sending OK code to client.")
        s.send("OK".encode())

        FileTransfer.sendFileSize(s, f, verbose, quiet)
        Logger.logIfNotQuiet(quiet, "Client " + str(addr) +
                             " sending file...")
        FileTransfer.sendFile(s, f, Constants.bytesChunk())

        Logger.log("Client " + str(addr) + " finished")

        f.close()
        s.close()

        return
