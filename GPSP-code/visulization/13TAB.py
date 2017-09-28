# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:21:33 2017

@author: wd1u16
"""

import pandas as pd


LINEpath = "H:/visulization/paper/LINE12paper.txt"

line = pd.read_csv(LINEpath, header=None, delim_whitespace=True)


#line = line[1]


line.to_csv(LINEpath,sep='\t',header=False,index=False)


