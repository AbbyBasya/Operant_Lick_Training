import time
from Daq_Functions.DAQSimpleDITask import DAQSimpleDITask
lick = DAQSimpleDITask('Dev1/port0/line7')
timeout = time.time() + 100

while time.time() < timeout:
    print(lick.read())
    time.sleep(.02)
lick.close()

import time
from Daq_Functions.DAQSimpleDOTask import DAQSimpleDOTask
water = DAQSimpleDOTask('Dev1/port1/line3')

water.high()
time.sleep(0.1)

#from Classes.Training_Setup import determine_reward_lickUnlimited
#determine_reward_lickUnlimited(self.duration_water_large, True)

water.low()