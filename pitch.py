from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '8842f7517ecf0393104bb6c30a420f74'

posts = [
    {
        'author': 'leon bichanga',
        'title': 'pitch no:1',
        'content': 'First pitch ',
        'date_posted': 'September 20,2019'

    },
    {
        'author': 'Martha chitayi',
        'title': 'pitch no:2',
        'content': 'Second pitch ',
        'date_posted': 'September 21,2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html',title='About') 


@app.route("/register" ,methods=['GET','POST'])
def register():
    form = RegistrationForm()    
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login",methods= ['GET','POST'])
def login():
    form=LoginForm()  
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in!', 'success')
            return redirect(url_for('home'))  
        else:
            flash('log in unsuccefull','danger')

    return render_template('login.html', title='Login', form=form)   


if __name__ == '__main__':
    app.run(debug=True)
