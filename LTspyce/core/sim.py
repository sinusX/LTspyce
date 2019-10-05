
import os
import logging

class Sim:

    def __init__(self, path):
        self._logger = logging.getLogger(__name__)
        if os.path.isfile(path):
            self._filePath = path
            self._wasExecuted = False
        else:
            self._logger.error('File %s not found',path)
            raise FileNotFoundError("Couldn't find file: "+path)
        self._logger.debug('Sim Object (%s) created',path)
            

    def getPath(self):
        return self._filePath

    def run(self):
        os.system("scad3.exe -Run -b "+self._filePath)
        wasExecuted = True
        self._logger.debug('Simulation (%s) executed',self._filePath)



