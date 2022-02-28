#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:25:26 2021

@author: nurbuke
"""


import pandas as pd 

data = pd.read_csv("train.csv") 

show_df = data[['TimeSpent', 'IsFulfilled']]


fulfilledFalse = show_df[show_df['IsFulfilled'] == 0]
fulfilledTrue = show_df[show_df['IsFulfilled'] == 1]


listof_count = [0,0,0,0,0]
for i,  row in  fulfilledTrue.iterrows():
    value_ = int(row['TimeSpent'])
    if(value_<= 30):
        listof_count[0] = listof_count[0] + 1
    elif(value_<= 60):
        listof_count[1] = listof_count[1] + 1
    elif(value_<= 120):
        listof_count[2] = listof_count[2] + 1
    elif(value_<= 180):
        listof_count[3] = listof_count[3] + 1
    else:
        listof_count[3] = listof_count[3] + 1
        
        
lst2 = ["<=30", "<=60", "<=120", "<=180", "180+"] 
  
df = pd.DataFrame(list(zip( lst2,listof_count )),  columns =['Zaman Aralık', 'Count']) 
        
df.plot(kind='bar',x='Zaman Aralık',y='Count',label="1")  

listof_count_false = [0,0,0,0,0]
for i,  row in  fulfilledFalse.iterrows():
    value_ = int(row['TimeSpent'])
    if(value_<= 30):
        listof_count_false[0] = listof_count_false[0] + 1
    elif(value_<= 60):
        listof_count_false[1] = listof_count_false[1] + 1
    elif(value_<= 120):
        listof_count_false[2] = listof_count_false[2] + 1
    elif(value_<= 180):
        listof_count_false[3] = listof_count_false[3] + 1
    else:
        listof_count_false[3] = listof_count_false[3] + 1
        
  

df_1 = pd.DataFrame(list(zip( lst2,listof_count_false )),  columns =['Zaman Aralık', 'Count']) 
        
df_1.plot(kind='bar',x='Zaman Aralık',y='Count',color='red',label="0")  


colors = ['b', 'g', 'r', 'c', 'm', 'y']

################
import matplotlib.pyplot as plt
import pandas as pd

ax = plt.gca()
# df.plot(x ='Zaman Aralık', y='Count', kind = 'pie',ax=ax,labels = lst2, colors = colors)
df.plot(kind='bar',x='Zaman Aralık',y='Count',ax=ax, label="1")  
df_1.plot(kind='bar',x='Zaman Aralık',y='Count',color='red',ax=ax,label="0")  


plt.show()


