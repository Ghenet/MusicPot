from datetime import datetime
from flask import Flask,render_template,url_for,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm ,LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '6ca0f4e0b99dcd7bb9ab'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = sb.Column(db.String(30), nullable=False)
    posts = db.realationship('Post',backref='author', lazy=True)


    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Clumn(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"



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
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))      
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

if __name__ == '__main__':
    app.run(debug=True)