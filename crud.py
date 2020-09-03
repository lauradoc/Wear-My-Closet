"""CRUD operations. Utility functions for creating data"""

from model import db, User, Category, Item, Checkout, CheckoutItem, Cart, Status, Community, CommunityMember, connect_to_db

def create_user(first_name, last_name, email, password, city, phone):
    """Create and return a new user."""

    user = User(first_name=first_name, last_name=last_name, email=email, password=password, city=city, phone=phone)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """takes in email and returns user if exists, otherwise returns none"""
    
    return User.query.filter(User.email==email).first()

def get_user_by_user_id(user_id):
    """Gets primary key from user table and returns it"""

    return User.query.get(user_id)


def create_category(category_name):
    """Create and return category name."""

    category_name = Category(category_name=category_name)

    db.session.add(category_name)
    db.session.commit()

    return category_name


def create_item(user_id, item_name, item_description, image_url, category_name, status_code):
    """Create and return a new item."""

    item = Item(user_id=user_id, item_name=item_name, item_description=item_description, image_url=image_url, category_name=category_name, status_code=status_code)

    db.session.add(item)
    db.session.commit()

    return item


def jsonify_item(item):
    """jsonify item data to use in js"""

    json_item = {
            "id": item.item_id,
            "user": item.user_id,
            "item_name": item.item_name,
            "item_description": item.item_description,
            "image_url": item.image_url,
            "category": item.category_name,
        }

    return json_item


def get_item_by_item_name(item_name):
    """takes in item name and return item if exists, otherwise returns none"""

    return Item.query.filter_by(item_name=item_name).first()


def get_item_by_id(item_id):
    """gets item by primary key"""

    return Item.query.get(item_id)


def get_image_urls_by_user(user_id):
    """takes in user_id and returns urls of all items under that user"""

    all_item_urls = db.session.query(Item.image_url)
    user_items = all_item_urls.filter(Item.user_id==user_id)

    return user_items.all()


def get_items_by_user(user_id):
    """Gets all items for specific user"""

    return Item.query.filter(Item.user_id==user_id).all()


def get_items_by_user_json(user_id):
    """Returns json for items for specific user to use in js"""

    item_details_json = []
    closet = Item.query.filter(Item.user_id==user_id).all()
    for item in closet:
        item_dict = {
                "id": item.item_id,
                "user": item.user_id,
                "item_name": item.item_name,
                "item_description": item.item_description,
                "image_url": item.image_url,
                "category": item.category_name,
            }
        item_details_json.append(item_dict)

    return item_details_json


def create_status(checkout_status):
    """Create and return checkout status"""

    checkout_status = Status(checkout_status=checkout_status)

    db.session.add(checkout_status)
    db.session.commit()

    return checkout_status


def create_cart(item_id, user_id):
    """Create and return item that has been added to cart by session user"""

    cart = Cart(item_id=item_id, user_id=user_id)

    db.session.add(cart)
    db.session.commit()

    return cart

def get_cart_ids_by_user(user_id):

    cart_ids = []
    user_carts = Cart.query.filter(Cart.user_id==user_id).all()
    for cart in user_carts:
        cart_ids.append(cart.item_id)

    return cart_ids

def get_cart_by_user_json(user_id):
    """Return all cart items from user"""

    cart_items_json = []
    cart_items = Cart.query.filter(Cart.user_id==user_id)

    for cart_item in cart_items:
        cart_item_dict = {
            # "username": user.first_name + ' ' + user.last_name,
            "id": cart_item.item_id,
            "user": cart_item.user_id,
            "item_name": cart_item.item.item_name,
            # "item_description": item.item_description,
            "image_url": cart_item.item.image_url,
            # "category": item.category_name,
            "status": cart_item.item.status_code
        }
        cart_items_json.append(cart_item_dict)

    return cart_items_json


def remove_item_from_cart(item_id, user_id):
    """Removes item from existing cart"""
    
    remove_item = Cart.query.filter(Cart.item_id==item_id).first()

    db.session.delete(remove_item)
    db.session.commit()

    return Cart.query.filter(Cart.user_id==user_id)


def create_checkout(user_borrowed_by, checkout_date):
    """Create and return checkout for item"""

    checkout = Checkout(user_borrowed_by=user_borrowed_by, checkout_date=checkout_date)

    db.session.add(checkout)
    db.session.commit()

    return checkout


def get_checkout_by_user_json(user_borrowed_by):
    """Gets all checkouts for session user and turns into json for js"""

    checkout_json = []
    checkout_items = Checkout.query.filter(Checkout.user_borrowed_by==user_borrowed_by)

    for checkout in checkout_items:
        checkout_dict = {
            # 'item_id': checkout.item_id,
            'user_borrowed_by': checkout.user_borrowed_by,
            'checkout_date': checkout.checkout_date
            # 'due_date': checkout.due_date
        }
        checkout_json.append(checkout_dict)

    return checkout_json

def get_checkout_by_user(user_borrowed_by):

    return Checkout.query.filter(Checkout.user_borrowed_by==user_borrowed_by).all()
    
def create_checkout_item(checkout_id, item_id, due_date):
    """Creating individual checkout item that is associated with whole checkout"""
    
    checkout_item = CheckoutItem(checkout_id=checkout_id, item_id=item_id, due_date=due_date)

    db.session.add(checkout_item)
    db.session.commit()

    return checkout_item

def get_all_checkout_items_by_user(user_id):

    return CheckoutItem.query.filter(CheckoutItem.user_id==user_id).all()

def get_checkout_items_by_checkout_id_json(checkout_id):

    checkout_item_json = []
    all_checkout_items = CheckoutItem.query.filter(CheckoutItem.checkout_id==checkout_id)

    for checkout_item in all_checkout_items:
        checkout_item_dict = {
            'checkout_id': checkout_item.checkout_id,
            'item_id': checkout_item.item_id,
            'item_name': checkout_item.item.item_name,
            'checkout_date': checkout_item.checkout.checkout_date,
            'due_date': checkout_item.due_date
        }
        checkout_item_json.append(checkout_item_dict)

    return checkout_item_json

def get_all_checkout_ids():

    checkout_item_ids = []
    all_checkout_items = CheckoutItem.query.all()
    for checkout in all_checkout_items:
        checkout_item_ids.append(checkout.item_id)

    return checkout_item_ids

def create_community(community_name, location):
    """Create and return new community"""

    community = Community(community_name=community_name, location=location)

    db.session.add(community)
    db.session.commit()

    return community

def get_community_id_by_community_name(community_name):
    """return community_id from community_name"""

    name = Community.query.filter_by(community_name=community_name).first()

    return name.community_id

def get_all_communities():
    """Return all communities in db"""

    return Community.query.all()

def get_all_community_names():

    community_names = []
    communities = Community.query.all()
    for community in communities:
        community_names.append(community.community_name)
        
    return community_names


def create_community_member(community_id, user_id):
    """Create and return members of community"""

    community_member = CommunityMember(community_id=community_id, user_id=user_id)

    db.session.add(community_member)
    db.session.commit()

    return community_member

def get_community_by_user(user_id):

    user_communities = []
    communities = db.session.query(CommunityMember, Community).join(Community)
    for commem, com in communities:
        if commem.user_id == user_id:
            user_communities.append(com.community_name)

    return user_communities


def get_community_by_user_json(user_id):

    user_communities_json = []
    communities = db.session.query(CommunityMember, Community).join(Community)
    for commem, com in communities:
        if commem.user_id == user_id:
            user_communities_json.append(com.community_name)

    return user_communities_json

def get_users_by_community(community_name):
#could change to community_id
    community = Community.query.filter(Community.community_name==community_name).first()
    if community:
        return community.members
    else:
        return []


def community_details_json(community_name, user_id):
    """Return community details as JSON"""

    user_items_json = []
    community_users = get_users_by_community(community_name)
    for user in community_users: 
        closet = user.items
        for item in closet:
            item_dict = {
                "username": user.first_name + ' ' + user.last_name,
                "id": item.item_id,
                "user": item.user_id,
                "item_name": item.item_name,
                "item_description": item.item_description,
                "image_url": item.image_url,
                "category": item.category_name,
                "status": item.status_code
            }
            user_items_json.append(item_dict)

    return user_items_json


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    