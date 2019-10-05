import sys
import logging
sys.path.insert(0,'..')
import LTspyce.core.sim as LTS_sim
import LTspyce.core.log.logger as LTspyceLogger

LTspyceLogger.default_log(logging.DEBUG)

exSim = LTS_sim.Sim("RC_Circuit.asc")
exSim.run()

