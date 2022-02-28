import pandas as pd 

data = pd.read_csv("train.csv") 

show_df = data[['CampaignId', 'IsFulfilled']]


# kampanya = data['CampaignId']
# a = list(kampanya)
# value = max(a)



fulfilledFalse = show_df[show_df['IsFulfilled'] == 0]
fulfilledTrue = show_df[show_df['IsFulfilled'] == 1]

# result = fulfilledTrue.set_index(["CampaignId", "IsFulfilled"]).count(level="CampaignId")
dups_true = fulfilledTrue.pivot_table(index=['CampaignId'], aggfunc='size').reset_index()
dups_true.rename( columns={0:'Count'}, inplace=True )



# dups_color = dups_color.to_frame()

# dups_true.plot(x ='CampaignId', y='Count', kind = 'scatter')	

dups_true.plot(kind='bar',x='CampaignId',y='Count', label="1")

#########3
#False

# result = fulfilledTrue.set_index(["CampaignId", "IsFulfilled"]).count(level="CampaignId")
dups_false = fulfilledFalse.pivot_table(index=['CampaignId'], aggfunc='size').reset_index()
dups_false.rename( columns={0:'Count'}, inplace=True )

# dups_false.plot(x ='CampaignId', y='Count', kind = 'scatter')	

dups_false.plot(kind='bar',x='CampaignId',y='Count',color='red',label="0")




################
import matplotlib.pyplot as plt
import pandas as pd

ax = plt.gca()

#dups_color.plot(kind='line',x='CampaignId',y='Count',ax=ax)

dups_true.plot(x ='CampaignId', y='Count', kind = 'bar',ax=ax,label="1")	
dups_false.plot(x ='CampaignId', y='Count', kind = 'bar',color='red',ax=ax,label="0")	


plt.show()

################

#Subtraction of true&false
df_campaignid = dups_true['CampaignId']
df_sub = dups_true.subtract(dups_false) 

df_sub['CampaignId'] = df_campaignid
#####################################################
import matplotlib.pyplot as plt
import pandas as pd

ax = plt.gca()

#dups_color.plot(kind='line',x='CampaignId',y='Count',ax=ax)

dups_true.plot(x ='CampaignId', y='Count', kind = 'bar',ax=ax)	
dups_false.plot(x ='CampaignId', y='Count', kind = 'bar',color='red',ax=ax)	
df_sub.plot(x ='CampaignId', y='Count', kind = 'bar',color='green',ax=ax)	


plt.show()
