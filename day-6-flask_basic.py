#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# mac 북
# export FLASK_APP = day-6-flask_basic.py
# window -> 관리자 권환으로 실행
# set FLASK_APP = day-6-flask_basic.py

# flask run


# In[1]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() :
    return '<h1>Hello World</h1>'

@app.route('/test')
def test() :
    return 'Hello test !!!'

