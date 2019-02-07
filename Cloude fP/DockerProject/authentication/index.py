from flask import Flask, request, render_template, redirect
import json
from flaskext.mysql import MySQL
from cryptography.fernet import Fernet

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'ninja'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'mydata'
app.config['MYSQL_DATABASE_HOST'] = 'database'
mysql.init_app(app)


@app.route('/')
def my_reg():
    return render_template('register.html')


@app.route('/login')
def my_log():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connect().cursor()
    cursor.execute("select user_id from users where nationcode = '" + username + "' and password = '" + password + "'")
    #cursor.execute("select * from users")
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    data = cursor.fetchall()
    if data is None:
        return "user or pass is wrong"
    else:
        return redirect("http://localhost:160/" + str(data[0]))

@app.route('/register', methods=['POST'])
def Authenticate():

        fname = request.form['fname']
        lname = request.form['lname']
        nationcode = request.form['nationcode']
        password = request.form['Pasd']
        con = mysql.connect()
        cursor = con.cursor()
        conversion = "insert into users(fname, lname,  nationcode, password) values(%s, %s, %s, %s)"
        cursor.execute(conversion, [fname, lname, nationcode, password])
        con.commit()
        return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
