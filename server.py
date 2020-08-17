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

    return render_template('login.html')


@app.route('/home', methods=['POST'])
def user_home():

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)

    
    if password in user.password:
        flash('Logged in!')
        session['email'] = user.user_id

    else:
        flash('Log in failed. Try again.')
        return redirect('/')


    return render_template('home.html')


@app.route('/mycloset')
def my_closet():

    return render_template('mycloset.html')


@app.route('/mycloset', methods=['POST'])
def upload_image():
    filename = request.files.get('file')
    if filename:
        image_url = api.upload_closet_image(filename)

    item_name = request.form()

    return render_template('mycloset.html', image_url=image_url)


# @app.route('/communitycloset')
# def community_closet():

#     return render_template('communitycloset.html')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

