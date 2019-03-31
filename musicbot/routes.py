from flask import render_template,url_for,flash, redirect, request
from musicbot import app , db, bcrypt
from musicbot.forms import RegistrationForm ,LoginForm
from musicbot.models import  User , Post
from flask_login import login_user , current_user,logout_user, login_required

posts =[
    {
        'singer': 'Rihanna',
        'album' : 'Bad Girl',
        'Genre' : "R&B",
        'date_released': 'April 20, 2018'

    },
    {
        'singer': 'Chris Brown',
        'album' : 'Royality',
        'Genre' : "R&B",
        'date_released': 'May 20, 2015'

    },
    {
        'singer': 'Justin Bieber',
        'album' : 'Baby',
        'Genre' : "POP",
        'date_released': 'November, 2010'

    }
]



@app.route("/")
@app.route("/home")
def home():
    return  render_template('home.html', posts_data=posts)
  


@app.route('/profile')
def profile():
     return render_template('profile.html',title='Hey About')  


@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!You are now able to log in','success')
        return redirect(url_for('login'))      
    return render_template('register.html',title='Register', form=form)



@app.route('/login', methods =['GET','POST']) 
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form =LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password , form.password.data):
             login_user(user, remember=form.remember.data)
             next_page = request.args.get('next')   #dont really know what this is doing , gotta refer back to part 6 at 43:00
             return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.Please check email or password','danger')
    return render_template('login.html',title='Login', form=form)            


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html' , title='Account')    