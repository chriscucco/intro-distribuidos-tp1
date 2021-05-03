
DATA_CHUNK = 1024


class ServerConection:
    def new_client_connected(s, sPath, verbose, quiet):
        data = s.recv(DATA_CHUNK)
        if data.decode() == 'upload':
            s.send("OK".encode())
            print("NEW UPLOAD CLIENT")
        elif data.decode() == 'download':
            s.send("OK".encode())
            print("NEW DOWNLOAD CLIENT")
        else:
            s.send("ERROR".encode())
        s.close()
        return
