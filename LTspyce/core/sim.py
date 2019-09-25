
import os

class Sim:

    filePath = ""
    wasExecuted = False

    def __init__(self, path):
        if os.path.isfile(path):
            self.filePath = path
        else:
            raise FileNotFoundError("Couldn't find file: "+path)
            

    def getPath(self):
        return self.filePath

    def run(self):
        os.system("scad3.exe -Run -b "+self.filePath)
        wasExecuted = True

        
