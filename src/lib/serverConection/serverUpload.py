from lib.constants import Constants
from lib.fileTransfer.fileTransfer import FileTransfer


class ServerUpload:
    def upload(s, sPath, verbose, quiet):
        data = s.recv(Constants.bytesChunk())
        fileName = data.decode()
        try:
            f = open(sPath+fileName, "wb")
        except Exception:
            s.send("ERROR".encode())
            s.close()
            return
        s.send("OK".encode())
        data = s.recv(Constants.bytesChunk())
        try:
            size = int(data.decode())
        except Exception:
            s.send("ERROR".encode())
            s.close()
            return
        s.send("OK".encode())
        chunkSize = Constants.bytesChunk()
        FileTransfer.recieveFile(s, f, size, chunkSize, verbose, quiet)
        f.close()
        s.close()
        return
