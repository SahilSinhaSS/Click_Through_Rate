#Thompson sampling

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')


#Building TS
import random
N = 10000
d = 10
total_reward = 0
ads_selected = []
not_reward1 = [0]*d
not_reward0 = [0]*d
for n in range(0,N):
    max_random = 0
    ad = 0
    for i in range(0,d):
        random_beta = random.betavariate(not_reward1[i]+1, not_reward0[i]+1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    if reward == 1:
        not_reward1[ad] = not_reward1[ad] + 1
    else:
        not_reward0[ad] = not_reward0[ad] + 1
    total_reward = total_reward + reward
    

            
        
