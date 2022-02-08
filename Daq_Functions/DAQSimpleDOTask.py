from PyDAQmx import *
from ctypes import byref, c_ulong, c_int32
import numpy as np


class DAQSimpleDOTask(Task):
    '''
    a simple task that set one digital output line to high or low
    '''

    def __init__(self, chan='Dev`/port0/line0'):
        '''
        chan: name of the channel, in the format of Dev2/port0/line0
        '''
        Task.__init__(self)
        self.chan = chan
        self.CreateDOChan(self.chan, '', DAQmx_Val_ChanPerLine)

    def write(self, value, timeout=0.0001):
        '''
        write a single sample to the digital line

        value: 1-D array with the size of the number of channels take np.uint8 array
        timeout: timeout in seconds
        '''
        written = c_int32(0)
        self.WriteDigitalLines(1, True, timeout, DAQmx_Val_GroupByScanNumber, value, byref(written), None)

    def high(self, timeout=0.0001):
        '''
        change the digital line to high

        timeout: timeout in seconds
        '''
        self.write(np.array([1], dtype=np.uint8), timeout)

    def low(self, timeout=0.0001):
        '''
        change the digital line to low

        timeout: timeout in seconds
        '''
        self.write(np.array([0], dtype=np.uint8), timeout)

    def close(self):
        '''
        close task
        '''
        self.ClearTask()