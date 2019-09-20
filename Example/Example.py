import sys
sys.path.insert(0,'..')
import LTspyce.core.sim as LTS_sim

exSim = LTS_sim.Sim("RC_Circuit")
exSim.run()
