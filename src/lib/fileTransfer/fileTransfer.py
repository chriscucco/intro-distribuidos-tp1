import os


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
