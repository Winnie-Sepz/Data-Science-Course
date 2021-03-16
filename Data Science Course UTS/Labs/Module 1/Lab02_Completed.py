#!/usr/bin/env python
# coding: utf-8

# <div>
# <img src=https://www.institutedata.com/wp-content/uploads/2019/10/iod_h_tp_primary_c.svg width="300">
# </div>
# 
# # Python - Lab 2
# 
# ## Learning objectives
# 
# This lab demonstrates examples of:
# 
# 1. Using `numpy` and `matplotlib` modules
# 2. Plotting line, bar, and histogram charts using `matplotlib` 
# 3. Simple customisations when creating visualisations
# 
# ## Instructions
# 
# 1. Replace ??? with the appropriate code
# 2. Press Shift + Enter to execute cell

# In[11]:


# Practice the use of matplotlib
import numpy as np
import matplotlib.pyplot as plt
# Create a data set 
x = np.linspace(0, 10, 100)
# Print the data
print(x)
# Create a figure using plt.figure
fig = plt.figure()
# Plot the sine wave of x
sin= np.sin(x)
plt.plot(x,sin, '-')
# Plot the cosine wave of x
cos= np.cos(x)
plt.plot(x,cos, '-')


# In[28]:


# Create two arrays of 5 arbitrary numbers 
array1 = np.array([1,2,3,4,5])
array2 = np.array([7,9,2,6,8])
# Plot two bar charts using plt.bar and the arrays you've created above
# Label them "Example one" and "example two"
plt.bar(array1,array2, label="Example one")
plt.bar(array2,array1, label="Example two", color='g') #TODO
plt.legend()
# Label x axis "Bar number"
plt.xlabel('Bar number')
# Label y axis "Bar height"
plt.ylabel('Bar height')
# Set title "Bar Graph"
plt.title("Bar Graph")
# Show the chart
plt.show()


# In[30]:


# Histogram Code 
# Create an array of a random normal distribution
s = np.random.laplace(loc=15, scale=3, size=100)
# Create a histrogram using plt hist()
n, bins, patches = plt.hist(s, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
# Set grid for x and y
# set transperancy of the grid using alpha=0.5
plt.grid(axis='x', alpha=0.5)
plt.grid(axis='y', alpha=0.5)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My First Histogram Ever')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)


# In[23]:


# Bonus: Create a scatter plot
x_values = [3,6,17,9,3,5,2,10,19,22,6,3,8,7,12,7,4]
y_values = [100,187,182,176,88,78,34,29,87,33,84,23,54,76,39,11,90]

plt.scatter(x, y)
plt.show()


# In[ ]:




