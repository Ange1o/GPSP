# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:21:33 2017

@author: wd1u16
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score


LINEpath = "H:\\node clustering\\deepwalk\\PaperDeepwalk.txt"

line = pd.read_csv(LINEpath, header=None, delim_whitespace=True)



GroupPath = "H:\\node clustering\\deepwalk\\group.txt"

group = pd.read_csv(GroupPath, names=[1,0], delim_whitespace=True).drop(1, axis=1)


group = group-1




g_list = group[0].values.tolist()

#
#g_list=[0,0,0,0,0,0,0,0]
#
#
#g_list[0] = group[group[0]==0]
#g_list[1] = group[group[0]==1]
#g_list[2] = group[group[0]==2]
#g_list[3] = group[group[0]==3]
#g_list[4] = group[group[0]==4]
#g_list[5] = group[group[0]==5]
#g_list[6] = group[group[0]==6]
#g_list[7] = group[group[0]==7]

    
seeds=np.random.randint(99999999, size=10)
#ratio= [0,0,0,0,0,0,0,0,0,0]
ars = [0,0,0,0,0,0,0,0,0,0]


i=10

for a in range (0,i):
    
    clusterer = KMeans(n_clusters = 8, random_state = seeds[a])
    
    
    cluster_labels = pd.DataFrame(clusterer.fit_predict(line))
    
    
    c_list = cluster_labels[0].values.tolist()
    
    ars[a] = adjusted_rand_score(c_list,g_list)
    
print(sum(ars)/i)
    