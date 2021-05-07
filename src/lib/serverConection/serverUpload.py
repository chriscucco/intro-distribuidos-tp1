from lib.constants import Constants
from lib.fileTransfer.fileTransfer import FileTransfer
from lib.logger.logger import Logger


class ServerUpload:
    def upload(s, sPath, addr, verbose, quiet):
        data = s.recv(Constants.bytesChunk())
        name = data.decode()
        Logger.logIfNotQuiet(quiet, "Client " + str(addr) +
                                    " uploading: " + name)

        try:
            f = open(sPath+name, "wb")
        except Exception:
            Logger.log("Client " + str(addr) + " error opening file" + name)
            Logger.logIfVerbose(verbose, "Sending ERROR code to client")

            s.send("ERROR".encode())
            s.close()
            return

        Logger.logIfVerbose(verbose, "File opened with no problems." +
                            "Sending OK code to client")
        s.send("OK".encode())
        data = s.recv(Constants.bytesChunk())

        try:
            size = int(data.decode())
        except Exception:
            strSize = data.decode()
            Logger.log("Client " + str(addr) + " invalid file size " + strSize)
            Logger.logIfVerbose(verbose, "Sending ERROR code to client.")
            s.send("ERROR".encode())
            s.close()
            return

        Logger.logIfVerbose(verbose, "File with valid size." +
                            "Sending OK code to client")
        s.send("OK".encode())

        Logger.logIfNotQuiet(quiet, "Client " + str(addr) + " file size: " +
                             str(size))
        chunkSize = Constants.bytesChunk()

        Logger.logIfNotQuiet(quiet, "Client " + str(addr) +
                             ", getting file...")
        FileTransfer.recieveFile(s, f, name, size, chunkSize, verbose, quiet)

        Logger.log("Client " + str(addr) + " finished")

        f.close()
        s.close()

        return
