import sys
from lib.params.paramsValidation import Params


class ServerParams(Params):
    def validate():
        host, port, verbose, quiet, helpParam = Params.validate()
        sPath = ServerParams.getStoragePath()
        return host, port, sPath, verbose, quiet, helpParam

    def getStoragePath():
        sPath = ''
        i = 0
        while i < len(sys.argv):
            if sys.argv[i] == '-s' or sys.argv[i] == '--storage':
                if len(sys.argv) > i+1:
                    sPath = sys.argv[i+1]
                    i += 1
            i += 1
        if sPath == '':
            sPath = '/lib'
        return sPath
