# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:16:05 2017

@author: wd1u16
"""


import pandas as pd

location = 'H:\\Downloads\\lineForHomo\\AMinerCoauthor.txt'

AMinerCoauthor = pd.read_csv(location, header=None, delim_whitespace=True)

order = [1,0,2]

AMinerCoauthorReverse = AMinerCoauthor[order]


AMinerCoauthorReverse.columns = [0,1,2]


frames = [AMinerCoauthor,AMinerCoauthorReverse]
AMinerCoauthor_Undirected = pd.concat(frames)


resultLocation =  'H:\\Downloads\\lineForHomo\\AMinerCoauthorUndirected.txt'
AMinerCoauthor_Undirected.to_csv(resultLocation,sep=' ',header=False,index=False,decimal='.')