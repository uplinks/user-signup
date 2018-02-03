from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def index():
    return render_template('signup.html', title='Sign up here')


@app.route('/', methods=['POST', 'GET'])
def validate_input():
    username = request.form['username']
    username_error = ""

    password = request.form['password']
    password_error = ""
    
    password_verify = request.form['password-verify']
    password_verify_error = ""

    email = request.form['email']
    email_error = ""

   
    if len(username) == 0:
        username_error = "This field can't be empty!"
    elif not 3 < len(username) <= 20:
        username_error = "must be 3-20 characters long"
    elif " " in username:
        username_error = "No empty space allowed"

    #Use this on password:
    if len(password) == 0:
        password_error = "This field can't be empty!"
    elif not 3 <= len(password) <= 20:
        password_error = "must be 3-20 characters long"  
    elif " " in password:
        password_error = "No empty space allowed"

    #Use this on password-verify.
    if password != password_verify:
        password_verify_error = "Passwords don't match!"
   
    #Use this on email.
    if len(email) > 0:
    
        if "." not in email or "@" not in email:
            email_error = "Enter correct e-mail"
        
    if not username_error and not password_error and not password_verify_error and not email_error: 
        return render_template('welcome.html', username=username, title='Success!')
    else:
        return render_template('signup.html', username=username, email=email, username_error=username_error, password_error=password_error, password_verify_error=password_verify_error, email_error=email_error, title="Enter your information")


if __name__ == '__main__':
    app.run()