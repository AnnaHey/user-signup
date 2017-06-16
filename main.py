from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_form.html')

@app.route('/validate')
def display_user_form():
    return render_template('user_form.html')


@app.route("/validate", methods=['POST', 'GET'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    username_error =''
    password_error = ''
    v_p_error = ''
    email_error = ''


    if len(username) < 3 or len(username) > 20:
        username_error = "Not a valid username" 
        username = ''

    if password != verify_password:
        password_error = "Not a match" 
        password = ''
    else:
        password = password
    
    if verify_password != password:
        v_p_error = "Not a match, please re-enter password and verification"
        password = ''
        verify_password = ''
    else:
        password = password
        verify_password = verify_password

    if email.count("@") == 1 and email.count(".") == 1 and email.count(" ") == 0:
        email = email
    else:
        email_error="invalid email"
        email = ''
        

    if not username_error and not password_error and not v_p_error and not email_error:
        
        return redirect("/Welcome?username={}".format(username))
    else:
        return render_template('user_form.html',username=username, 
            username_error=username_error, 
            password=password,
            password_error=password_error,
            verify_password=verify_password,
            v_p_error=v_p_error, 
            email=email, 
            email_error=email_error)

@app.route("/Welcome")
def valid_entry ():
    username = request.args.get('username')
    return render_template('welcome.html', awesome=username)

app.run()