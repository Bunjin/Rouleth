from random import randint

win_if_lte = 17
payoff = 2.0

block_reward = 5.0

def bet_n_times(n, bet_size):
    profit = 0
    for i in range(n):
        profit -= bet_size + 0.003 #transaction fees
        roll = randint(0,36)
        if roll <= win_if_lte:
            # We won!
            profit += bet_size * payoff
    return profit

def bet_n_times_with_cheat(n, stake, pom):
#Without Uncles
#uncle_reward = 0
# With Uncles
    uncle_reward= pom*(4.375+1/32*5.0) + (1-pom)*3.75 - 0.01
    # print(uncle_reward)
# uncle included in first next or second
# first if auto includes (receives bonus), second if network -> simplification
# no transaction fees
    profit=0
    for i in range(n):
        # print(profit," time", i)
        profit = profit - stake - 0.003 #transaction fees
        if randint(1,100) > pom * 100:
        #we did not find the first block but still have a chance as a "normal player"
            roll = randint(0,36)
            if roll <= win_if_lte: #and won !
                profit += stake * payoff
            else :
                pass
        #we found the block
        else :
            roll = randint(0,36)
            if roll <= win_if_lte: #and won !
                profit += stake * payoff 
            else :  
                # We mined a losing block we give it up
                profit -= block_reward
                # We try to mine another block
                if randint(1,100) <= pom * 100: # success
                        profit += block_reward
                else : #fail
                        profit += uncle_reward
                #we still get the uncle reward !
                #check the bet result in this case :       
                roll = randint(0,36)
                if roll <= win_if_lte: #won !
                        profit += stake * payoff
    return profit


trials = 10000000 #

def find_betlimit(percent_of_mining):
    bet_size=0.2
    while True:
       profit_trial=bet_n_times_with_cheat(trials, bet_size, percent_of_mining)
       #print(percent_of_mining)
       if percent_of_mining<=1 : #0.01:
           #for first run (in terms of pom) only print the details, because it might not stop
           print(profit_trial)
           print(bet_size)
       if profit_trial<0:
           if percent_of_mining<=0.05:
               bet_size+=0.1
           elif percent_of_mining<=0.25:
               bet_size+=0.25
           elif percent_of_mining<=1:
               bet_size+=0.1
       else:
           break
       if bet_size>100000000:
           break #max supply ether

    return bet_size


power=0.24
for k in range(50):
    power+=0.01
    lim=find_betlimit(power)
    print(power*100,"% mining ", lim, "payroll", lim*20*35)


    #under 3% power : bet size larger than total eth supply 
    # 3 % : 23 eth max bet per block
    # 4 % : 4 eth max bet per block
    # 5 % : 3 eth max bet per block
    # 6% : 2.5 eth max bet per block
    # 7 % : 2 eth
    # 8 % : 1.95
    # 9% : 1.85
    # 10% : 1.75
    # 11% : 1.5
    # 25 % : 1.2
    # 51% : 0.5 eth
    #a lot of variance for the small % of mining cases
    # need sample size >5M for accurate result !
    # todo : Compute variance of this random var

    # 
