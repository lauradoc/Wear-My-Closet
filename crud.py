"""CRUD operations. Utility functions for creating data"""

from model import db, User, Category, Item, Checkout, Status, Community, CommunityMember, connect_to_db


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

    return User.query.get(user_id)


def create_category(category_name):
    """Create and return category name."""

    category_name = Category(category_name=category_name)

    db.session.add(category_name)
    db.session.commit()

    return category_name


def create_item(user_id, item_name, image_url, category_name):
    """Create and return a new item."""

    item = Item(user_id=user_id, item_name=item_name, image_url=image_url, category_name=category_name)

    db.session.add(item)
    db.session.commit()

    return item

# def create_item_json(user_id, item_name, image_url, category_name):
#     """Create item and return new item as json"""

#     new_item_json = []

#     item = Item(user_id=user_id, item_name=item_name, image_url=image_url, category_name=category_name)

#     db.session.add(item)
#     db.session.commit()

#     item_dict = {
#             "user": item.user_id,
#             "item_name": item.item_name,
#             "image_url": item.image_url,
#             "category": item.category_name,
#         }
#     new_item_json.append(item_dict)

#     return new_item_json


def get_item_by_item_name(item_name):
    """takes in item name and return item if exists, otherwise returns none"""

    return Item.query.filter_by(item_name=item_name).first()
    

def get_image_urls_by_user(user_id):
    """takes in user_id and returns urls of all items under that user"""

    all_item_urls = db.session.query(Item.image_url)
    user_items = all_item_urls.filter(Item.user_id==user_id)

    return user_items.all()


def get_items_by_user(user_id):

    return Item.query.filter(Item.user_id==user_id).all()


def get_items_by_user_json(user_id):

    item_details_json = []
    closet = Item.query.filter(Item.user_id==user_id).all()
    for item in closet:
        item_dict = {
                "id": item.item_id,
                "user": item.user_id,
                "item_name": item.item_name,
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

def create_checkout(item_id, user_id, checkout_date, due, return_date, checkout_status):
    """Create and return checkout for item"""

    checkout = Checkout(item_id=item_id, user_id=user_id, checkout_date=checkout_date, due=due, return_date=return_date, checkout_status=checkout_status)

    db.session.add(checkout)
    db.session.commit()

    return checkout

def get_checkout_by_user(user_id):
    """Return all checkouts from user"""

    return Checkout.query.filter(Checkout.user_id==user_id)

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
                "image_url": item.image_url,
                "category": item.category_name,
            }
            user_items_json.append(item_dict)

    return user_items_json


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    