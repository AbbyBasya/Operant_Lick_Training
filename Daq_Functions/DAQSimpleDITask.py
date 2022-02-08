from PyDAQmx import *
from ctypes import byref, c_ulong,c_int32, c_int8
import numpy as np

#     a simple task that reads one digital input line

class DAQSimpleDITask(Task):

    def __init__(self, chan='Dev1/port0/line7'):
        '''
        chan: name of the channel, in the format of Dev2/port0/line0
        '''
        Task.__init__(self)
        self.chan = chan
        self.CreateDIChan(self.chan, '', DAQmx_Val_ChanPerLine)

    def read(self, timeout=0.0001):
        '''
        read a single sample from the digital line

        timeout: timeout in seconds
        '''
        read_array = np.zeros((1,), dtype=np.uint8)
        written = c_int32(0)
        written2 = c_int32(0)
        self.ReadDigitalLines(1, timeout, DAQmx_Val_GroupByScanNumber, read_array, 1, byref(written), byref(written2),
                              None)
        return read_array

    def close(self):
        '''
        close task
        '''
        self.ClearTask()


if __name__ == '__main__':
    ditask = DAQSimpleDITask()
    print(ditask.read())
    ditask.close()


