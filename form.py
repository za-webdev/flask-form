from flask import Flask ,render_template,request,redirect,session,flash
from datetime import datetime
import re
app=Flask(__name__)

app.secret_key = "vsdkjnfskj/nsknjscdckj"



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+-._]+@[a-zA-Z0-9+-._]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')



@app.route('/')
def user():

	return render_template('form.html')

@app.route('/process', methods=['post'])
def process():

	valid = True
	#for first name
	if request.form["first_name"]=='':
		flash(" First Name field is required!")
		valid = False
	elif len(request.form["first_name"])< 2:
		flash("First name must be 2 characters or longer")
		valid = False
	elif  not request.form["first_name"].isalpha():
		flash("Name field cannot have numbers")
		valid=False

	#for last name
	if request.form["last_name"]=='':
		flash(" First Name field is required!")
		valid = False
	elif len(request.form["last_name"])< 2:
		flash("Last name must be 2 characters or longer")
		valid = False
	elif  not request.form["last_name"].isalpha():
		flash("Name field cannot have numbers")
		valid=False

	# fir email
	if request.form["email"]=='':
		flash("Email is required!")
		valid = False
	elif not EMAIL_REGEX.match(request.form["email"]):
		flash("Invalid Email")
		valid = False
	#for password

	if len(request.form["password"])<1:
		flash("password is required")
		valid=False
	if len(request.form["password"])<8:
		flash("password must be 8 characters or long")
		valid=False
	elif not PASSWORD_REGEX.match(request.form["password"]):
		flash("Password should contain at least 1 uppercase letter and 1 numeric value")
		valid = False
	#for confirm password

	if request.form["confirm"]=='':
		flash("Please confirm password")
		valid=False

	elif request.form["password"] != request.form["confirm"]:
		flash("Password donot match")
		valid=False

	for birthday
	if request.form["birthdate"]=='':
		flash("Please enter Birthday")
		valid=False
	elif request.form["birthdate"] != datetime.strptime(request.form["birthdate"], "%m-%d-%Y").strftime('%m-%d-%Y'):
		flash("please enter a valid birthdate")
		valid=False
            raise ValueError
        return True
    except ValueError:
        return False

		
	elif now > birthDate:
		flash("Birthday should not be in past")
		valid=False

	
	if not valid:
		print("there was an error")
		return redirect("/")
		
	
	return render_template('register.html',data=request.form)



app.run(debug=True)