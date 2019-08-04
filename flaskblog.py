from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '061a9d20aa9aec2f897c7e0e115f65c0'


posts = [
    {
        "author": "Olufemi Afolabi",
        "title": "Blog Post 1",
        "content": "First Post",
        "date_posted": "4 04, 2019"
    },
    {
        "author": "Olayemi Afolabi",
        "title": "Blog Post 2",
        "content": "Second Post",
        "date_posted": "4 05, 2019"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login Successful {form.email.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
