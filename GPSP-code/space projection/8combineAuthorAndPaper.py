# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 13:08:46 2017

@author: wd1u16
"""

import pandas as pd

lo = 'H:\\Downloads\\lineForHetero\\LINE12paperPosition.txt'

LINE1paper = pd.read_csv(lo, header=None,index_col=0, delim_whitespace=True)

locationAcat = 'H:\Downloads\svmForMultilabel\\Author_8area.txt'

Acat = pd.read_csv(locationAcat,index_col=0,names=[1,0], header=None, delim_whitespace=True)

resultLocationAll = 'H:\\Downloads\\svmForMultilabel\\AMiner_LINE12.txt'

AMiner_LINE1 = pd.read_csv(resultLocationAll, header=None, delim_whitespace=True)



n = AMiner_LINE1.columns.values
n=[x+1 for x in n]
AMiner_LINE1.columns = n

n = LINE1paper.columns.values
n=[x+256 for x in n]
LINE1paper.columns = n



locationIndex = 'H:\\Downloads\\svmForMultilabel\\index.txt'

index = pd.read_csv(locationIndex, header=None, delim_whitespace=True)


indexAMiner_LINE1 =  pd.concat([index,AMiner_LINE1], axis=1).set_index(0)



combined = pd.concat([indexAMiner_LINE1, LINE1paper], axis=1)




combinedLo = 'H:\\Downloads\\lineForHetero\\103024LINE12anpPosition.txt'
combined.to_csv(combinedLo,sep=' ',header=False,index=False,decimal='.')



result = pd.concat([combined,Acat],axis=1,join="inner")


group = result.reset_index().filter([0], axis=1)
group.index+=1
groupLocation = 'H:\\Downloads\\lineForHetero\\testSVM\\group12Position.txt'
group.to_csv(groupLocation,sep=' ',header=False,index=True,decimal='.')
