#!/usr/bin/env python
# coding: utf-8

# In[1]:


# main
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

print(test.PI)
test.PI = 5
print(test.get_circumference(radius))


# In[ ]:




