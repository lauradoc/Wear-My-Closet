"""Server for Wear my Closet app"""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db
import crud
import api
import send_sms

from jinja2 import StrictUndefined
from datetime import date


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
        flash(u'Email already exists. Please make an account with a different email', 'error-message')

    else:
        user = crud.create_user(first_name, last_name, email, password, city, phone)
        session['email'] = user.email
        session['user_id'] = user.user_id
        flash(u'Your account was created successfully! You can now log in.', 'error-message')

    return redirect('/')


@app.route('/login', methods=['POST'])
def handle_login():
    """Check to see if password matches and log user in"""

    email = request.form.get('email')
    password = request.form.get('password')
    print(password)
    user = crud.get_user_by_email(email)

    if password == '' or email == '':
        flash(u'Log in failed. Try again.', 'error-message')
        return redirect('/')

    if password in user.password:
        session['email'] = user.email
        session['user_id'] = user.user_id
        return redirect('/home')

    else:        
        flash(u'Log in failed. Try again.', 'error-message')
        return redirect('/')


@app.route('/home')
def view_home():
    """Load home page once user is logged in"""

    user_id = session.get('user_id')
    if user_id:
        user_community_names = []
        user_communities = crud.get_community_by_user(user_id)
        for community in user_communities:
            user_community_names.append(community.community.community_name)
        communities = crud.get_all_communities()
        available_communities = []
        for community in communities:
            if community.community_name not in user_community_names:
                available_communities.append(community)
        return render_template('home.html', user=user_id, communities=available_communities, user_communities=user_communities)
    else:
        flash(u'Must be logged in to view this page.', 'error-message')
        return redirect('/')


@app.route('/createcommunity', methods=['POST'])
def create_community():
    """Form to create a new community"""

    community_name = request.form.get('community_name')
    community_description = request.form.get('community_description')
    if community_name:
        new_community = crud.create_community(community_name, community_description=community_description)

    return redirect('/home')


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
    if user_id:
        user_communities = crud.get_community_by_user(user_id) 
        return render_template('community.html', user_communities=user_communities)
    
    else:
        flash(u'Must be logged in to view this page.', 'error-message')
        return redirect('/')
    

@app.route('/communitycloset.json')
def get_items_by_community_json():
    """Return items for users in selected community as json"""

    user_id = session.get('user_id')

    if user_id:
        community_name = request.args.get("community")
        community_items = crud.community_details_json(community_name, user_id)

        return jsonify(community_items)

    else:
        flash(u'Must be logged in to view this page.', 'error-message')
        return redirect('/')

@app.route('/addtocart', methods=['POST'])
def add_to_cart():
    """New item added to cart"""

    user_id = session.get('user_id')
    item_id = request.form.get('item_id')
    print(item_id)
    new_cart_item = crud.create_cart(item_id, user_id)
    print('item added', new_cart_item.item_id)
    item = crud.get_item_by_id(item_id)

    return f'{item.item_name} has been added to your cart!'


@app.route('/removecartitem', methods=['POST'])
def remove_from_cart():
    """Removes item from cart table"""

    item_id = request.form.get('item_id')
    user_id = session.get('user_id')
    remove_item = crud.remove_item_from_cart(item_id, user_id)
    item = crud.get_item_by_id(item_id)
    cart = crud.get_cart_by_user_json(user_id)

    return f'{item.item_name} has been removed.'


@app.route('/cart')
def go_to_cart():

    user_id = session.get('user_id')

    if user_id:
        return render_template('cart.html')
    
    else:
        flash(u'Must be logged in to view this page.', 'error-message')
        return redirect('/')
    

@app.route('/cartjson')
def show_cart_items():

    user_id = session.get('user_id')
    cart = crud.get_cart_by_user_json(user_id)

    return jsonify(cart)


@app.route('/checkout', methods=['POST'])
def create_checkout_item():
    
    user_borrowed_by = session.get('user_id')
    checkout_date = date.today()
    new_checkout = crud.create_checkout(user_borrowed_by, checkout_date)
    session['checkout_id'] = new_checkout.checkout_id

    checkout_id = session.get('checkout_id')
    item_ids = request.form.getlist('item-id')
    for item_id in item_ids:
        item_due_date = request.form.get(f'due-date-{item_id}')
        new_checkout_item = crud.create_checkout_item(checkout_id, item_id, item_due_date)
        checkout_items = crud.get_checkout_items_by_checkout_id_json(checkout_id)
        remove_from_cart = crud.remove_item_from_cart(f'{item_id}', session['user_id'])
        send_message = send_sms.send_message_to_user(new_checkout_item)
        new_status = crud.change_item_status(item_id)
    
    return jsonify(checkout_items)


@app.route('/mycloset')
def get_closet_form():

    user_id = session.get('user_id')
    if user_id:
        # import pdb; pdb.set_trace()
        # crud.set_items_status([1,2], "Unavailable")
        # crud.set_items_status([1,2], "Available")

        return render_template('mycloset.html')

    else:
        flash(u'Must be logged in to view this page.', 'error-message')
        return redirect('/')


@app.route('/mycloset', methods=['POST'])
def update_item_status():
    
    item_id = request.form.get('item-id')
    item_update = crud.change_item_status(item_id)
    json_item = crud.jsonify_item(item_update)

    return redirect('/mycloset')

@app.route('/myclosetjson')
def get_closet_data():
    """View closet of user logged in. else return to login page"""
    
    if 'user_id' in session:
        closet = crud.get_items_by_user_json(session['user_id'])
        return jsonify(closet)

    else:
        flash(u'Need to be logged in to view this page', 'error-message')
        return redirect('/')


@app.route('/addnewitem', methods=['POST'])
def upload_item():
    """Upload new item to user's closet"""

    item = request.files.get('file')
    if item:
        image_url = api.upload_closet_image(item)
        item_name = request.form.get('item_name')
        item_description = request.form.get('item_description')
        category_name = request.form.get('category') 
        user_id = session.get('user_id')
        status = "Available"
        
        new_item = crud.create_item(user_id, item_name, item_description, image_url, category_name, status)

        return jsonify(crud.jsonify_item(new_item))


@app.route('/myaccount')
def account_details():
    """View user's account details"""

    email = session.get('email')

    if email:
        user = crud.get_user_by_email(session['email'])
        user_id = user.user_id
        city = user.city
        phone = user.phone
        closet = crud.get_items_by_user(user_id)
        checkout_items = crud.get_checkout_item_ids_by_user(user_id)
        communities = crud.get_community_by_user(user_id)

        return render_template('account.html', user_id=user_id, email=email, city=city, phone=phone, closet=closet, checkout_items=checkout_items, communities=communities)

    else:
        flash(u'Must be logged in to view this page.', 'error-message')
        return redirect('/')

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

