from lib.constants import Constants
from lib.fileTransfer.fileTransfer import FileTransfer
from lib.logger.logger import Logger


class ServerDownload:
    def download(s, sPath, addr, verbose, quiet):
        data = s.recv(Constants.bytesChunk())
        fileName = data.decode()
        Logger.logIfVerbose(verbose, "Client "+addr+" downloading: "+fileName)
        try:
            f = open(sPath+fileName, "rb")
        except Exception:
            Logger.log("Client "+str(addr)+" error opening file"+fileName)
            s.send("ERROR".encode())
            s.close()
            return
        Logger.logIfVerbose(verbose, "Client "+addr+" file opened.")
        s.send("OK".encode())
        FileTransfer.sendFileSize(s, f, verbose, quiet)
        Logger.logIfVerbose(verbose, "Client "+addr+" sending file...")
        FileTransfer.sendFile(s, f, Constants.bytesChunk(), verbose, quiet)
        Logger.log("Client "+str(addr)+" finished")
        f.close()
        s.close()
        return
