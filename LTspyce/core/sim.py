
import os

class Sim:

    name = "";
    wasExecuted = false

    def __init__(self, a_name):
        self.name = a_name

    def getName(self):
        return self.name;

    def run(self):
        os.system("scad3.exe -Run -b -ascii "+self.name+".asc")
        wasExecuted = true

        
