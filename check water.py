import time
from Daq_Functions.DAQSimpleDOTask import DAQSimpleDOTask
water = DAQSimpleDOTask('Dev1/port1/line3')

water.high()
time.sleep(1)

#from Classes.Training_Setup import determine_reward_lickUnlimited
#determine_reward_lickUnlimited(self.duration_water_large, True)

water.low()