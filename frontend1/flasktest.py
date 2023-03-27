from flask import Flask, render_template, url_for, request, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dsgb'
  
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('homecopy.html')


@app.route('/about')
def about_page():
    return render_template('aboutus.html')

@app.route('/contact')
def contact_page():
    return render_template('contactus.html')


@app.route('/signup')
def signup_page():
    return render_template('signup.html')


   
@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('homecopy.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('loginpage.html', mesage = mesage)

@app.route('/premium')
def premium_page():
    return render_template('premium.html')



if __name__ == "__main__":
    app.run(debug=True)
