"""CRUD operations. Utility functions for creating data"""

from model import db, User, Item, Checkout, Status, Community, Community_member, connect_to_db


def create_user(email, password, city, phone):
    """Create and return a new user."""

    user = User(email=email, password=password, city=city, phone=phone)

    db.session.add(user)
    db.session.commit()

    return user


def create_item(user_id, category, item_name, image_name):
    """Create and return a new item."""

    item = Item(user_id=user_id, category=category, item_name=item_name, image_name=image_name)

    db.session.add(item)
    db.session.commit()

    return item


def create_status(status):
    """Create and return checkout status"""

    return status

def create_checkout(item_id, user_id, checkout_date, due, return_date, checkout_status):
    """Create and return checkout for item"""

    checkout = Checkout(item_id=item_id, user_id=user_id, checkout_date=checkout_date, due=due, return_date=return_date, checkout_status=checkout_status)

    db.session.add(checkout)
    db.session.commit()

    return checkout


def create_community(community_name, location):
    """Create and return new community"""

    community = Community(community_name=community_name, location=location)

    db.session.add(community)
    db.session.commit()

    return community


def create_community_member(community_id, user_id):
    """Create and return members of community"""

    community_member = Community_member(community_id=community_id, user_id=user_id)

    db.session.add(community_member)
    db.session.commit()

    return community_member


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    