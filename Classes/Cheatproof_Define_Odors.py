from Daq_Functions.DAQSimpleDOTask import DAQSimpleDOTask


class OdorGen(object):
    def __init__(self,odorindex):
        self.odorindex = odorindex
        self.odors_DAQ=[]

    #initiate odor solenoids
    def assign_odor(self):
        for item in self.odorindex:
            self.odors_DAQ.append(DAQSimpleDOTask('Dev3/port0/line{}'.format(item)))
        print ('Odor {} has been assigned'.format(self.odorindex))

    # saying that the rewarded done with be one labeled 0
    def set_rewardodor(self, index:list):

        reward_odor1 = self.odors_DAQ[index[0]]
        reward_odor2 = self.odors_DAQ[index[1]]
        reward_odor3 = self.odors_DAQ[index[2]]

        non_reward_odor1 = self.odors_DAQ[index[3]]
        non_reward_odor2 = self.odors_DAQ[index[4]]
        non_reward_odor3 = self.odors_DAQ[index[5]]




        print ('reward odor and unrewarded odor loaded')
        return reward_odor1, reward_odor2, reward_odor3, non_reward_odor1, non_reward_odor2, non_reward_odor3

    def initiate (self):
        for odor in self.odors_DAQ:
            print(odor)
            odor.low()
        print ('odor initiation:status low')

    def close (self):
        for odor in self.odors_DAQ:
            odor.close()
        print ('Connection has been closed')




