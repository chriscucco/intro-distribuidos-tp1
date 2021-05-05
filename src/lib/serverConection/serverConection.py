from lib.serverConection.serverDownload import ServerDownload
from lib.serverConection.serverUpload import ServerUpload
from lib.logger.logger import Logger
from lib.constants import Constants


class ServerConection:
    def new_client_connected(s, sPath, addr, verbose, quiet):
        data = s.recv(Constants.bytesChunk())
        if data.decode() == 'download':
            Logger.logIfVerbose(verbose, "Client " + str(addr) + "started")
            s.send("OK".encode())
            return ServerDownload.download(s, sPath, addr, verbose, quiet)
        elif data.decode() == 'upload':
            Logger.logIfVerbose(verbose, "Client " + str(addr) + "started")
            s.send("OK".encode())
            return ServerUpload.upload(s, sPath, addr, verbose, quiet)
        else:
            Logger.log("Client " + str(addr) + " is not upload or download")
            s.send("ERROR".encode())
        s.close()
        return
