#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:47:24 2021

@author: nurbuke
"""


import pandas as pd 

data = pd.read_csv("train.csv") 

show_df = data[['ServiceId', 'Price', 'IsFulfilled']]


# kampanya = data['ServiceId']
# a = list(kampanya)
# value = max(a)



service_1 = show_df[show_df['ServiceId'] == 1]
service_1 = service_1[service_1['IsFulfilled'] == 0]


listof_count = [0,0,0,0,0,0]
for i,  row in  service_1.iterrows():
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
        
df.plot(kind='bar',x='Fiyat Aralık',y='Count')  