import logging
import os
import string
import struct


class SimResult:
    def __init__(self, path):
        self._logger = logging.getLogger(__name__)
        if os.path.isfile(path):
            self._Path = path
            self._vol = dict()
            self._cur = dict()
            self._logger.debug('SimResult Object (%s) created', path)
        else:
            self._logger.error('File %s not found', path)
            raise FileNotFoundError("Couldn't find file: " + path)


    def readMetadata(self):
        self._logger.debug('readMetadata called')
        self._logger.debug('\t reading from: %s', self._Path)
        self._metadata = dict()
        with open(self._Path, "rb") as rawFile:

            for line in rawFile:
                lineDec = line.decode('utf-8')
                spLine = lineDec.split(":", 1)
                if (len(spLine) != 2):
                    raise ValueError('Couldn''t parse line: ' + lineDec.strip() + ' of file: ' + self._Path)
                if spLine[0] == "Binary":
                    break
                elif spLine[0] == "Variables":
                    break
                else:
                    self._metadata[spLine[0].strip()] = spLine[1].strip()

            i = 1
            for line in rawFile:
                lineDec = line.decode('utf-8')
                spLine = lineDec.split(None,2)
                if spLine[2].strip() == 'time':
                    self._timeIndex = int(spLine[0])
                elif spLine[2].strip() == 'voltage':
                    self._vol[spLine[1].strip()] = int(spLine[0])
                elif spLine[2].strip() == 'device_current':
                    self._cur[spLine[1].strip()] = int(spLine[0])
                else:
                    raise ValueError('Couldn''t parse variable: '+spLine[2].strip())

                if i >= int(self._metadata["No. Variables"]):
                    break
                else:
                    i = i + 1


    def getPath(self):
        self._logger.debug('getPath called')
        return self._Path

    def printMetaData(self):
        self._logger.debug('printMetaData called')
        for key in self._metadata:
            print(key, ': ', self._metadata[key])

    def getSimDate(self):
        self._logger.debug('getSimDate called')
        return self._metadata['Date']

    def getNoVars(self):
        self._logger.debug('getNoVars called')
        return int(self._metadata["No. Variables"])

    def getNoPoints(self):
        self._logger.debug('getNoPoints called')
        return int(self._metadata["No. Points"])

    def getTime(self):
        with open(self._Path, "rb") as rawFile:

            for line in rawFile:
                lineDec = line.decode('utf-8')
                spLine = lineDec.split(":", 1)
                if spLine[0] == "Binary":
                    break

            nPoint = int(self._metadata["No. Points"])
            nVars = int(self._metadata["No. Variables"])
            t = []
            for i in range(0,nPoint):
                t.append(abs(struct.unpack('d', rawFile.read(8))[0]))
                rawFile.seek(4*(nVars-1), os.SEEK_CUR)
            return t

    def getVoltage(self,node):
        varName = 'V('+node+')'
        varIndex = int(self._vol[varName])
        with open(self._Path, "rb") as rawFile:
            for line in rawFile:
                lineDec = line.decode('utf-8')
                spLine = lineDec.split(":", 1)
                if spLine[0] == "Binary":
                    break

            nPoint = int(self._metadata["No. Points"])
            nVars = int(self._metadata["No. Variables"])
            vol = []
            for i in range(0,nPoint):
                rawFile.seek(8+4*(varIndex - 1), os.SEEK_CUR)
                vol.append(struct.unpack('f', rawFile.read(4))[0])
                rawFile.seek(4*(nVars-varIndex-1), os.SEEK_CUR)
            return vol

    def getCurrent(self,node):
        varName = 'I('+node+')'
        varIndex = int(self._cur[varName])
        with open(self._Path, "rb") as rawFile:
            for line in rawFile:
                lineDec = line.decode('utf-8')
                spLine = lineDec.split(":", 1)
                if spLine[0] == "Binary":
                    break

            nPoint = int(self._metadata["No. Points"])
            nVars = int(self._metadata["No. Variables"])
            cur = []
            for i in range(0,nPoint):
                rawFile.seek(8+4*(varIndex - 1), os.SEEK_CUR)
                cur.append(struct.unpack('f', rawFile.read(4))[0])
                rawFile.seek(4*(nVars-varIndex-1), os.SEEK_CUR)
            return cur
