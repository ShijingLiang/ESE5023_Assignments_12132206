#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#1.-Flowchart" data-toc-modified-id="1.-Flowchart-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>1. Flowchart</a></span></li></ul></div>

# # 1. Flowchart
# 
# [10 points] Write a function Print_values with arguments a, b, and c to reflect the following flowchart. Here the purple parallelogram operator is to print values in the given order. Report your output with some random a, b, and c values.

# In[1]:


import numpy as np


# In[2]:


def Print_values(a,b,c):
    if (a>b):    # if: if condition satisfies, stop running
        if(b>c): # if & elif: elif allows judging from previous states
            print(a,b,c)
        if(b<c):
            if (a>c):
                print(a,c,b)
            else:
                print(c,a,b)
    if (a<b):
        if(b>c):
                print(c,a,b)
        else:
                print(c,b,a)
                


# In[3]:


a,b,c = 2,3,1


# In[4]:


test = Print_values(a,b,c)


# In[ ]:




