import sys
import logging
sys.path.insert(0,'..')
import LTspyce.core.sim as LTS_sim
import LTspyce.core.SimResults as LTS_simRes
import LTspyce.core.log.logger as LTspyceLogger
from matplotlib import pyplot as plt

LTspyceLogger.default_log(logging.DEBUG)

exSim = LTS_sim.Sim("RC_Circuit.asc")
exSim.run()

Result = LTS_simRes.SimResult("RC_Circuit.raw")
Result.readMetadata()
print(Result.getSimDate())
print(Result.getNoPoints())
print(Result.getNoVars())
print(Result._timeIndex)
print(Result._vol)
print(Result._cur)
t = Result.getTime()
v = Result.getVoltage('v_out')
i = Result.getCurrent('R1')

max_val = max(i)
max_index = i.index(max_val)
print('Max value: '+str(max_val)+' A at t='+str(t[max_index]*1000)+' ms')
print(i[max_index])
plt.plot(t,i)
plt.show()

