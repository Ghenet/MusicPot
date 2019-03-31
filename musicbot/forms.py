from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email,EqualTo, ValidationError
from musicbot.models import User


#Sign up form

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators= [DataRequired(), 
    Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    

   #username validator 
    def validate_username(self, username):
        user = User.query.filter_by(username =username.data)
        if user:
            raise ValidationError('That username is taken.please choose another one')



    #email validator
    def validate_email(self, email):
        user = User.query.filter_by(email =email.data)
        if user:
            raise ValidationError('That email is already taken.Please choose another one')
#Login Form

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit =SubmitField('Login')