from Daq_Functions.DAQSimpleDOTask import DAQSimpleDOTask
import time

odor7 = DAQSimpleDOTask('Dev1/port2/line6')
#odor6 = DAQSimpleDOTask('Dev1/port2/line6')


odor7.high()
time.sleep(2)
odor7.low()
time.sleep(6)
odor7.high()
time.sleep(2)
odor7.low()
print('2nd time')
time.sleep(6)
odor7.high()
time.sleep(2)
odor7.low()
print('3rd time')
time.sleep(6)
odor7.high()
time.sleep(2)
odor7.low()
time.sleep(6)
odor7.high()
time.sleep(2)
odor7.low()