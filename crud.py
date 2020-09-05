"""CRUD operations. Utility functions for creating data"""

from model import db, User, Category, Item, Checkout, CheckoutItem, Cart, Status, Community, CommunityMember, connect_to_db

def create_user(first_name, last_name, email, password, city, phone):
    """Creates new user for login page"""

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
    """Create and return category name to seed data"""

    category_name = Category(category_name=category_name)

    db.session.add(category_name)
    db.session.commit()

    return category_name


def create_item(user_id, item_name, item_description, image_url, category_name, status_code):
    """Create and return a new item to seed data and for item upload page"""

    item = Item(user_id=user_id, item_name=item_name, item_description=item_description, image_url=image_url, category_name=category_name, status_code=status_code)

    db.session.add(item)
    db.session.commit()

    return item


def jsonify_item(item):
    """jsonify item data to use in js to view closet items"""

    json_item = {
            "id": item.item_id,
            "user": item.user_id,
            "item_name": item.item_name,
            "item_description": item.item_description,
            "image_url": item.image_url,
            "category": item.category_name,
            "status": item.status_code
        }

    return json_item

def change_item_status(item_id, status):
    """update item status when there is a manual change by user or item as been added to cart"""

    item = Item.query.filter(Item.item_id==item_id).first()
    item.status_code = status

    db.session.commit()

    return item


def set_items_status(item_ids, new_status):

    old_status = "available" if new_status == "checked_out" else "checked_out"

    # db.session.query(Item).filter_by(status_code=old_status).update({"name": user.name})

    rows_updated = db.session.query().filter(
        Item.status_code == old_status, Item.item_id.in_(item_ids)
    ).update(
        {"status_code": new_status}, synchronize_session=False
    )
    import pdb; pdb.set_trace()
    db.session.commit()

    return rows_updated

def get_item_by_item_name(item_name):
    """takes in item name and return item if exists, otherwise returns none"""

    return Item.query.filter_by(item_name=item_name).first()


def get_item_by_id(item_id):
    """gets item by primary key"""

    return Item.query.get(item_id)


def get_image_urls_by_user(user_id):
    """takes in user_id and returns iamge urls of all items under that user"""

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
                "status": item.status_code
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
    """find all items that have been added to cart by session user, but not yet transitioned to checkout or been removed from cart"""

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
            "id": cart_item.item_id,
            "user": cart_item.user_id,
            "item_name": cart_item.item.item_name,
            "image_url": cart_item.item.image_url,
            "status": cart_item.item.status_code
        }
        cart_items_json.append(cart_item_dict)

    return cart_items_json


def remove_item_from_cart(item_id, user_id):
    """Removes item from existing cart"""
    
    remove_item = Cart.query.filter(Cart.item_id==item_id, Cart.user_id==user_id).first()

    db.session.delete(remove_item)
    db.session.commit()

    return remove_item


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
            'user_borrowed_by': checkout.user_borrowed_by,
            'checkout_date': checkout.checkout_date
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


def get_all_checkout_item_ids():

    checkout_item_ids = []
    all_checkout_items = CheckoutItem.query.all()
    for item in all_checkout_items:
        checkout_item_ids.append(item.item_id)

    return checkout_item_ids


def get_checkout_item_ids_by_user(user_id):

    user_checkout_items = []
    user_checkouts = Checkout.query.filter(Checkout.user_borrowed_by==user_id).all()
    print(user_checkouts)
    for checkout in user_checkouts:
        checkout_id = checkout.checkout_id
        checkout_item = CheckoutItem.query.filter(CheckoutItem.checkout_id==checkout_id).all()
        for item in checkout_item:
            user_checkout_items.append(item)

    return user_checkout_items


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

def create_community(community_name, community_description):
    """Create and return new community"""

    community = Community(community_name=community_name, community_description=community_description)

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

    return CommunityMember.query.filter(CommunityMember.user_id==user_id).all() 


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
    