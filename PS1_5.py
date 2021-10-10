#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#5.-Dynamic-programming" data-toc-modified-id="5.-Dynamic-programming-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>5. Dynamic programming</a></span></li></ul></div>

# # 5. Dynamic programming
# 
# Insert + or - operation anywhere between the digits 123456789 in a way that the expression evaluates to an integer number. You may join digits together to form a bigger number. However, the digits must stay in the original order.
# 
# 5.1 [30 points] Write a function Find_expression, which should be able to print every possible solution that makes the expression evaluate to a random integer from 1 to 100. For example, Find_expression(50) should print lines include:
# 1−2+34+5+6+7+8−9=50
# and
# 1+2+34−56+78−9=50
# 
# 5.2 [5 points] Count the total number of suitable solutions for any integer i from 1 to 100, assign the count to a list called Total_solutions. Plot the list Total_solutions, so which number(s) yields the maximum and minimum of Total_solutions?
# 

# In[1]:


import numpy as np


# In[2]:


def calcp(num_x):
    return '+'+ num_x

def calcm(num_x):
    return '-'+ num_x

def calcc(num_xi):
    return num_xi+''


# In[3]:


def Find_expression(num):
    # Three operations for digits 123456789
    M = []
    for i in range(2,10):
        M.append([calcp('%s'%i),calcm('%s'%i),calcc('%s'%i)])
    test = []
    # List all possible expressions
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    for e in range(3):
                        for f in range(3):
                            for g in range(3):
                                for h in range(3):
                                    test.append(('1'+M[0][a]+M[1][b]+M[2][c]+M[3][d]+M[4][e]+M[5][f]+M[6][g]+M[7][h]))
    # The result of each espression
    num_sum = np.zeros((len(test)))
    for i in range(len(test)):
        indx = []
        for j in range(len(test[i])):        
            if(test[i][j].isdigit()==False):
                indx.append(j)
        indx.append(len(test[i]))
        num_sum[i] = int(test[i][:indx[0]])
        for k in range(1,len(indx)):
            num_sum[i] += int(test[i][indx[k-1]:indx[k]])
            
    index = np.argwhere(num_sum == num)
    return [test[int(index[i])] for i in range(len(index))]


# In[4]:


Find_expression(100)


# In[5]:


import matplotlib.pyplot as plt


# In[6]:


def Total_solutions():
    tot_sols = [len(Find_expression(i)) for i in range(101)]
    return tot_sols


# In[7]:


tot_sols = Total_solutions()


# In[8]:


x = np.arange(101)
pltdata = np.array(tot_sols)
plt.plot(x,pltdata)

sols_min = [np.argwhere(pltdata==pltdata.min()),pltdata.min()]
sols_max = [np.argwhere(pltdata==pltdata.max()),pltdata.max()]

plt.scatter(sols_min[0],sols_min[1],c='b',label='Minumum steps')
[plt.scatter(sols_max[0][i],sols_max[1],c='r',label='Maximum steps') for i in range(2)]
plt.legend()

