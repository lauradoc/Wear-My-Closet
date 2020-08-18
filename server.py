"""Server for Wear my Closet app"""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db
import crud
import api

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "closet"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def login():
    
    return render_template('login.html')


@app.route('/newuser', methods=['POST'])
def create_account():

    email = request.form.get('new_email')
    password = request.form.get('new_password')
    city = request.form.get('city')
    phone = request.form.get('phone')
    user = crud.get_user_by_email(email)

    if user:
        flash('Email already exists. Please make an account with a different email')

    else:
        user = crud.create_user(email, password, city, phone)
        session['email'] = user.email
        session['user_id'] = user.user_id
        flash('Your account was created successfully! You can now log in.')

    return redirect('/')


@app.route('/login')
def handle_login():
    """Check to see if password matches and log user in"""

    email = request.args.get('email')
    password = request.args.get('password')
    user = crud.get_user_by_email(email)

    if password in user.password:
        flash(u'Logged in!', 'email-success')
        session['email'] = user.email
        session['user_id'] = user.user_id
        return render_template('home.html', email=email)

    else:        
        flash(u'Log in failed. Try again.', 'password-error')
        return redirect('/')


@app.route('/home')
def show_homepage():

    return render_template('home.html')


@app.route('/mycloset')
def my_closet():
    
    if 'user_id' in session:
        closet = crud.get_items_by_user(session['user_id'])
        return render_template('mycloset.html', closet=closet)

    else:
        flash(u'Need to be logged in to view "My Closet" page', 'login-error')
        return redirect('/')

@app.route('/mycloset', methods=['POST'])
def upload_item():
    # import pdb; pdb.set_trace()  
    item = request.files.get('file')
    print(item)
    print(request)
    closet = crud.get_items_by_user(session['user_id'])
    if item:
        image_url = api.upload_closet_image(item)
        item_name = request.form.get('item_name')
        category_name = request.form.get('category') 
        user_id = session.get('user_id')
        closet.append(image_url)
        
        new_item = crud.create_item(user_id, item_name, image_url, category_name)
    
    else:
        image_url = None

    return redirect('/mycloset')

@app.route('/communitycloset')
def community_closet():


    return render_template('communitycloset.html')


@app.route('/myaccount')
def checkout():

    return render_template('profile.html')

@app.route("/logout")
def logout_user():
    """Log out a user."""

    if 'email' in session:
        session.pop('email', None)
        session.pop('user_id', None)
    return redirect("/")


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

