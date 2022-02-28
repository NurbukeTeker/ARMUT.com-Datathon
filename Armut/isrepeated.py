import pandas as pd 

data = pd.read_csv("train.csv") 

show_df = data[['IsRepeat', 'IsFulfilled']]


# kampanya = data['CampaignId']
# a = list(kampanya)
# value = max(a)



fulfilledFalse = show_df[show_df['IsFulfilled'] == 0]
fulfilledTrue = show_df[show_df['IsFulfilled'] == 1]

# result = fulfilledTrue.set_index(["CampaignId", "IsFulfilled"]).count(level="CampaignId")
dups_true = fulfilledTrue.pivot_table(index=['IsRepeat'], aggfunc='size').reset_index()
dups_true.rename( columns={0:'Count'}, inplace=True )



# dups_color = dups_color.to_frame()

dups_true.plot(x ='IsRepeat', y='Count', kind = 'scatter')	

dups_true.plot(kind='bar',x='IsRepeat',y='Count',label="1")

#########
#False

dups_false = fulfilledFalse.pivot_table(index=['IsRepeat'], aggfunc='size').reset_index()
dups_false.rename( columns={0:'Count'}, inplace=True )

dups_false.plot(x ='IsRepeat', y='Count', kind = 'scatter')	

dups_false.plot(kind='bar',x='IsRepeat',y='Count',color='red',label="0")




################
import matplotlib.pyplot as plt
import pandas as pd

ax = plt.gca()

#dups_color.plot(kind='line',x='CampaignId',y='Count',ax=ax)

dups_true.plot(x ='IsRepeat', y='Count', kind = 'bar',ax=ax,label="1")	
dups_false.plot(x ='IsRepeat', y='Count', kind = 'bar',color='red',ax=ax,label="0")	


plt.show()


