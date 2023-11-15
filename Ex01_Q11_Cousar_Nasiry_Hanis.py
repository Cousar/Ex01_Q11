#!/usr/bin/env python
# coding: utf-8

# Importing numpy library and definning a function that calculate the product of two 3 by 3 matrices

# In[1]:


import numpy as np
def product_matrix(matrix1,matrix2):
    
    final_product = np.zeros((3, 3), dtype=float)
    for i in range (3):
        for j in range (3):
            for k in range (3):
                final_product[i, j] += float(matrix1[i, k]) * float(matrix2[k, j])
    return final_product
    


# Making two random matrices and recalling the defined function to give the final product of theor multiplication.

# In[2]:


matrix1=np.ndarray(shape=(3,3), dtype=int)
matrix2=np.ndarray(shape=(3,3), dtype=int)
final_product = product_matrix(matrix1, matrix2)

print (matrix1)
print (matrix2)
print (final_product)   


# In[ ]:




