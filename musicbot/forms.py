from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from musicbot.models import User
# import musicbot.models

#Sign up form


# def validate_username(form, username):
#     print('username.data')
#     for user in User.query.filter_by(username=username.data):
#         if user:
#             raise ValidationError('Username is taken. Please choose another one')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    

#    username validator
    def validate_username(self, username):
        for user in User.query.filter_by(username=username.data):
            if user:
                raise ValidationError('Username is taken. Please choose another one')



    #email validator
    def validate_email(self, email):
        for user in User.query.filter_by(email=email.data):
            if user:
                raise ValidationError('Email is taken. Please choose another one')

#Login Form

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit =SubmitField('Login')


#Update account form

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture' ,validators=[FileAllowed(['jpg','png', 'jpeg'])])
    submit = SubmitField('Update')
    
  # username validator 
    def validate_username(self, username):
        if username.data != current_user.username:
            for user in User.query.filter_by(username=username.data):
                if user:
                    raise ValidationError('Username is taken. Please choose another one')

    # #email validator
    def validate_email(self, email):
        if email.data != current_user.email:
            for user in User.query.filter_by(email=email.data):
                if user:
                    raise ValidationError('Email is taken. Please choose another one')

# create post form
class PostForm(FlaskForm):
    title = StringField('Singer',validators=[DataRequired()])
    content = TextAreaField('Song', validators=[DataRequired()])
    submit = SubmitField('Post')   