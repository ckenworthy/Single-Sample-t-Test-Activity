#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy import stats


# In[6]:


hybrid2013=pd.read_csv(r"C:\Users\camke\OneDrive\Documents\Copy of hybrid2013.csv")


# # Test for Normality
# 

# In[7]:


hybrid2013['mpg'].hist()


# # Single Sample t-Test

# In[8]:


stats.ttest_1samp(hybrid2013['mpg'], 40)


# # Check the Population Mean

# In[9]:


hybrid2013.mpg.mean()


# In[ ]:




