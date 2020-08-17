"""Server for Wear my Closet app"""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
import api

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "closet"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():

    if 'email' in session:
        return redirect('/home')

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def user_home():

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)
    
    if password in user.password:
        flash(u'Logged in!', 'email-success')
        session['email'] = user.email
        session['user_id'] = user.user_id
        print(session['email'], session['user_id'])
        return redirect('/home')

    else:
        flash(u'Log in failed. Try again.', 'password-error')
        return redirect('/')

@app.route('/register', methods=['POST'])
def create_account():

    email = request.form.get('new_email')
    password = request.form.get('new_password')
    city = request.form.get('city')
    phone = request.form.get('phone')

    user = crud.create_user(email, password, city, phone)

    session['email'] = user.email
    session['user_id'] = user.user_id
    print(session['email'], session['user_id'])

    return redirect('/home')

@app.route('/home')
def show_homepage():

    return render_template('home.html')


@app.route('/mycloset')
def my_closet():

    return render_template('mycloset.html')


@app.route('/mycloset', methods=['POST'])
def upload_item():

    item_name = request.form.get('item_name') 
    category_name = request.form.get('category')   
    image_name = request.files.get('file')

    new_item = crud.create_item(item_name, image_name, category_name)

    if image_name:
        image_url = api.upload_closet_image(image_name)

    return render_template('mycloset.html', image_url=image_url)


# @app.route('/communitycloset')
# def community_closet():

#     return render_template('communitycloset.html')

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

