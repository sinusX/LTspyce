import sys
import logging
sys.path.insert(0,'..')
import LTspyce.core.sim as LTS_sim
import LTspyce.core.SimResults as LTS_simRes
import LTspyce.core.log.logger as LTspyceLogger

LTspyceLogger.default_log(logging.DEBUG)

exSim = LTS_sim.Sim("RC_Circuit.asc")
exSim.run()

Result = LTS_simRes.SimResult("RC_Circuit.raw")
Result.readMetadata()
print(Result.getSimDate())
print(Result.getNoPoints())
print(Result.getNoVars())

