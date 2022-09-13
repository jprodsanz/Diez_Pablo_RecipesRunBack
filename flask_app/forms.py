#python classes that turn into html forms courtesy of wtforms
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user 
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_app.models import User

class RegistrationForm(FlaskForm): 
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    first_name = StringField('First Name', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username not available')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email is taken')
        

class LoginForm(FlaskForm): 
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
    

class UpdateAccountForm(FlaskForm): 
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('username not available')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('email is taken')

class PostForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators= [DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    submit= SubmitField('Post')
