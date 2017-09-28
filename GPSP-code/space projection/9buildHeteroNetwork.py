# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 22:00:18 2017

@author: wd1u16
"""

import pandas as pd

lo1 = 'H:\\Downloads\\lineForHomo\\AMinerCoauthorUndirected.txt'


A2A = pd.read_csv(lo1, header=None, delim_whitespace=True)


lo2 = 'H:\\Downloads\\lineForHetero\\dataset\\AMiner-Author2Paper.txt'

a2p = pd.read_csv(lo2, header=None, delim_whitespace=True)


a=a2p.filter([1], axis=1)
p=a2p.filter([2], axis=1)
w=a2p.filter([3], axis=1)


p=-p
w=w*0+1


A2P = pd.concat([a,p,w],axis=1)


A2P.columns = [0,1,2]



loa2p='H:\\Downloads\\lineForHetero\\Author2PaperNetwork.txt'
A2P.to_csv(loa2p,sep=' ',header=False,index=False,decimal='.')



lo3 = 'H:\\Downloads\\lineForHetero\\paperNetwork.txt'

p2p = pd.read_csv(lo3, header=None, delim_whitespace=True)



p1=p2p.filter([0], axis=1)
p2=p2p.filter([1], axis=1)
w=p2p.filter([2], axis=1)


p1=-p1
p2=-p2

P2P = pd.concat([p1,p2,w],axis=1)


frames = [A2A,A2P,P2P]

result = pd.concat(frames,ignore_index=True)


combinedLo = 'H:\\Downloads\\lineForHetero\\heteroNetwork.txt'
result.to_csv(combinedLo,sep=' ',header=False,index=False,decimal='.')


result_unweighted = result.drop([2], axis=1)
combinedLo = 'H:\\Downloads\\lineForHetero\\heteroNetworkunweighted.txt'
result_unweighted.to_csv(combinedLo,sep=' ',header=False,index=False,decimal='.')




p1=-p1
p2=-p2

P2P_unweighted = pd.concat([p1,p2],axis=1)
combinedLo = 'H:\\Downloads\\lineForHetero\\paperNetworkUnweighted.txt'
P2P_unweighted.to_csv(combinedLo,sep=' ',header=False,index=False,decimal='.')
