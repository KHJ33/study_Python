#!/usr/bin/env python
# coding: utf-8

# In[1]:


# create table
from select import select
import pymysql

db = pymysql.connect(host='localhost', user='root',
                     db='python', password='passwd', charset='utf8')
curs = db.cursor()

sql = '''create table sample (
    column01 varchar(50), 
    column02 varchar(50), 
    column03 varchar(50))
'''

curs.execute(sql)

# sql = "select * from sample";
# curs.execute(sql)

# rows = curs.fetchall()
# print(rows)

# db.commit()
db.close()


# In[2]:


db = pymysql.connect(host='localhost', user='root',
                     db='python', password='passwd', charset='utf8')
curs = db.cursor()

sql = "select * from sample";
curs.execute(sql)

rows = curs.fetchall()
print(rows)

db.commit()
db.close()


# In[9]:


# insert
import pymysql

db = pymysql.connect(host='localhost', user='root', db='python', 
                     password='passwd', charset='utf8')
curs = db.cursor()

sql='''insert into sample (column01, column02, column03) 
        values ('aa12' ,'bb12','cc12')
    '''

curs.execute(sql)

sql = "select * from sample";
curs.execute(sql)

rows = curs.fetchall()
print(rows)

db.commit()
db.close()


# In[12]:


# 여러개의 row 검색 : select
db = pymysql.connect(host='localhost', user='root', db='python', 
                     password='passwd', charset='utf8')
curs = db.cursor()

# sql = "select * from sample";
sql = "select * from sample where column01 = 'aa' ";

curs.execute(sql)

rows = curs.fetchall()
for row in rows:
    print(row)

db.commit()
db.close()


# In[13]:


# update
import pymysql

db = pymysql.connect(host='localhost', user='root', 
                     db='python', password='passwd', charset='utf8')
curs = db.cursor()

sql = '''
update sample set column01 = 'cc', column02 = 'bb'
where column01 = 'aa';
'''

curs.execute(sql)

sql = "select * from sample";
curs.execute(sql)

rows = curs.fetchall()
print(rows)

db.commit()
db.close()


# In[16]:


# delete
import pymysql

db = pymysql.connect(host='localhost', user='root', 
                     db='python', password='passwd', charset='utf8')
curs = db.cursor()

sql = '''
delete from sample 
where column01 = 'cc'
'''
curs.execute(sql)

sql = "select * from sample";
curs.execute(sql)

rows = curs.fetchall()
print('rollback before \n', rows)

db.rollback()   #  작업 원 위치

sql = "select * from sample";
curs.execute(sql)

rows = curs.fetchall()
print('rollback  after \n', rows)

sql='''insert into sample (column01, column02, column03) 
        values ('dd' ,'bb12','cc12')
    '''
curs.execute(sql)

sql = "select * from sample";
curs.execute(sql)

rows = curs.fetchall()
print(rows)

db.commit()
db.close()

