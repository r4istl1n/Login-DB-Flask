from . import db
from flask import Flask, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)
db   = SQLAlchemy()


@auth.route('/login', methods= ['GET', 'POST'])
def login():
    return render_template("login.html", text="Testing", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign_up', methods= ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email      = request.form.get('email') 
        first_name = request.form.get('firstName')
        password1  = request.form.get('password1')
        password2  = request.form.get('password2')

       

        if len(email) < 4:
            flash('Email must be greater than 3 characthers.', category= 'error')
        elif len(first_name) < 2:
            flash('Fist name must be greater than 1 characther.', category= 'error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category= 'error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characthers')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='success')
        return redirect(url_for('views.home'))

            #add user to database
            #flash('Account created!', category= 'success') 

    return render_template("sign_up.html")

