#!/usr/bin/env python
# coding: utf-8

# In[5]:


def mod(number, cellNumber):
    return number % cellNumber


# In[6]:


print(mod(400, 24))


# In[7]:


def modASCII(string,cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber


# In[8]:


print(modASCII("ABC", 24))

