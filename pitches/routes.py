from flask import render_template, url_for, flash, redirect
from pitches import app
from pitches.forms import RegistrationForm, LoginForm
from pitches.models import User, Pitch

pitches = [
    {
        'author': 'Barrack Obama',
        'type': 'One Word Pitch',
        'content': 'Hope',
        'date_posted': 'May 13, 2022'
    },
    {
        'author': 'Google',
        'type': 'One Word Pitch',
        'content': 'Search',
        'date_posted': 'May 1, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', pitches=pitches)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account for {form.username.data} created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
