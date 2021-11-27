#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import cufflinks as cf
import chart_studio.plotly as py
import plotly.tools as tls
import plotly.offline as po
import plotly.graph_objs as go

dataset=pd.read_excel("C:/Users/DELL/Desktop/Analysis and Visualization Basics.xlsx")
dataset.head()
print(dataset)


# In[2]:


dataset[['date','product B','product C']].describe()


# In[3]:


#range_productB
dataset['product B'].max()-dataset['product B'].min()


# In[4]:


#range_productC
dataset['product C'].max()-dataset['product C'].min()


# In[5]:


#variance_productB
dataset['product B'].var()


# In[6]:


#variance_productC
dataset['product C'].var()


# In[7]:


#squreRoot_productB
import math
from math import sqrt
math.sqrt(dataset['product B'].var())


# In[8]:


#squreRoot_productB
import math
from math import sqrt
math.sqrt(dataset['product C'].var())


# In[ ]:





# In[ ]:




