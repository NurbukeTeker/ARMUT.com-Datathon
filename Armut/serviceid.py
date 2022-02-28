import pandas as pd 

data = pd.read_csv("train.csv") 

show_df = data[['ServiceId', 'IsFulfilled']]


kampanya = data['ServiceId']
a = list(kampanya)
value = max(a)



fulfilledFalse = show_df[show_df['IsFulfilled'] == 0]
fulfilledTrue = show_df[show_df['IsFulfilled'] == 1]

dups_true = fulfilledTrue.pivot_table(index=['ServiceId'], aggfunc='size').reset_index()
dups_true.rename( columns={0:'Count'}, inplace=True )

#############################################

lst2 = ["Categori0", "Categori1", "Categori2"] 
colors = ['m', 'b', 'r']


dups_true.plot(kind='bar',x='ServiceId',y='Count',label ="1")



import matplotlib.pyplot as plt
import pandas as pd

ax = plt.gca()
dups_true.plot(x ='ServiceId', y='Count', kind = 'pie',ax=ax,labels = lst2, colors = colors)	


plt.show()

###############################################


dups_true.plot(x ='ServiceId', y='Count', kind = 'bar')	


#########
#False

dups_false = fulfilledFalse.pivot_table(index=['ServiceId'], aggfunc='size').reset_index()
dups_false.rename( columns={0:'Count'}, inplace=True )

dups_false.plot(kind='bar',x='ServiceId',y='Count',color='red',label ="0")




################
import matplotlib.pyplot as plt
import pandas as pd

ax = plt.gca()


dups_true.plot(x ='ServiceId', y='Count', kind = 'bar',ax=ax,label ="1")	
dups_false.plot(x ='ServiceId', y='Count', kind = 'bar',color='red',ax=ax,label ="0")	


plt.show()


