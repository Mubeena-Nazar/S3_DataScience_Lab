#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""
1. Write a NumPy program to create an element-wise comparison
(greater, greater_equal, less and less_equal) of two given arrays.
"""
import numpy as np
x = np.array([1,6,3])
y = np.array([2, 5,3])
print("Original numbers:")
print(x)
print(y)
print("\n1. Comparison - greater")
print("----------------------")
print(np.greater(x, y))
print("\n2. Comparison - greater_equal")
print("-----------------------------")
print(np.greater_equal(x, y))
print("\n3. Comparison - less")
print("--------------------")
print(np.less(x, y))
print("\n4. Comparison - less_equal")
print("--------------------------")
print(np.less_equal(x, y))



# In[16]:


"""2. Write a NumPy program to create an array of all the even integers from 30 to 70."""

import numpy as np
array=np.arange(30,71,2)
print("Array of all the even integers from 30 to 70:\n")
print(array) 


# In[15]:


"""3. Write a NumPy program to create a 3x3 identity matrix."""

import numpy as np
array_2D=np.identity(3)
print('3x3 matrix:')
print(array_2D)


# In[18]:


"""4. Write a NumPy program to create a vector with values 
from 0 to 20 and change the sign of the numbers in the range from 9 to 15."""


import numpy as np
x = np.arange(21)
print("\nOriginal vector:")
print(x)
print("\nAfter changing the sign of the numbers in the range from 9 to 15:")
x[(x >= 9) & (x <= 15)] *= -1
print(x)


# In[29]:


"""5. Write a NumPy program to create a 5x5 zero matrix with elements 
on the main diagonal equal to 1, 2, 3, 4, 5"""

import numpy as np
print("\tMatrix")
print("------------------------")
x = np.diag([1, 2, 3, 4, 5])
print(x)


# In[32]:


"""6. Write a NumPy program to compute sum of all elements, sum of each column 
and sum of each row of a given array."""

import numpy as np
x = np.array([[0,1],[2,3]])
print("Original array:")
print(x)
print("\nSum of all elements:")
print("------------------------")
print(np.sum(x))
print("\nSum of each column:")
print("------------------------")
print(np.sum(x, axis=0))
print("\nSum of each row:")
print("------------------------")
print(np.sum(x, axis=1))


# In[38]:


"""7. Write a NumPy program to save a given array to a text file and load it."""
import numpy as np
import os
x = np.arange(12).reshape(4, 3)
print("Original array:")
print("---------------")
print(x)
header = 'col1 col2 col3'
np.savetxt('temp.txt', x, fmt="%d", header=header) 
print("\nAfter loading, content of the text file:")
print("----------------------------------------")
result = np.loadtxt('temp.txt')
print(result)


# In[41]:


"""Write a NumPy program to check whether two arrays are equal (element wise) or not."""

import numpy as np


nums1 = np.array([0.5, 1.5, 0.2])
nums2 = np.array([0.4999999999, 1.500000000, 0.2])
np.set_printoptions(precision=15)
print("Original arrays:")
print("---------------")
print(nums1)
print(nums2)
print("\nTest said two arrays are equal (element wise) or not:?")
print(nums1 == nums2)


nums1 = np.array([0.5, 1.5, 0.23])
nums2 = np.array([0.4999999999, 1.5000000001, 0.23])
print("\nOriginal arrays:")
print("---------------")
np.set_printoptions(precision=15)
print(nums1)
print(nums2)
print("\nTest said two arrays are equal (element wise) or not:?")
print(np.equal(nums1, nums2))


# In[50]:


"""9. Write a NumPy program to create a 4x4 array with random values, 
now create a new array from the said array swapping first and last rows."""

import numpy as np 
nums = np.arange(16, dtype='int').reshape(-1, 4)
print("Original array:")
print(nums)
print("\nNew array after swapping first and last rows of the said array:")
new_nums = nums[[-1,1,2,0]]
print(new_nums)


# In[56]:


"""10. Write a NumPy program to multiply two given arrays of same size element-by-element."""
import numpy as np 
nums1 = np.array([[2, 5, 2],
              [1, 5, 5]])
nums2 = np.array([[5, 3, 4],
              [3, 2, 5]])
print("\nArray1:") 
print("-------------")
print(nums1)
print("\nArray2:") 
print("-------------")
print(nums2)
print("\nMultiply said arrays of same size element-by-element:")
print("----------------------------------------------------")
print(np.multiply(nums1, nums2))



