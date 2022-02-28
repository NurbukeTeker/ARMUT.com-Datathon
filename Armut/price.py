#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:25:26 2021

@author: nurbuke
"""


import pandas as pd 

data = pd.read_csv("train.csv") 

show_df = data[['Price', 'IsFulfilled']]


fulfilledFalse = show_df[show_df['IsFulfilled'] == 0]
fulfilledTrue = show_df[show_df['IsFulfilled'] == 1]


listof_count = [0,0,0,0,0,0]
for i,  row in  fulfilledTrue.iterrows():
    value_ = int(row['Price'])
    if(0<value_<10):
        listof_count[0] = listof_count[0] + 1
    elif(10<value_<20):
        listof_count[1] = listof_count[1] + 1
    elif(20<value_<30):
        listof_count[2] = listof_count[2] + 1
    elif(30<value_<40):
        listof_count[3] = listof_count[3] + 1
    elif(40<value_<50):
        listof_count[4] = listof_count[4] + 1
    elif(50<value_<60):
        listof_count[5] = listof_count[5] + 1
      
      
          
lst2 = ["0-10", "10-20", "20-30", "30-40", "40-50", "50-60"] 
  
df = pd.DataFrame(list(zip( lst2,listof_count )),  columns =['Fiyat Aralık', 'Count']) 
        
df.plot(kind='bar',x='Fiyat Aralık',y='Count' ,label="1")  


listof_count_false = [0,0,0,0,0,0]
for i,  row in  fulfilledFalse.iterrows():
    value_ = int(row['Price'])
    if(0<value_<10):
        listof_count_false[0] = listof_count_false[0] + 1
    elif(10<value_<20):
        listof_count_false[1] = listof_count_false[1] + 1
    elif(20<value_<30):
        listof_count_false[2] = listof_count_false[2] + 1
    elif(30<value_<40):
        listof_count_false[3] = listof_count_false[3] + 1
    elif(40<value_<50):
        listof_count_false[4] = listof_count_false[4] + 1
    elif(50<value_<60):
        listof_count_false[5] = listof_count_false[5] + 1
      
  

df_1 = pd.DataFrame(list(zip( lst2,listof_count_false )),  columns =['Fiyat Aralık', 'Count']) 
        
df_1.plot(kind='bar',x='Fiyat Aralık',y='Count' ,label="0",color='red')  




################
import matplotlib.pyplot as plt
import pandas as pd

ax = plt.gca()

#dups_color.plot(kind='line',x='CampaignId',y='Count',ax=ax)

df.plot(x ='Fiyat Aralık', y='Count', kind = 'bar',ax=ax,label="1")	
df_1.plot(x ='Fiyat Aralık', y='Count', kind = 'bar',color='red',ax=ax,label="0")	


plt.show()


