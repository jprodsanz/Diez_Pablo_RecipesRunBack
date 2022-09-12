from flask import render_template, flash, redirect, url_for
from flask_app.models import User, Recipe
from flask_app.forms import RegistrationForm, LoginForm
from flask_app import app, db, bcrypt 

recipes = [
    {
        'chef': ' Pablo X',
        'dish': 'Tacos',
        'content': 'Not under 30 mins',
        'date_posted': 'Sept 11, 2022',
    },
    {
        'chef': ' Ana Sofia',
        'dish': 'Asado Negro',
        'content': 'Yes, under 30 mins',
        'date_posted': 'Sept 11, 2022',
    },
    {
        'chef': ' Sara Restrepo',
        'dish': 'Arepas',
        'content': 'Maybe under 30 mins',
        'date_posted': 'Sept 11, 2022',
    }
]

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', recipes=recipes)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Log in,please', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'pablox@gmail.com' and form.password.data == 'password':
            flash('You are logged in!','success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Check your info', 'danger')
    return render_template('login.html', title='Login', form=form)
