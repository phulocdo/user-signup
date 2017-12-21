from flask import Flask, render_template, request, flash
from createform import CreateForm



app = Flask(__name__)
app.config['DEBUG'] = True ##enable debug option
app.secret_key = 'Luanchcode tampabay 2017'   ###CSRF key

"""Rendering home page"""
@app.route('/')
def home():
    return render_template('home.html')


"""Instantiate signup form and rendering welcome page if successfully validated, else rendering signup page"""
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = CreateForm()
    if(request.method == 'POST' and form.validate_on_submit()):
        status = "signup"
        return render_template('welcome.html',name=form.username.data,status=status) 
	
    return render_template('signup.html',form=form) 

"""Instantiate login form and rendering welcome page if successful, else rendering login page"""
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = CreateForm()
    error = ""
    if(request.method == 'POST'):
        if(request.form['username'] != "admin" or request.form['password1'] != "newsys"):
            error="Invalid credential, Please sign up for an account"
        else:
            status = "login"
            return render_template('welcome.html',name=form.username.data,status=status) 

    return render_template('login.html', form=form, error=error)

"""rendering about page"""
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000)
