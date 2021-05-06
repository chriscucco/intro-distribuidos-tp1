import os
from lib.logger.logger import Logger


class FileTransfer:
    # sacar parametros verbose y quite si no se van a usar
    def sendFile(s, f, chunkSize, verbose, quiet):
        chunk = f.read(chunkSize)
        while True:
            s.send(chunk)
            chunk = f.read(chunkSize)
            if not chunk:
                break

    def sendFileSize(s, f, verbose, quiet):
        f.seek(0, os.SEEK_END)
        size = f.tell()
        f.seek(0, os.SEEK_SET)
        s.send(str(size).encode())

    def recieveFile(s, f, name, fileSize, chunkSize, verbose, quiet):
        try:
            bytesRecieved = 0
            while bytesRecieved < int(fileSize):
                data = s.recv(chunkSize)
                bytesRecieved += len(data)
                f.write(data)
            s.send("OK".encode())
        except Exception:
            Logger.log("Failed saving file " + name)
            s.send("ERROR".encode())
            return
