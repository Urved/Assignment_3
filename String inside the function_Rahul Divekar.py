#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Write a Python program to reverse a string.
#method 1 (loop)

def reverse(s1):

    reverse_s1 = ''
    idx = len(s1)
    while idx > 0:
        reverse_s1 += s1[ idx - 1 ]
        idx -= 1
    return reverse_s1
print(reverse('1234abcd'))


# In[4]:


#method 2 (Slicing)

def reverse(s2):
  return s2[::-1]

string = '1234abcd'
print(reverse('1234abcd'))


# In[ ]:




