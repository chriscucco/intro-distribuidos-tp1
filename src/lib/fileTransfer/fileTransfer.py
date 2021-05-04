import os
from lib.logger.logger import Logger


class FileTransfer:
    def sendFile(s, f, chunkSize, verbose, quiet):
        while True:
            chunk = f.read(chunkSize)
            if not chunk:
                break
            s.send(chunk.encode())

    def sendFileSize(s, f, verbose, quiet):
        f.seek(0, os.SEEK_END)
        size = f.tell()
        f.seek(0, os.SEEK_SET)
        s.send(str(size).encode())

    def recieveFile(s, f, name, fileSize, chunkSize, verbose, quiet):
        try:
            bytesRecieved = 0
            while bytesRecieved < fileSize:
                data = s.recv(chunkSize)
                bytesRecieved += len(data)
                f.write(data)
            s.send("OK")
        except Exception:
            Logger.log("Failed saving file " + name)
            s.send("ERROR")
            return
