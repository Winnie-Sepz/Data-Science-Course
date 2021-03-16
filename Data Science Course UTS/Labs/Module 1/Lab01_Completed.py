#!/usr/bin/env python
# coding: utf-8

# <div>
# <img src=https://www.institutedata.com/wp-content/uploads/2019/10/iod_h_tp_primary_c.svg width="300">
# </div>
# 
# # Python - Lab 1 
# 
# ## Learning objectives
# 
# This lab demonstrates examples of: 
# 
# 1. Creating and manipulating lists
# 2. For loops
# 3. Importing modules and functions
# 4. Creating dictonaries
# 
# ## Instructions:
# 
# 1. Replace ??? with the appropriate code
# 2. Press Shift + Enter to execute cell
# 
# 

# In[ ]:


# create a list of 10 student (use just first name)
students = ["Anne", "Bianca", "Cassie", "Debbie", "Erica", "Fiona", "Georgia", "Helen", "Isabelle", "Jenny"]


# In[5]:


# Print the list
print(students)


# In[28]:


# print the list of students
# in the following format
# Index 01 	 Alice
# Index 02 	 Bob
# Index 03 	 Pradeep
for index, a in enumerate(students):
       print(f'index {index +1 :02d}\t {a}')


# In[ ]:


# print the list of students in reverse order one student in a line with its index
reversed_list = students.copy()
for index, a in reversed(list(enumerate(reversed_list))):
       print(f'index {index +1 :02d}\t {a}')


# In[34]:


# print the student list in random order
# hint look up the function random.sample
import random
random_list= random.sample(students,10)
print(random_list)


# In[49]:


# list students in order of their exam marks in the following list
marks = [87,45,76,64,66,90,55,73,69,75]
sorted_values = sorted(studentsAndMarks, key=studentsAndMarks.get, reverse=True)
studentsAndMarks = dict(zip(students,marks))
#print(f"Students and their marks: \n {studentsAndMarks}")
for r in sorted_values :
    print(r, studentsAndMarks[r])


# In[ ]:





# In[ ]:




