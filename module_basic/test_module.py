#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()


# In[ ]:


PI = 3.14

def number_input() :
    output = input('숫자 입력')
    
    return float(output)

def get_circumference(radius) :
    return radius * 2 * PI

def get_circle_area(radius) :
    return radius * radius * PI

print('test 모듈')
print(__name__)
print('test ---')

if __name__ == '__main__' :
    print('get_circumference(10) : ', get_circumference(10))
    print('get_circle_area(10) : ', get_circle_area(10))