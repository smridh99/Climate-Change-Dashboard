#!/usr/bin/env python
# coding: utf-8

# In[57]:


import matplotlib
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import numpy as np


#load csv file

rawdf = pd.read_csv("owid-co2-data.csv")

# Droping ISO_CODE with no regional code

df = rawdf.dropna(subset=['iso_code'])




# Create figure with 10X10 dimensions and 4 subplots compatible

fig = plt.figure(figsize = (10,10))

#  Line Graph top_left



# # Labelling
top_left = fig.add_subplot(2,2,1)
top_left.set_xlabel("Year")
top_left.set_ylabel("Emissions (millions of tons)")
top_left.set_title('Global GHG Emissions')

# Data Extraction: InWORLD
inworld = df[df.country == 'World']
xval1 = pd.Series(inworld['year'])
yval1 = pd.Series(inworld['total_ghg'])
top_left.plot(xval1,yval1, color='black')





# Line Graph top_right

# # Labelling
top_right = fig.add_subplot(2,2,2)
top_right.set_xlabel("Year")
top_right.set_ylabel('CO2 Emissions (tons per year)')
top_right.set_title('Top Emitters per Capita')

# #Data filtering: ffill, sorting by 2018 - 1990 and then top 5
dataset = df.ffill()
dataset = dataset.dropna(subset =['ghg_per_capita'])
dataset = dataset[dataset.year >= 1990]


d1 = dataset[dataset.country =='Guyana']
d2 = dataset[dataset.country =='Brunei']
d3 = dataset[dataset.country =='Qatar']
d4 = dataset[dataset.country =='Bahrain']
d5 = dataset[dataset.country =='Botswana']

# # Plotting the data

# ## 1st: Guyana
xzim = pd.Series(d1['year'])
yzim = pd.Series(d1['ghg_per_capita'])
top_right.plot(xzim,yzim, label= 'Guyana')
top_right.legend(loc="upper right")

# ## 2nd: Brunei
xsyr = pd.Series(d2['year'])
ysyr = pd.Series(d2['ghg_per_capita'])
top_right.plot(xsyr,ysyr, label= 'Brunei')
top_right.legend(loc="upper right")

# ## 3rd: Qatar
xmau = pd.Series(d3['year'])
ymau = pd.Series(d3['ghg_per_capita'])
top_right.plot(xmau,ymau, label= 'Qatar')
top_right.legend(loc="upper right")

# ## 4th: Bahrain
xswe = pd.Series(d4['year'])
yswe = pd.Series(d4['ghg_per_capita'])
top_right.plot(xswe,yswe, label= 'Bahrain')
top_right.legend(loc="upper right")

# ## 5th: Botswana
xels = pd.Series(d5['year'])
yels = pd.Series(d5['ghg_per_capita'])
top_right.plot(xels,yels, label= 'Botswana')
top_right.legend(loc="upper right")




# Bar Graph bottom_left

# # Labelling
down_left = fig.add_subplot(2,2,3)
down_left.set_xlabel(" ")
down_left.set_ylabel('CO2 Per Capita (tons per year)')
down_left.set_title('2018 Regional CO2 Emissions')

# Data Extraction
data6 = rawdf.ffill()
data6 = data6[data6.year == 2018]

af = data6[(data6.country == 'Africa') | (data6.country == 'Asia') | (data6.country == 'Oceania') | (data6.country == 'North America') | (data6.country == 'South America')]
countries = af[['country']]
af = af[['co2_per_capita']]

# Plotting graph
bar_graph = af.plot.bar(ax=down_left,color='black')
bar_graph.set_xticklabels(['Africa',"Asia","Oceania","North America","South America"])
bg= down_left.legend(['2018'],loc="upper left")
bg.set_title(title='Year')




# HISTOGRAM bottom_RIGHT

## Labelling
down_right = fig.add_subplot(2,2,4)
down_right.set_xlabel("CO2 Emissions (tons per year per person)")
down_right.set_ylabel('Number of Countries')
down_right.set_title('CO2 Emissions per Capita')

## Data Extraction
hd = rawdf.dropna(subset =['iso_code'])
hd = rawdf.ffill()
hd = hd[(hd.country != 'World') & (hd.year == 2018)]
hd = hd[['co2_per_capita']]
# his_data = hd['co2_per_capita'].value_counts()

down_right.hist(hd,bins=50)



## Saving the graph

fig.savefig("vizoutput", dpi=300)


# In[ ]:




