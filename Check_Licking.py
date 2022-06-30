import time
from Daq_Functions.DAQSimpleDITask import DAQSimpleDITask
lick = DAQSimpleDITask('Dev1/port0/line7')
timeout = time.time() + 100

while time.time() < timeout:
    print(lick.read())
    time.sleep(.05)
lick.close()

