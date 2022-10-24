import streamlit as st
import numpy as np 
import time
import pandas as pd
# import numpy as np
import seaborn 
import matplotlib.pyplot as plot
from datetime import datetime


data = pd.read_csv('lovoo_v3_users_api-results.csv')
#import data
data


# 1/
df = pd.DataFrame(data=data, columns=['counts_kisses','counts_profileVisits'])
#initalisation taille
#arr = np.random.normal(1, 1, size=100)
# creation df
fig=seaborn.relplot(x=df["counts_kisses"], y=df["counts_profileVisits"], s = 100, height=10)
#affichage avec streamlit
st.pyplot(fig)




#2/
df = pd.DataFrame(data=data, columns=['counts_fans','counts_kisses'])
fig=seaborn.relplot(x=df["counts_fans"], y=df["counts_kisses"], s = 100, height=10)
st.pyplot(fig)





#3/
df = pd.DataFrame(data=data, columns=['counts_kisses','counts_profileVisits','counts_fans'])
corr=df.corr()
f, ax = plot.subplots(figsize=(20,5))
seaborn.heatmap(corr, annot=True, ax =ax)
fig=plot.savefig('heatmapEX1.png')
st.pyplot(fig)

#4/
df = pd.DataFrame(data=data, columns=['counts_pictures','counts_profileVisits'])
fig=seaborn.relplot(x=df["counts_pictures"], y=df["counts_profileVisits"], kind='line', height=10)
st.pyplot(fig)

#5/
df = pd.DataFrame(data=data, columns=['counts_profileVisits','counts_pictures']) 
# df[(df['counts_pictures'] < 15) ].plot.scatter(x = 'counts_pictures', y = 'counts_kisses');
fig=seaborn.catplot(x="counts_pictures", y="counts_profileVisits", data= df, kind="bar", height=10)
st.pyplot(fig)

#6/
df = pd.DataFrame(data=data, columns=['counts_pictures','counts_kisses'])
fig=seaborn.relplot(x=df["counts_pictures"], y=df["counts_kisses"],kind='line',height=10)
st.pyplot(fig)

# #7/
# print("probleme")
# df = pd.DataFrame(data=data, columns=['counts_profileVisits','counts_pictures'])
# df["counts_pictures"].replace({0: "peu", 1: "peu",2: "peu",3: "beaucoup",4:"beaucoup",5: "beaucoup",6:"beaucoup",7: "beaucoup",8:"beaucoup",9: "beaucoup",10:"beaucoup",11: "beaucoup",12:"beaucoup",13: "beaucoup",14:"beaucoup",15: "beaucoup",16:"beaucoup",17: "beaucoup",18:"beaucoup",19: "beaucoup",20:"beaucoup",21: "beaucoup",22:"beaucoup",23: "beaucoup",24:"beaucoup",25: "beaucoup",26:"beaucoup",27: "beaucoup",28:"beaucoup",29: "beaucoup",30:"beaucoup"}, inplace=True)
# fig=seaborn.boxplot(data=df, x="counts_profileVisits", y="counts_pictures",showfliers=False)
# st.pyplot(fig)


# #8/
# df = pd.DataFrame(data=data, columns=['counts_kisses','verified'])
# fig=seaborn.boxplot(data=df, x="verified", y="counts_kisses",showfliers=False)
# st.pyplot(fig)

#9/
df = pd.DataFrame(data=data, columns=['counts_details','counts_kisses'])
fig=seaborn.relplot(x=df["counts_details"], y=df["counts_kisses"],kind='line',height=10)
st.pyplot(fig)

#10/
df = pd.DataFrame(data=data, columns=['age','counts_kisses'])
df["age"].replace({27: 26}, inplace=True)
fig=seaborn.catplot(x="age", y="counts_kisses", data= df, kind="bar", height=10)
st.pyplot(fig)
#11/
df = pd.DataFrame(data=data, columns=['age','counts_profileVisits'])
df["age"].replace({27: 26}, inplace=True)
fig=seaborn.catplot(x="age", y="counts_profileVisits", data= df, kind="bar", height=10)
st.pyplot(fig)

#12/
df = pd.DataFrame(data=data, columns=['counts_kisses','counts_profileVisits','age','country','counts_details','counts_pictures','lang_count','verified','distance','counts_g'])
corr=df.corr()
f, ax = plot.subplots(figsize=(20,5))
seaborn.heatmap(corr, annot=True, ax =ax)
fig=plot.savefig('heatmapEX1.png')
st.pyplot(fig)

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()

# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
st.button("Re-run")
