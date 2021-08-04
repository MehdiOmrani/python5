#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(20, 35, 19))


# In[2]:


#Question 2
def calculation(a, b):
    # Your Code

answer = calculation(40, 10)
print(answer)


# In[3]:


#Question 3
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))


# In[ ]:


#Question 4
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))


# In[ ]:


#Question 5
import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)


# In[ ]:




