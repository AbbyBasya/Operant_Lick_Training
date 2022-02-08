from Daq_Functions.DAQSimpleDOTask import DAQSimpleDOTask


class OdorGen(object):
    def __init__(self,odorindex):
        self.odorindex = odorindex
        self.odors_DAQ=[]

    #initiate odor solenoids
    def assign_odor(self):
        for item in self.odorindex:
            self.odors_DAQ.append(DAQSimpleDOTask('Dev1/port2/line{}'.format(item)))
        print ('Odor {} has been assigned'.format(self.odorindex))

    # saying that the rewarded done with be one labeled 0
    def set_rewardodor(self, index:list):
        reward_odor = self.odors_DAQ[index[0]]
        non_reward_odor = self.odors_DAQ[index[1]]
        print ('reward odor and unrewarded odor loaded')
        return reward_odor, non_reward_odor

    def initiate (self):
        for odor in self.odors_DAQ:
            print(odor)
            odor.low()
        print ('odor initiation:status low')

    def close (self):
        for odor in self.odors_DAQ:
            odor.close()
        print ('Connection has been closed')




