from socialmediabot import db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from socialmediabot import login


@login.user_loader
def load_user(id):
    """
    Returns User object given an id
    :param id: id of user object in db
    :return: a User object identified by id
    """
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship("Post", backref = "author", lazy = "dynamic")
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User {}>".format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    twitter = db.Column(db.Boolean)
    facebook = db.Column(db.Boolean)
    instagram = db.Column(db.Boolean)
    posted = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return "<Post {}>".format(self.body)

