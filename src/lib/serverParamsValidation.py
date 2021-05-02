import sys

class Params():
    def initializeParams():
        return '', '', '', False, False, False
    
    def processParams(host, port, sPath): 
        if host == '':
            host = '127.0.0.1'
        if port == '':
            port = '8080'
        if sPath == '':
            sPath = '/lib'
        return host, port, sPath

    def validateParams():
        host, port, sPath, verboseParam, quietParam, helpParam = Params.initializeParams()
        i = 0
        while i < len(sys.argv):
            if sys.argv[i] == '-h' or sys.argv[i] == '--help':
                helpParam = True
            elif sys.argv[i] == '-v' or sys.argv[i] == '--verbose':
                verboseParam = True
            elif sys.argv[i] == '-q' or sys.argv[i] == '--quiet':
                quietParam = True
            elif sys.argv[i] == '-H' or sys.argv[i] == '--host':
                if len(sys.argv) > i+1:
                    host = sys.argv[i+1]
                    i += 1
            elif sys.argv[i] == '-p' or sys.argv[i] == '--port':
                if len(sys.argv) > i+1:
                    port = sys.argv[i+1]
                    i += 1
            elif sys.argv[i] == '-s' or sys.argv[i] == '--storage':
                if len(sys.argv) > i+1:
                    sPath = sys.argv[i+1]
                    i += 1
            i+= 1
        host, port, sPath = Params.processParams(host, port, sPath)
        return host, port, sPath, verboseParam, quietParam, helpParam