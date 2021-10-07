#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#2.-Matrix-multiplication" data-toc-modified-id="2.-Matrix-multiplication-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>2. Matrix multiplication</a></span></li></ul></div>

# # 2. Matrix multiplication
# 
# 2.1 [5 points] Make two matrices M1 (5 rows and 10 columns ) and M2 (10 rows and 5 columns ); both are filled with random integers from 0 and 50.

# In[2]:


import numpy as np


# In[3]:


M1 = np.matrix(np.random.rand(5,10)*50)
M2 = np.matrix(np.random.rand(10,5)*50)
M1.shape, M2.shape


# 2.2 [10 points] Write a function Matrix_multip to do matrix multiplication, i.e., M1 * M2. Here you are ONLY allowed to use for loop, * operator, and + operator

# In[4]:


def Matrix_multip(M1,M2):
    row1,col1 = M1.shape
    row2,col2 = M2.shape
    
    if (col1 != row2):
        M2_t = M2.reshape((col2,row2))
        row2_t,col2_t = M2_t.shape
        M2 = M2_t
        print('Transpose M2')
    
        if (col1 != row2_t):
            return print('Matrix Multiplication False: Shape error')
            
    elif (col1 == row2):
        global out_matrix
        out_matrix = np.matrix(np.zeros((M1.shape[0],M2.shape[1])))
        for i in range(out_matrix.shape[0]):
            for j in range(out_matrix.shape[1]):
                out_matrix[i,j] = M1[i,:]*M2[:,j]
                
    return out_matrix


# In[5]:


Mul_M = Matrix_multip(M1,M2)
Mul_M

