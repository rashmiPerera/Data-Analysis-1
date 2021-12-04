#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as no
import plotly.express as px
import plotly.graph_objs as go
dataset=pd.read_csv("C:/Users/DELL/Desktop/aa.csv")
dataset.head()


# In[2]:


x=dataset["date"]
y=dataset["productB"]
fig=px.line(dataset,x,y)
fig.show()


# In[3]:


fig=go.Figure()

fig.add_trace(go.Scatter(y=dataset.productB, x=dataset.date))
fig.add_trace(go.Scatter(y=dataset.productC, x=dataset.date))

fig.show()


# In[6]:


fig=go.Figure()
fig.add_trace(go.Scatter(y=dataset.productB,x=dataset.date,
                         mode='lines',
                         name='productB'))
fig.add_trace(go.Scatter(y=dataset.productC,x=dataset.date,
                         mode='lines+markers',
                         name='productC'))

fig.show()


# In[ ]:




