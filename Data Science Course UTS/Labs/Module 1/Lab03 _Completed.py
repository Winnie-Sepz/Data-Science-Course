#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Load data from 'https://coded2.herokuapp.com/datavizpandas/london2018.csv'
# and print it
# First import libraries numpy, and pandas and matplotlib.pyplot
import numpy as np
import pandas as pd

# Load data from the above url using pandas read_csv
weather = pd.read_csv('https://coded2.herokuapp.com/datavizpandas/london2018.csv')
# Print the top 10 rows
print(weather)


# <div>
# <img src=https://www.institutedata.com/wp-content/uploads/2019/10/iod_h_tp_primary_c.svg width="300">
# </div>
# 
# # Python - Lab 3
# 
# ## Learning objectives
# 
# This lab demonstrates examples of:
# 
# 1. Using the `pandas` module for data import and analysis
# 2. Using `matplotlib` and `seaborn` modules for data visualisation 
# 
# ## Instructions
# 
# 1. Replace ??? with the appropriate code
# 2. Press Shift + Enter to execute cell

# In[ ]:


# Use pandas describe() function to describe the data loaded above
get_ipython().run_line_magic('pinfo2', '')


# In[ ]:


# Plt temprture min and max
weather.plot(y=[???], x='Month')


# In[ ]:


# Plot the rain as above
weather.???


# In[ ]:


# Plot the sun column


# In[10]:


# Load the iris dataset
# Import numpy and pandas
import numpy as pandas
# Import seaborn library
import seaborn as sns
# Import load_iris
from sklearn.datasets import load_iris
# Load the dataset
dataset=load_iris()
# Place in pandas dataframe
data=pd.DataFrame(dataset["data"],columns=["Petal length","Petal Width","Sepal Length","Sepal Width"])
data["Species"]=dataset["target"]
data["Species"]=data["Species"].apply(lambda x: dataset["target_names"][x])
# Print top 10 rows
print(data.head(10))
df.column_name.describe()


# In[15]:


# Describe the dataframe
print(data.describe())


# In[8]:


# use seaborn paitplot function to plot relationship between variables
sns.pairplot(data, hue="Species")


# In[ ]:




