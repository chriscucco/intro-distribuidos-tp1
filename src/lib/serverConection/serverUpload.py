from lib.constants import Constants
from lib.fileTransfer.fileTransfer import FileTransfer
from lib.logger.logger import Logger


class ServerUpload:
    def upload(s, sPath, addr, verbose, quiet):
        data = s.recv(Constants.bytesChunk())
        name = data.decode()
        Logger.logIfVerbose(verbose, "Client "+str(addr)+" uploading: "+name)
        try:
            f = open(sPath+name, "wb")
        except Exception:
            Logger.log("Client "+str(addr)+" error opening file"+name)
            s.send("ERROR".encode())
            s.close()
            return
        s.send("OK".encode())
        data = s.recv(Constants.bytesChunk())
        try:
            size = int(data.decode())
        except Exception:
            strSize = data.decode()
            Logger.log("Client "+str(addr)+" invalid file size "+strSize)
            s.send("ERROR".encode())
            s.close()
            return
        s.send("OK".encode())
        Logger.logIfVerbose(verbose, "Client "+str(addr)+" file size: "+str(size))
        chunkSize = Constants.bytesChunk()
        Logger.logIfVerbose(verbose, "Client "+str(addr)+" getting file...")
        FileTransfer.recieveFile(s, f, name, size, chunkSize, verbose, quiet)
        Logger.log("Client "+str(addr)+" finished")
        f.close()
        s.close()
        return
