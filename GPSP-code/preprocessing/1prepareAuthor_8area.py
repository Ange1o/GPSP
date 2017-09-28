# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

locationAID = 'H:\\Downloads\\lineForHomo\\preprocessing\\AMiner_Author_Modified.txt'
namesAID = ['AID']

locationAC = 'H:\\Downloads\\lineForHomo\\preprocessing\\googlescholar.8area.author.label.txt'
namesAC = ['ACAT']


AuthorIDd = pd.read_csv(locationAID, index_col=1, names=namesAID, header=None, delim_whitespace=True,  encoding="ISO-8859-1")
AuthorCat = pd.read_csv(locationAC,index_col=0, names=namesAC, header=None, delim_whitespace=True,  encoding="ISO-8859-1")

AuthorID = AuthorIDd.reset_index().drop_duplicates(subset='index', keep= False).set_index('index')

result = pd.concat([AuthorCat,AuthorID], axis=1,join="inner")

result = result[['AID','ACAT']]

resultLocation = 'H:\\Downloads\\lineForHomo\\preprocessing\\result.txt'
result.to_csv(resultLocation,header=False,index=False,decimal='.')