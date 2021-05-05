import sys
from lib.params.paramsValidation import Params


class UploadClientParams(Params):
    def validate():
        host, port, verbose, quiet, helpParam = Params.validate()
        fName, fSourcePath = UploadClientParams.getSourcePathAndFilename()
        return host, port, fName, fSourcePath, verbose, quiet, helpParam

    def getSourcePathAndFilename():
        fName = ''
        fSourcePath = ''
        i = 0
        while i < len(sys.argv):
            if sys.argv[i] == '-s' or sys.argv[i] == '--src':
                if len(sys.argv) > i+1:
                    fSourcePath = sys.argv[i+1]
                    i += 1
            if sys.argv[i] == '-n' or sys.argv[i] == '--name':
                if len(sys.argv) > i+1:
                    fName = sys.argv[i+1]
                    i += 1
            i += 1
        if fName == '':
            fName = 'test'
        if fSourcePath == '':
            fSourcePath = '/lib'
        return fName, fSourcePath
