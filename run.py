from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '0e3264bd6bca6f26a5a4630f'

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
@app.route('/home')
def home():
    return render_template('home.html', recipes=recipes)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'pablox@gmail.com' and form.password.data == 'password':
            flash('You are logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Check your info', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
