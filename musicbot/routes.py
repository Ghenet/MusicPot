from flask import render_template,url_for,flash, redirect
from musicbot import app , db, bcrypt
from musicbot.forms import RegistrationForm ,LoginForm
from musicbot.models import  User , Post

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
    form =LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@ga.com' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))        
        else:
            flash('Unsuccessful login try again please','danger')
    return render_template('login.html',title='Login', form=form)            
