import pandas as pd 
import numpy as np
# criar um datafrsme 

marketing = pd.read_csv('marketing.csv', delimiter=',')

print(marketing.head(5))


print(marketing.describe(include='all'))

print(marketing['converted'].head(5))

#conversao 
marketing['converted']=marketing['converted'].astype('bool')
print(marketing['converted'].astype('bool'))
#marketing=['is_house_Ads']=np.where(marketing['marketing_channel'] == 'House Ads',True, False)