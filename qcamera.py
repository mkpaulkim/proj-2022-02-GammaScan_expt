import numpy as np
import pycube_hwlib.hardware as hw
import pycubelib.plotting_functions as pf

t_exp = 5.0

qcam = hw.Quantalux()
qcam.setup(t_exp=5.0)

print('> acquire and plotAAB: ^C to stop ...')

try:
    while True:
        qcam.acquire_cc()
        AA = qcam.cc
        pf.plotAAB(AA, pause=.1, ulimit=(0, 2**16-1))
except KeyboardInterrupt:
    pass
