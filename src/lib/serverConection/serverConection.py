from lib.serverConection.serverDownload import ServerDownload
from lib.serverConection.serverUpload import ServerUpload
from lib.logger.logger import Logger
from lib.constants import Constants


class ServerConection:
    def new_client_connected(s, sPath, addr, verbose, quiet):
        data = s.recv(Constants.bytesChunk())
        if data.decode() == 'download':
            Logger.logIfVerbose(verbose, "Client " + str(addr) + "started")
            Logger.logIfNotQuiet(quiet, "Initiating download process.")

            Logger.logIfVerbose(verbose, "Sending OK code to client")
            s.send('OK'.encode())
            return ServerDownload.download(s, sPath, addr, verbose, quiet)

        elif data.decode() == 'upload':
            Logger.logIfVerbose(verbose, "Client " + str(addr) + "started")
            Logger.logIfNotQuiet(quiet, "Initiating upload process.")

            Logger.logIfVerbose(verbose, "Sending OK code to client")
            s.send('OK'.encode())
            return ServerUpload.upload(s, sPath, addr, verbose, quiet)

        else:
            Logger.log("Client " + str(addr) + " is not upload or download")
            Logger.logIfVerbose(verbose, "Sending ERROR code to client")

            s.send('ERROR'.encode())

        s.close()
        Logger.log("Server closed")
        return
