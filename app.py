from flask import Flask,render_template,url_for,flash, redirect
from forms import RegistrationForm ,LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '6ca0f4e0b99dcd7bb9ab'

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