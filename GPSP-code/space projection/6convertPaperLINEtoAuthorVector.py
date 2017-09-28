# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:06:45 2017

@author: wd1u16
"""

import pandas as pd

locationA2P = 'H:\\Downloads\\lineForHetero\\dataset\\AMiner-Author2Paper.txt'

a2p = pd.read_csv(locationA2P, header=None, delim_whitespace=True)

a2p = a2p.drop(0,1)

a2p=a2p.sort_values(by=1)

a2pNetwork = a2p.reset_index().drop('index',1)

lo = 'H:\\Downloads\\lineForHetero\\homoAuthorIndex.txt'

homo=pd.read_csv(lo,header=None, delim_whitespace=True)

homolist = homo[0].tolist()

results = a2p[a2p[1].isin(homolist)].reset_index().drop('index',1)

authorframe=results[1].drop_duplicates().reset_index().drop('index',1)




locationLINE1 = 'H:\\Downloads\\lineForHetero\\LINE12.txt'

LINE1 = pd.read_csv(locationLINE1, header=None, delim_whitespace=True)

paperlist = results[2].drop_duplicates().tolist()

LINE1s=LINE1[LINE1[0].isin(paperlist)].set_index(0)




a=results[1]
p=results[2]
o=results[3]

result = []
list=[]
previous=0

for i in range(0,len(a)):
    current = a[i]
    if current == previous:
        list.append(p[i])
    else:
        previous=current
        result.append(list)
        list=[]
        list.append(p[i])
result.append(list)

result.pop(0)





position = []
list=[]
previous=0

for i in range(0,len(a)):
    current = a[i]
    if current == previous:
        list.append(o[i])
    else:
        previous=current
        position.append(list)
        list=[]
        list.append(o[i])
position.append(list)

position.pop(0)



finalResult=pd.DataFrame()
df = pd.DataFrame()

for i in range(0,len(result)):
    list=result[i]
    positions=position[i]
    for j in range(0,len(list)):
        item = list[j]
        p=positions[j]
        try:
            temp=LINE1s.loc[item]/p
            df=df.append(temp)
        except:
            pass
    if df.shape[0]>1:
        avg = df.mean(0)
    elif df.shape[0]==1:
        avg=df
    else:
        avg=LINE1s.loc[12]*0
    finalResult= finalResult.append(avg,ignore_index=True)
    df = pd.DataFrame()
    if i%1000==0:
        print(i)
   
    
finalConcat = pd.concat([authorframe,finalResult],axis=1)

lo = 'H:\\Downloads\\lineForHetero\\LINE12paperPosition.txt'

finalConcat.to_csv(lo,sep=' ',header=False,index=False,decimal='.')