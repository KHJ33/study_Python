import cx_Oracle 
import pandas as pd

# cx_Oracle.makedsn : 오라클에 대한 주소 정보
# cx_Oracle.connect : 오라클 접속 유저 정보
# db.cursor : 데이터 담을 메모리의 이름을 선언
# cursor.execute : SQL의 결과가 cursor 메모리를 담는다.
# cursor.fetchall : 메모리에 담긴 데이터를 한 행씩 fetch 한다. 전부 all.
# cursor.description : 데이터의 칼럼명을 추출

dsn = cx_Oracle.makedsn('hostname',1521,'서비스 이름')
db = cx_Oracle.connect('사용자명', '비밀번호')

cursor = db.cursor()
cursor.execute('select * from test')

row = cursor.fetchall()
colname = cursor.description

col = []
for i in colname:
    col.append(i[0])


# dataframe으로 변환시킴
emp = pd.DataFrame(row,  columns = col)
emp