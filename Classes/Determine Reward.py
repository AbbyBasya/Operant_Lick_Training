#cleanup + doublecheck

def determine_reward_lickUnlimited (self, action_interval):
    checkperiod = 0.005
    action_timeout = time.time() + action_interval
    right_lick_last = 0
    count = 0

    while time.time() < action_timeout:
        right_lick = self.lickR.read()
        if right_lick != right_lick_last:
            if right_lick:
                print('Lick')
                d = self.ws1.cell(row=(self.ws1.max_row + 1), column=1, value=time.time())
                d = self.ws1.cell(row=self.ws1.max_row, column=2, value=11)

                count +=1
            else:
                d = self.ws1.cell(row=(self.ws1.max_row + 1), column=1, value=time.time())
                d = self.ws1.cell(row=self.ws1.max_row, column=2, value=10)
        else:
            pass
        right_lick_last = right_lick
        time.sleep(checkperiod)

    while time.time()
        if right_lick >= self.licknum:

            print('licking activate reward')
            return reward_on


def determine_reward_lickLimited (self, pre_action_interval, action_interval, check_action=True):
    checkperiod = 0.005

    pre_action_timeout = time.time() + pre_action_interval
    action_timeout = time.time() + action_interval

    reward_on = True
    right_lick_last = 0
    wrong_lick_last = 0

    count = 0

    while time.time() < pre_action_timeout:
        wrong_lick = self.lickR.read()
        if wrong_lick != wrong_lick_last:
            if wrong_lick:
                print('Extraneous Lick')
                d = self.ws1.cell(row=(self.ws1.max_row + 1), column=1, value=time.time())
                d = self.ws1.cell(row=self.ws1.max_row, column=2, value=11)

                if check_action:
                    count += 1

            else:
                d = self.ws1.cell(row=(self.ws1.max_row + 1), column=1, value=time.time())
                d = self.ws1.cell(row=self.ws1.max_row, column=2, value=10)
        else:
            pass
        wrong_lick_last = wrong_lick
        time.sleep(checkperiod)


    while time.time() < action_timeout:
        right_lick = self.lickR.read()
        if right_lick != right_lick_last:
            if right_lick:
                print('Lick')
                d = self.ws1.cell(row=(self.ws1.max_row + 1), column=1, value=time.time())
                d = self.ws1.cell(row=self.ws1.max_row, column=2, value=11)

                if check_action:
                    count += 1

            else:
                d = self.ws1.cell(row=(self.ws1.max_row + 1), column=1, value=time.time())
                d = self.ws1.cell(row=self.ws1.max_row, column=2, value=10)
        else:
            pass
        right_lick_last = right_lick
        time.sleep(checkperiod)

    while time.time()
        if check_action and (right_lick >= self.licknum) and (wrong_lick==0):

            print('correct licking activate reward')
            return reward_on

        elif check_action and right_lick < self.licknum:
            print('not enough licking for reward')
            reward_on = False

        elif check_action and wrong_lick > 0:
            print('extraneous licking so no reward')
            reward_on = False
            ### need to increase ITI by 5s

    def check_licking_1spout(self, pre_action_interval, action_interval, check_action=False):
        checkperiod = 0.005
        timeout = time.time() + pre_action_interval
        reward_on = True
        right_lick_last = 0
        count = 0
        while time.time() < timeout:
            right_lick = self.lickR.read()
            if right_lick != right_lick_last:
                if right_lick:
                    print('Lick')
                    d = self.ws1.cell(row=(self.ws1.max_row + 1), column=1, value=time.time())
                    d = self.ws1.cell(row=self.ws1.max_row, column=2, value=11)

                    if check_action:
                        count += 1

                else:
                    d = self.ws1.cell(row=(self.ws1.max_row + 1), column=1, value=time.time())
                    d = self.ws1.cell(row=self.ws1.max_row, column=2, value=10)
            else:
                pass
            right_lick_last = right_lick
            time.sleep(checkperiod)

        while time.time()
            if check_action and count >= self.licknum:

                print('licking activate reward')
            elif check_action and count < self.licknum:
                print('not enough licking')
                reward_on = False
            elif
                return reward_on
