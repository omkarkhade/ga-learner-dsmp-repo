# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path,sep=',')
#path of the data file- path
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
plt.bar(gender_count.index,gender_count.values)
plt.show()
#Code starts here 





# --------------
#Code starts here
alignment =  data['Alignment'].value_counts()
plt.pie(alignment)


# --------------
#Code starts here
sc_df =data[['Strength','Combat']]
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance/(sc_strength * sc_combat)
##############
ic_df =data[['Intelligence','Combat']]
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance/(ic_intelligence * ic_combat)
print(sc_pearson)
print(ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
super_best = data[data['Total']> total_high]
super_best_names = list(super_best['Name'].values)

super_best_names = list(super_best['Name'].values)

print(super_best_names)
##################################



# --------------
#Code starts here
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,10))
data['Intelligence'].plot(kind='bar', ax=ax_1)
ax_1.set_title('Intelligence')

data['Speed'].plot(kind='bar', ax=ax_2)
ax_1.set_title('Speed')


data['Power'].plot(kind='bar', ax=ax_3)
ax_1.set_title('Power')


