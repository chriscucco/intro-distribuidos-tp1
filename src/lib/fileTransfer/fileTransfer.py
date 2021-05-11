import os
from lib.logger.logger import Logger


class FileTransfer:
    def sendFile(s, f, chunkSize):
        while True:
            chunk = f.read(chunkSize)
            if not chunk:
                break
            s.send(chunk)

    def sendFileSize(s, f, verbose, quiet):
        f.seek(0, os.SEEK_END)
        size = f.tell()
        Logger.logIfNotQuiet(quiet, "Size of file to send: " +
                             str(size))
        f.seek(0, os.SEEK_SET)
        s.send(str(size).encode())

    def recieveFile(s, f, name, fileSize, chunkSize, verbose, quiet):
        try:
            bytesRecieved = 0
            while bytesRecieved < int(fileSize):
                data = s.recv(chunkSize)
                bytesRecieved += len(data)
                f.write(data)

            # Logger.logIfVerbose(verbose, "Sending OK code")
            s.send("OK".encode())
        except Exception:
            Logger.log("Failed saving file " + name)
            Logger.logIfVerbose(verbose, "Sending ERROR code")
            s.send("ERROR".encode())
            return
