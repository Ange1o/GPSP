# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:44:03 2017

@author: wd1u16
"""


import pandas as pd
locationLINE1 = 'H:\pte\myPTE\\svmForMultilabel\\A2A.txt'
locationLINE2 = 'H:\pte\myPTE\\svmForMultilabel\\A2P.txt'

LINE1 = pd.read_csv(locationLINE1, header=None, delim_whitespace=True)
LINE2 = pd.read_csv(locationLINE2, header=None, delim_whitespace=True)

LINE1.set_index(0, inplace=True)
LINE2.set_index(0, inplace=True)

n = LINE1.columns.values
n=[x+128 for x in n]

LINE2.columns = n

LINE12 = pd.concat([LINE1, LINE2], axis=1)


resultLocationAll = 'H:\pte\myPTE\\svmForMultilabel\\PTE.txt'
LINE12.to_csv(resultLocationAll,sep=' ',header=False,index=True,decimal='.')
