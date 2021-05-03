from lib.constants import Constants
from lib.fileTransfer.fileTransfer import FileTransfer


class ServerDownload:
    def download(s, sPath, verbose, quiet):
        data = s.recv(Constants.bytesChunk())
        fileName = data.decode()
        try:
            f = open(sPath+fileName, "rb")
        except Exception:
            s.send("ERROR".encode())
            s.close()
            return
        FileTransfer.sendFileSize(s, f, verbose, quiet)
        FileTransfer.sendFile(s, f, Constants.bytesChunk(), verbose, quiet)
        f.close()
        s.close()
        return
