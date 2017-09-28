# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 21:07:39 2017

@author: wd1u16
"""


import pandas as pd

lo1 = 'H:\Downloads\lineForHomo\paper\\LINE1anp.txt'

lo2 = 'H:\Downloads\lineForHomo\paper\\LINE2anp.txt'
lo12 = 'H:\Downloads\lineForHomo\paper\\LINE12anp.txt'

LINE1paper = pd.read_csv(lo1, header=None,index_col=0, delim_whitespace=True)
LINE2paper = pd.read_csv(lo2, header=None,index_col=0, delim_whitespace=True)
LINE12paper = pd.read_csv(lo12, header=None,index_col=0, delim_whitespace=True)


range1 = list(range(128,256))
range2=range1
range12 = list(range(256,512))


paper1=LINE1paper.filter(range1, axis=1)
paper2=LINE2paper.filter(range2, axis=1)
paper12=LINE12paper.filter(range12, axis=1)



loc1='H:\Downloads\lineForHomo\paper\\LINE1paper.txt'
loc2='H:\Downloads\lineForHomo\paper\\LINE2paper.txt'
loc12='H:\Downloads\lineForHomo\paper\\LINE12paper.txt'


paper1.to_csv(loc1,sep=' ',header=False,index=False,decimal='.')

paper2.to_csv(loc2,sep=' ',header=False,index=False,decimal='.')

paper12.to_csv(loc12,sep=' ',header=False,index=False,decimal='.')