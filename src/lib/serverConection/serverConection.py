from lib.serverConection.serverDownload import ServerDownload
from lib.serverConection.serverUpload import ServerUpload
from lib.constants import Constants


class ServerConection:
    def new_client_connected(s, sPath, verbose, quiet):
        data = s.recv(Constants.bytesChunk())
        if data.decode() == 'upload':
            s.send("OK".encode())
            return ServerDownload.download(s, sPath, verbose, quiet)
        elif data.decode() == 'download':
            s.send("OK".encode())
            return ServerUpload.upload(s, sPath, verbose, quiet)
        else:
            s.send("ERROR".encode())
        s.close()
        return
