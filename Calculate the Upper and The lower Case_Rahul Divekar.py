#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def sample_string(ss):
    a={"UP_CASE":0, "LOW_CASE":0}
    for i in ss:
        if i.isupper():
           a["UP_CASE"]+=1
        elif i.islower():
           a["LOW_CASE"]+=1
        else:
           pass
    print ("No. of Upper case characters : ", a["UP_CASE"])
    print ("No. of Lower case Characters : ", a["LOW_CASE"])

sample_string('The quick Brown Fox')


# In[ ]:





# In[ ]:





# In[ ]:




