# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import pandas as pd

locationLINE1 = 'H:\\Downloads\\testHetero\\LinuxLINE\\vec_2nd_wo_norm.txt'

locationAcat = 'H:\\Downloads\\testSVM\\Author_8area.txt'

# LINE1 = pd.read_csv(locationLINE1, index_col=0, header=None, delim_whitespace=True)

LINE1 = pd.read_csv(locationLINE1, header=None, delim_whitespace=True)
Acat = pd.read_csv(locationAcat,index_col=0,names=[1,0], header=None, delim_whitespace=True)

LINE1.set_index(0, inplace=True)

result = pd.concat([Acat,LINE1],axis=1,join="inner")

AMiner_LINE1 = result.drop(0, axis=1)


resultLocation1 = 'H:\\Downloads\\testHetero\\LinuxLINE\\AMiner_LINE2.txt'
AMiner_LINE1.to_csv(resultLocation1,sep=' ',header=False,index=False,decimal='.')

group = result.reset_index().filter([0], axis=1)
group.index+=1
groupLocation = 'H:\\Downloads\\testHetero\\LinuxLINE\\group.txt'
group.to_csv(groupLocation,sep=' ',header=False,index=True,decimal='.')

index=result.reset_index().filter(['index'],axis=1)
index.to_csv('H:\\Downloads\\testHetero\\LinuxLINE\\index.txt',sep=' ',header=False,index=False,decimal='.')
