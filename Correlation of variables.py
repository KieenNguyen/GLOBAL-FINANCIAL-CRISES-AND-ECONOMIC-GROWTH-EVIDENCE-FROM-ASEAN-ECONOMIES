#!/usr/bin/env python
# coding: utf-8

# In[56]:


#import libaries 
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

#Adjust the size of figure 
from matplotlib.pyplot import figure
plt.rcParams["figure.figsize"] = (20,10)


# In[57]:


data= pd.read_excel('Data_group3.xlsx')
data


# In[58]:


#Xoá dữ liệu thùa: 
for col in data.columns:
    if 'Unnamed' in col:
        del data[col]


# In[59]:


data


# In[60]:


#Kiểm tra kiểu dữ liệu:
data.info()


# In[61]:


#Descriptive statistic:
data.describe()


# In[62]:


#Đổi kiểu dữ liệu thành float:
header = data.columns.drop(['code','year ']).to_series()
for name in header:
    data[name]=data[name].apply(float)


# In[64]:


data2=data.drop(['code','year '],1)
data2


# In[65]:


#Correlation Martrix:
data2.corr() 


# In[66]:


data1=data.drop(['fdi','year '],1)
matrix=data1.corr()
sns.heatmap(matrix, annot = True)
plt.show()


# In[67]:


data.columns


# In[68]:


data['fdi_new']= data['fdi']/100
data['gdp_new']=data['gdp']/100
data


# In[ ]:




