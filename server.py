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
        # communities = crud.get_community_by_user(session['user_id'])

        return redirect('/home')

    else:        
        flash(u'Log in failed. Try again.', 'password-error')
        return redirect('/')


@app.route('/home')
def view_home():
    """Load home page once user is logged in"""

    user_id = session.get('user_id')
    if user_id:
        user_communities = crud.get_community_by_user(user_id)
        communities = crud.get_all_communities()
        available_communities = []
        for community in communities:
            if community.community_name not in user_communities:
                available_communities.append(community)
        return render_template('home.html', user=user_id, communities=available_communities)
    else:
        return redirect('/')


@app.route('/createcommunity', methods=['POST'])
def create_community():
    """Form to create a new community"""

    community_name = request.form.get('community_name')
    location = request.form.get('location')
    if community_name:
        new_community = crud.create_community(community_name, location)

    return render_template('home.html')


@app.route('/joincommunity')
def join_community():
    """Form to join an existing community"""

    user_id = session.get('user_id')
    community_name = request.args.get('join-community')
    community_id = crud.get_community_id_by_community_name(community_name)
    new_member = crud.create_community_member(community_id, user_id)
    user_communities = crud.get_community_by_user(user_id) 

    return render_template('community.html', user_communities=user_communities)


@app.route('/community')
def view_my_community():
    """View communities based on user logged in"""

    user_id = session.get('user_id')
    user_communities = crud.get_community_by_user(user_id) 

    return render_template('community.html', user_communities=user_communities)


@app.route('/community.json')
def view_my_community_json():
    """View communities based on user logged in using json"""

    user_id = session.get('user_id')
    user_communities_json = crud.get_community_by_user_json(user_id)

    return jsonify(user_communities_json)
    

@app.route('/communitycloset.json')
def get_items_by_community_json():
    """Return items for users in selected community as json"""

    community_name = request.args.get("community")
    print(request.args)
    user_id = session.get('user_id')
    print(session)
    community_items = crud.community_details_json(community_name, user_id)
    print(community_items)

    return jsonify(community_items)

@app.route('/addtocart', methods=['POST'])
def add_to_cart():

    user_id = session.get('user_id')
    item_id = request.form.get('item_id')
    print(item_id)
    new_cart_item = crud.create_cart(item_id, user_id)
    print('item added', new_cart_item.item_id)
    item = crud.get_item_by_id(item_id)

    return f'{item.item_name} has been added to your cart!'


@app.route('/removecartitem', methods=['POST'])
def remove_from_cart():

    item_id = request.form.get('item_id')
    user_id = session.get('user_id')
    print(item_id)
    remove_item = crud.remove_item_from_cart(item_id, user_id)
    print('item removed', remove_item)
    item = crud.get_item_by_id(item_id)
    cart = crud.get_cart_by_user_json(user_id)

    return f'{item.item_name} has been removed. Refresh this page.'


@app.route('/cart')
def go_to_cart():

    return render_template('cart.html')
    

@app.route('/cartjson')
def show_cart_items():

    user_id = session.get('user_id')
    cart = crud.get_cart_by_user_json(user_id)

    return jsonify(cart)
    #get  request for all items that are on cart table for session user
    #need crud function that pulls all items in cart by user
    #cart.html to remove items

@app.route('/checkout')
def checkout():

    return render_template('checkout.html')

# @app.route('/cart', methods=['POST'])
# def checkout_item():

#     checkout = crud.get_checkout_by_user(session['user_id'])
#     item = request.form.get('checkout-items')

#     if checkout:
#         return render_template('cart.html', item=item)
#     else:
#         flash(u'No item in checkout')
#         return redirect('/mycommunity')
    

@app.route('/mycloset')
def get_closet_form():

    return render_template('mycloset.html')

@app.route('/myclosetjson')
def get_closet_data():
    """View closet of user logged in. else return to login page"""
    
    if 'user_id' in session:
        closet = crud.get_items_by_user_json(session['user_id'])
        return jsonify(closet)

    else:
        flash(u'Need to be logged in to view this page', 'login-error')
        return redirect('/')


@app.route('/addnewitem', methods=['POST'])
def upload_item():
    """Upload new item to user's closet"""

    item = request.files.get('file')
    if item:
        image_url = api.upload_closet_image(item)
        # image_thumbnail = api.get_image_thumbnail(item)
        item_name = request.form.get('item_name')
        item_description = request.form.get('item_description')
        category_name = request.form.get('category') 
        user_id = session.get('user_id')
        
        new_item = crud.create_item(user_id, item_name, item_description, image_url, category_name)

        return jsonify(crud.jsonify_item(new_item))


@app.route('/myaccount')
def account_details():
    """View user's account details"""

    user = crud.get_user_by_email(session['email'])
    user_id = user.user_id
    email = user.email
    city = user.city
    phone = user.phone
    # item = request.files.get('file')
    # image_thumbnail = api.get_image_thumbnail(item)
    closet = crud.get_image_urls_by_user(session['user_id'])
    checkouts = crud.get_cart_by_user_json(session['user_id'])
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

