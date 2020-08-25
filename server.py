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
    """Login page for user"""
    
    return render_template('login.html')


@app.route('/newuser', methods=['POST'])
def create_account():
    """Form on login page to create a new account"""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('new_email')
    password = request.form.get('new_password')
    city = request.form.get('city')
    phone = request.form.get('phone')
    user = crud.get_user_by_email(email)

    if user:
        flash(u'Email already exists. Please make an account with a different email')

    else:
        user = crud.create_user(first_name, last_name, email, password, city, phone)
        session['email'] = user.email
        session['user_id'] = user.user_id
        flash('Your account was created successfully! You can now log in.')

    return redirect('/')


@app.route('/login', methods=['POST'])
def handle_login():
    """Check to see if password matches and log user in"""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)

    if password in user.password:
        flash(u'Logged in!', 'email-success')
        session['email'] = user.email
        session['user_id'] = user.user_id
        communities = crud.get_community_by_user(session['user_id'])

        return redirect('/home')

    else:        
        flash(u'Log in failed. Try again.', 'password-error')
        return redirect('/')


@app.route('/home')
def view_home():
    """Load home page once user is logged in"""

    email = session.get('email')
    if email:
        communities = crud.get_all_communities()
        return render_template('home.html', email=email, communities=communities)
    else:
        return redirect('/')


@app.route('/createcommunity', methods=['POST'])
def create_community():
    """Create a new community"""

    community_name = request.form.get('community_name')
    location = request.form.get('location')
    if community_name:
        new_community = crud.create_community(community_name, location)

    return render_template('home.html')


@app.route('/joincommunity')
def join_community():
    """Join an existing community"""

    user_id = session.get('user_id')
    community_name = request.args.get('join-community')
    community_id = crud.get_community_id_by_community_name(community_name)
    new_member = crud.create_community_member(community_id, user_id)
    user_communities = crud.get_community_by_user(user_id) 

    return render_template('community.html', user_communities=user_communities)


@app.route('/community')
def view_my_community():
    """view communities based on user logged in"""

    user_id = session.get('user_id')
    user_communities = crud.get_community_by_user(user_id) 

    return render_template('community.html', user_communities=user_communities)
    

@app.route('/communitycloset')
def view_community_closet():
    community_name = request.args.get("community")
    community_users = crud.get_users_by_community(community_name)
    user_items = {}
    for user in community_users:
        closet = crud.get_items_by_user(user.user_id)
        user_items[user.user_id] = closet
    return render_template('communitycloset.html', community_name=community_name, community_users=community_users, user_items=user_items)


# @app.route('/commmunity_items')
# def view_items_by_community():

#     community_users = crud.get_users_by_community(community)
#     user_items = {}
#     for user in community_users:
#         closet = crud.get_items_by_user(user)
#         user_items[user] = closet
#     return render_template('community.html', community=community, community_users=community_users, user_items=user_items)

@app.route('/checkout')
def add_to_checkout():

    return render_template('checkout.html')
    

@app.route('/checkout', methods=['POST'])
def checkout_item():

    checkout = crud.get_checkout_by_user(session['user_id'])
    item = request.form.get('checkout-items')

    if checkout:
        return render_template('checkout.html', item=item)
    else:
        flash(u'No item in checkout')
        return redirect('/mycommunity')
    

@app.route('/mycloset')
def my_closet():
    
    if 'user_id' in session:
        closet = crud.get_image_urls_by_user(session['user_id'])
        return render_template('mycloset.html', closet=closet)

    else:
        flash(u'Need to be logged in to view this page', 'login-error')
        return redirect('/')


@app.route('/mycloset', methods=['POST'])
def upload_item():
    # import pdb; pdb.set_trace()  
    item = request.files.get('file')
    closet = crud.get_image_urls_by_user(session['user_id'])
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


@app.route('/myaccount')
def account_details():
    user = crud.get_user_by_email(session['email'])
    user_id = user.user_id
    email = user.email
    city = user.city
    phone = user.phone
    closet = crud.get_image_urls_by_user(session['user_id'])
    checkouts = crud.get_checkout_by_user(session['user_id'])
    communities = crud.get_community_by_user(session['user_id'])

    return render_template('account.html', user_id=user_id, email=email, city=city, phone=phone, closet=closet, checkouts=checkouts, communities=communities)


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

