## Introducción a los Sistemas Distribuidos (75.43/75.33/95.60)

This is a client-server app that allows to upload and download files from clients to the server, using TCP protocol and Python's standard Socket lib.
Server can recieve multiple clients at the same time, using a multithreading model.

### Authors
- Ramiro Santos
- Guido Negri
- Christian Cucco

### Requirements: 
- Python 3 


### Usage

#### Server
For running the server, execute current command in root/src folder:
` python3 start-server.py [-h] [-v | -q] [-H ADDR] [-p PORT] [-s DIRPATH] `

Example:
` python3 start-server.py -p 8080 -v -s lib/ `

Complete parameters options are described running `python3 start-server.py -h -s /lib`

Default address value is 127.0.0.1 (Localhost) and default port is 8080. Also default path for saving files and searching in downloads is root/src folder.

To close server, only write `exit` in console where server is running, and it will close all sockets and join thread, without loosing memory.

#### Client Upload
For running the client upload, execute current command in root/src folder:
` python3 upload-file.py [-h] [-v | -q] [-H ADDR] [-p PORT] [-s FILEPATH] [-n FILENAME] `

Example:
` python3 upload-file.py -v -H 127.0.0.1 -p 8080 -n Test.txt `

Complete parameters options are described running `python3 upload-file.py -h`

Default address that client will try to connect value is 127.0.0.1 (Localhost) and default port is 8080. Also default path for searching files is root/src folder.

Once file is uploaded and server's response is affirmative, client finishes.

#### Client Download
For running the client download, execute current command in root/src folder:
` python3 download-file.py [-h] [-v | -q] [-H ADDR] [-p PORT] [-d FILEPATH] [-n FILENAME] `

Example:
` python3 download-file.py -v -H 127.0.0.1 -p 8080 -n Test.txt `

Complete parameters options are described running `python3 download-file.py -h`

Default address that client will try to connect value is 127.0.0.1 (Localhost) and default port is 8080. Also default path for searching files is root/src folder.

Once file is downloaded, client finishes.