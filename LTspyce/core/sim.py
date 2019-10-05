
import os
import logging

class Sim:

    filePath = ""
    wasExecuted = False

    def __init__(self, path):
        self.logger = logging.getLogger('LTspyce.core.sim')
        if os.path.isfile(path):
            self.filePath = path
        else:
            self.logger.error('File %s not found',path)
            raise FileNotFoundError("Couldn't find file: "+path)
        self.logger.debug('Sim Object (%s) created',path)
            

    def getPath(self):
        return self.filePath

    def run(self):
        os.system("scad3.exe -Run -b "+self.filePath)
        wasExecuted = True
        self.logger.debug('Simulation (%s) executed',self.filePath)

        
