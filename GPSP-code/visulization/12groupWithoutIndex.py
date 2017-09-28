# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:21:33 2017

@author: wd1u16
"""

import pandas as pd


LINEpath = "H:\\visulization\\HNE\\group.txt"

line = pd.read_csv(LINEpath,index_col=0, header=None, delim_whitespace=True)

line.to_csv(LINEpath,header=False,index=False)


