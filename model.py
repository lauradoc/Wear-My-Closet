"""Models for Wear my Closet app"""

from flask_sqlalchemy import SQLAlchemy 

from datetime import date

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    city = db.Column(db.String)
    lat = db.Column(db.Integer, nullable=True)
    lon = db.Column(db.Integer, nullable=True)
    phone = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id}>'

class Item(db.Model):
    """An item in a user's closet"""

    __tablename__ = 'items'

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    item_name = db.Column(db.String)
    image_name = db.Column(db.String)
    category = db.Column(db.String, db.ForeignKey('categories.category_id'))
    size = db.Column(db.String)

    user = db.relationship('User', backref='items')
    category = db.relationship('Category', backref='items')

    def __repr__(self):
        return f'<Item item_id={self.item_id} user={self.user_id} name={self.item_name}>'

class Category(db.Model):
    """A category for a user's item"""

    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_name = db.Column(db.String)

class Checkout(db.Model):
    """A checkout for a user to borrow items"""

    __tablename__ = 'checkouts'

    checkout_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    checkout_date = db.Column(db.Date)
    due = db.Column(db.Date)
    return_date = db.Column(db.Date)
    checkout_status = db.Column(db.String, db.ForeignKey('statuses.checkout_status'))

    item = db.relationship('Item', backref='checkouts')
    user = db.relationship('User', backref='checkouts')
    status = db.relationship('Status', backref='checkouts')

    def __repr__(self):
        return f'<Checkout checkout_id={self.checkout_id} user={self.user_id} item={self.item_id}>'

class Status(db.Model):
    """The status of an item out for checkout"""

    __tablename__ = 'statuses'

    checkout_status = db.Column(db.String, primary_key=True)

    def __repr__(self):
        return f'<Status checkout_status={self.checkout_status}>'

class Community(db.Model):
    """Community page that users can join"""

    __tablename__ = 'communities'

    community_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    community_name = db.Column(db.String)
    location = db.Column(db.String)

    def __repr__(self):
        return f'<Community community_id={self.community_id} name={self.community_name}>'

class Community_member(db.Model):
    """Identifies what community a user is in"""

    __tablename__ = 'community_members'

    community_member_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    community_id = db.Column(db.Integer, db.ForeignKey('communities.community_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    community = db.relationship('Community', backref='community_members')
    user = db.relationship('User', backref='community_members')

    def __repr__(self):
        return f'<Community Member member_id={self.community_member_id} user={self.user_id}>'

def connect_to_db(flask_app, db_uri='postgresql:///closets', echo=False):
    """connect to database"""

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
