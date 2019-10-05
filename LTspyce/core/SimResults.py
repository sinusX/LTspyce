import logging
import os
import string

class SimResult:

    def __init__(self, path):
        self._logger = logging.getLogger(__name__)
        if os.path.isfile(path):
            self._Path = path
        else:
            self._logger.error('File %s not found',path)
            raise FileNotFoundError("Couldn't find file: "+path)
        self._logger.debug('SimResult Object (%s) created',path)

    def readMetadata(self):
        self._logger.debug('readMetadata called')
        self._logger.debug('\t reading from: %s',self._Path)
        self._metadata = dict()
        with open(self._Path, "rb") as rawFile:

            for line in rawFile:
                lineDec = line.decode('utf-8')
                spLine = lineDec.split(":", 1)
                if spLine[0] == "Binary":
                    break
                elif spLine[0] == "Variables":
                    break
                else:
                    self._metadata[spLine[0].strip()] = spLine[1].strip()


    def getPath(self):
        self._logger.debug('getPath called')
        return self._Path

    def printMetaData(self):
        self._logger.debug('printMetaData called')
        for key in self._metadata:
            print(key,': ',self._metadata[key])

    def getSimDate(self):
        self._logger.debug('getSimDate called')
        return self._metadata['Date']

    def getNoVars(self):
        self._logger.debug('getNoVars called')
        return int(self._metadata["No. Variables"])

    def getNoPoints(self):
        self._logger.debug('getNoPoints called')
        return int(self._metadata["No. Points"])

