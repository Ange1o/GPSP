# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:43:57 2017

paperNetwork


@author: wd1u16
"""



import pandas as pd

locationPaper = 'H:\\Downloads\\testHetero\\dataset\\AMiner-Paper.txt'

paper = pd.read_csv(locationPaper, header=None, delim_whitespace=True)

a = paper[0]
b = paper[1]

index = 0
ref = 0
result = []

for i in range (1,len(a)):
    if a[i] == '#index':
        index = b[i]
    else:
        ref = b[i]
        tup = (index,ref)
        result.append(tup)

paperFrame = pd.DataFrame(result)



c = paperFrame[0].to_frame(2)

paperNet = pd.concat([paperFrame, c], axis=1)

paperNet[2]=1


locationPaperNet = 'H:\\Downloads\\testHetero\\paperNetwork.txt'
paperFrame.to_csv(locationPaperNet,sep=' ',header=False,index=False,decimal='.')