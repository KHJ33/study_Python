from flask import Flask, session, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'passwd'
app.config['MYSQL_DB'] = 'pydata'
app.secret_key = 'ABCDEF'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def main():
    error = None

    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']

        conn = mysql.connection
        cursor = conn.cursor()

        sql = "SELECT id,name FROM users WHERE id = '%s' AND passwd = '%s' " % (id, pw)

        # print(sql)
        # cursor.execute("set names utf8")
        cursor.execute(sql)

        data = cursor.fetchall()
        cursor.close()
        conn.close()

        for row in data:
            r_id = row[0]
            r_name = row[1]

        if data:
            session['login_id'] = id
            return redirect(url_for('home',name=r_name))
        else:
            error = 'invalid input data detected !'

    return render_template('main.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        id = request.form['regi_id']
        pw = request.form['regi_pw']
        name = request.form['regi_name']

        conn = mysql.connection
        cursor = conn.cursor()

        sql = "INSERT INTO users(id,passwd,name) VALUES ('%s', '%s')" % (id, pw,name)
        cursor.execute(sql)

        data = cursor.fetchall()

        if not data:
            conn.commit()
            return redirect(url_for('main'))
        else:
            conn.rollback()
            return "Register Failed"

        cursor.close()
        conn.close()

    return render_template('register.html', error=error)

@app.route('/home/<name>')
def home(name):
    return render_template('home.html', name=name)
    
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
