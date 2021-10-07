#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#4.-Add-or-double" data-toc-modified-id="4.-Add-or-double-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>4. Add or double</a></span></li></ul></div>

# # 4. Add or double
# 
# [20 points] If you start with 1 RMB and, with each move, you can either double your money or add another 1 RMB, what is the smallest number of moves you have to make to get to exactly x RMB? Here x is an integer randomly selected from 1 to 100. Write a function Least_moves to print your results. For example, Least_moves(2) should print 1, and Least_moves(5) should print 3

# In[4]:


import numpy as np


# In[11]:


def Least_moves():
    iters = 100
    x0_step = [1,]
    rand = int(input("Please type a random interger: "))
    xx_step = np.zeros(iters)
    xx_step[0]=rand
    for i in range(1,iters):
        rand_i = rand/2
        if (rand_i != 1):
            if (rand%2 != 0):
                rand_i = rand-1
                xx_step[i] = rand_i
            if (rand%2 ==0):
                xx_step[i] = rand_i
        if (rand_i == 1):
            xx_step[i] = 1
            break
        rand = rand_i
    return len([x for x in xx_step if x>0])-1


# In[13]:


Least_moves()

