class StatRec(object):
    def __init__(self):
        self.buffer = np.zeros((10,2000))
        self.state_dict = {'success': 1, 'failure':2, 'early':3, 'miss':4}
        self.trial = 0
        self.up_to_date = True

    def increment(self, state_name,j):
        #called by task object, whenever mice make a choice

        state = self.state_dict[state_name]
        self.up_to_date = False
        self.trial +=1
        i=self.trial
        self.buffer[:,i] = self.buffer[:,i - 1]
        self.buffer[0, i] = self.trial
        self.buffer[state, i] += 1
        self.buffer[5:9, i] = 100.0 * self.buffer[1:5, i] / self.trial
        self.buffer[9, i] = j

    def write(self):
        # output to a buffer
        self.up_to_date = True
        return self.buffer, self.trial

    def updated (self):
        return self.up_to_date

