#pip install flask
#pip install flask_mysqldb

from flask import Flask, render_template, request, url_for, redirect
from flaskext.mysql import MySQL
import datetime

user = ''
addition = None
fuser = ''
new = []

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'cars'

mysql = MySQL()
mysql.init_app(app)
conn=mysql.connect()


ALLOWED_EXT=set(['.jpg'])
curr = conn.cursor()
curr.execute("select * from user")
u = curr.fetchone()
print("..........Testing database connection........")
if(u):
	print(u)
	print("<----connected---->")
else:
	print("!!!!!!!unable to connect successfully!!!!!")


#retrieves a user if present
def retrieveUser(user):
	curr = conn.cursor()
	curr.execute("select user_id, password from User where user_id = '{user_id}'".format(user_id = user))
	u = curr.fetchone()
	return u

#inserts a new user's details into user table
def insertUser(user, email, uname, pwd, dob):
	curr = conn.cursor()
	#print(user,email,uname,pwd,dob)
	curr.execute("select email_id from User where email_id='{email_id}'".format(email_id=email))
	x=curr.fetchone()
	print(x)
	if(x):
		return False
	curr.execute("INSERT INTO User VALUES ('{user_id}', '{email_id}', '{username}', '{password}', '{DOB}')".format(user_id = user , email_id = email, username = uname, password = pwd, DOB = dob))
	conn.commit()
	
	curr.execute("select * from user where user_id='{user_id}'".format(user_id=user))
	u = curr.fetchone()
	print(u)
	return True

#renders the login page
@app.route('/')
def hello_world():
    return render_template('login.html', error=False, user=None, btn = '0')

#Checks sign-in. If successful renders home page. If sign-up is chosen renders sign-up page.
@app.route('/account', methods=['GET', 'POST'])
def login() :
	curr = conn.cursor()
	global user
	if request.form['btn'] == '1' :
		user = retrieveUser(request.form['inputid'])
		if user:
			pwd = user[1]
			ip_pwd = request.form['inputpwd']
			if pwd == ip_pwd :
				return redirect('/home')
		return render_template('login.html', error=True, btn='1',flag=False)
	elif request.form['btn'] == '2' :
		return redirect('/signup')

#Renders sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup_page() :
	return render_template('signup.html', error = False, user = None, btn ='0',flag=False)

#Creates a new user. If successful, renders login page
@app.route('/create', methods = ['GET', 'POST'])
def signup():
	global user
	user = retrieveUser(request.form['inputid'])
	print("user",user)
	if user :
		return render_template('signup.html', error = True, create = False,flag=False)
	else :
		#print(request.form['inputid'], request.form['emailid'], request.form['inputname'], request.form['inputpwd'], request.form['dob'])
		check = insertUser(request.form['inputid'], request.form['emailid'], request.form['inputname'], request.form['inputpwd'], request.form['dob'])
		if(check):
			return render_template('login.html', error = False, create = True, user = None, btn = '0')
		else:
			return render_template('signup.html', error = False, create = False,flag=True)
		
#Renders home page with the data from the back end
@app.route('/home', methods=['GET', 'POST'])
def home() :
	return render_template('home.html')

#Renders login page
@app.route("/signout")
def sign_out():
    return render_template('login.html', error=False, user=None, btn = '0')

if __name__ == "__main__" :
	app.run(host="0.0.0.0", debug = True, threaded = True)

