import pandas as pd
# import numpy as np
import seaborn 
import matplotlib.pyplot as plot


import time
from datetime import datetime

# df.plot(LotArea ='LotArea ', SalePrice='SalePrice', style='o')
# plt.savefig("pandas_scatter_plot_01.png", bbox_inches='tight', dpi=100)


data = pd.read_csv('lovoo_v3_users_api-results.csv')
data



# df = pd.DataFrame(data=data, columns=['Statut','Pricing'])
# # df["Pricing"] = df["Pricing"].astype(str).astype(float)
# # df['Pricing'] = pd.to_numeric(df['Pricing'],errors = 'coerce') 
# print(df.dtypes)
# print(df)
# seaborn.relplot(x=df["Statut"], y=df["Pricing"], s = 100, height=30)
# seaborn.relplot(x=df["Statut"], y=df["Pricing"], kind='line', height=10)

# seaborn.relplot(x=df["Statut"], y=df["Pricing"], s = 100, height=10)

# plot.show(); 
# corr=df.corr()
# f, ax = plot.subplots(figsize=(20,5))
# seaborn.heatmap(corr, annot=True, ax =ax)
# plot.savefig('heatmapEX1.png')
# # df = pd.DataFrame(data=data, columns=['LotArea','SalePrice'])
# # df[(df['SalePrice'] < 500000) & (df['LotArea'] < 20000)]
# # df.plot.scatter(x='LotArea', y='SalePrice', title= "");

# df[(df['SalePrice'] < 500000) & (df['LotArea'] < 20000)].plot.scatter(x = 'SalePrice', y = 'LotArea' , s = 100);
# # seaborn.regplot(x=df["SalePrice"], y=df["LotArea"], s=100)
# plot.show(); 

# df = pd.DataFrame(data=data)
# df = pd.DataFrame(data=data, columns=['counts_profileVisits','lastOnlineDate','lastOnlineTime'])
# df['new_time']=datetime.fromtimestamp()df['lastOnlineTime'][df['lastOnlineTime']]
# df['lastOnlineTime'] = pd.to_datetime(df['lastOnlineTime'], unit='s')
# print(df)
# # df['lastOnlineDate'] = pd.to_datetime(df["lastOnlineDate"], infer_datetime_format=True)
# print(datetime.fromtimestamp(1429994606.0))


# df

# seaborn.relplot(x=value, y=df["item_price"], s=50, height=10)
# plot.show(); 


