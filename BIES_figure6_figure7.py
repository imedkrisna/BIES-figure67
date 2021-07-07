#!/usr/bin/env python
# coding: utf-8
# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))
path = r"C:\Users\imedk\OneDrive - Australian National University\ANU Skul\aaa paper 1\BIES_FINAL"
os.chdir(path)

# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))


# In[1]:


# Data source
source='https://data.imf.org/?sk=F8032E80-B36C-43B1-AC26-493C5B1CD33B'
print('Accessed 07/07/2021 from IMF website -> '+source)


# In[2]:


# Reading the data from my github. Downloaded from
import pandas as pd

url='https://github.com/imedkrisna/BIES-figure67/raw/main/FD%20Index%20Database%20(Excel).xlsx'
df=pd.read_excel(url)
df.head()


# In[3]:


# Data for figure 6
FD=df.query('code=="IDN" or code=="USA" or code=="CHN" or code=="SGP" or code=="MYS" or code=="THA" or code=="VNM"')


# In[4]:


# Plotting figure 6
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="white")

# Plot the responses for different events and regions
sns.lineplot(x="year", y="FD",
             hue="country", style="country",
             data=FD)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('Figure 6. Financial Development Index for Seven Select Economies, 1980–2018')
plt.savefig('fig6.png')


# In[5]:


# Creating dataset for figure 7
FDID=df.query('code=="IDN"')
a=FDID.melt(id_vars=['code','year'], value_vars=['FID'])
b=FDID.melt(id_vars=['code','year'], value_vars=['FIA'])
c=FDID.melt(id_vars=['code','year'], value_vars=['FIE'])
d=FDID.melt(id_vars=['code','year'], value_vars=['FMD'])
e=FDID.melt(id_vars=['code','year'], value_vars=['FMA'])
f=FDID.melt(id_vars=['code','year'], value_vars=['FME'])
FDII=pd.concat([a,b,c])
FDMM=pd.concat([d,e,f])


# In[6]:


# creating figure 7 in a subplot
fig, axes = plt.subplots(1, 2, figsize=(10,5))
fig.suptitle('Figure 7. Indonesian Financial Institution Index (LHS) and Financial Market Index (RHS), 1980–2018')
sns.lineplot(ax=axes[0],x="year", y="value",
             hue="variable", style="variable",
             data=FDII,legend=False)
axes[0].set_title('Financial Institution')

# Charmander
sns.lineplot(ax=axes[1],x="year", y="value",
             hue="variable", style="variable",
             data=FDMM)
axes[1].set_title('Financial Market')
plt.legend(labels=['Depth','Access','Efficiency'],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.savefig('fig7.png')


# In[7]:


# figure 7 left
sns.lineplot(x="year", y="value",
             hue="variable", style="variable",
             data=FDII)
plt.legend(labels=['Depth','Access','Efficiency'],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[8]:


#figure 7 right
sns.lineplot(x="year", y="value",
             hue="variable", style="variable",
             data=FDMM)
plt.legend(labels=['Depth','Access','Efficiency'],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

