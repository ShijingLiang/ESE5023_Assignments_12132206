#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#3.-Pascal-triangle" data-toc-modified-id="3.-Pascal-triangle-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>3. Pascal triangle</a></span></li></ul></div>

# # 3. Pascal triangle
# 
# [20 points] One of the most interesting number patterns is Pascal’s triangle (named after Blaise Pascal). Write a function Pascal_triangle with an argument k to print the kth line of the Pascal triangle. Report Pascal_triangle(100) and Pascal_triangle(200)

# In[1]:


# Import libraries
from math import factorial
import numpy as np


# In[2]:


def Pascal_triangle(n):
    out_array = np.zeros(n+1)
    for k in range(0,n+1):
        out_array[k] = factorial(n) / (factorial(k)*factorial(n-k))
    return out_array


# In[3]:


Pascal_triangle(100)


# In[4]:


Pascal_triangle(200)

