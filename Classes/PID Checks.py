from Daq_Functions.DAQSimpleDOTask import DAQSimpleDOTask
import time



odor0 = DAQSimpleDOTask('Dev3/port0/line7')
odorb = DAQSimpleDOTask('Dev3/port0/line5')
odorc = DAQSimpleDOTask('Dev3/port0/line6')
odor_to_mouse = DAQSimpleDOTask('Dev3/port1/line2')
air_to_exhaust = DAQSimpleDOTask('Dev3/port2/line0')

num = 15
for _ in range  (num):
     odor0.high()
     time.sleep(1.2)
     odor_to_mouse.high()
     air_to_exhaust.high()
     time.sleep(2)
     odor0.low()
     odor_to_mouse.low()
     air_to_exhaust.low()
     time.sleep(5)

     # odorb.high()
     # time.sleep(1.2)
     # odor_to_mouse.high()
     # air_to_exhaust.high()
     # time.sleep(2)
     # odorb.low()
     # odor_to_mouse.low()
     # air_to_exhaust.low()
     # time.sleep(2)
     #
     # odorc.high()
     # time.sleep(1.2)
     # odor_to_mouse.high()
     # air_to_exhaust.high()
     # time.sleep(2)
     # odorc.low()
     # odor_to_mouse.low()
     # air_to_exhaust.low()
     # time.sleep(2)

     # odorb.high()
     # time.sleep(2)
     # odorb.low()
     # time.sleep(3)
#




