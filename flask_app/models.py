from __init__ import db, login_manager

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from time import time
from datetime import datetime
import jwt 



followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    user_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    
    
    #Profile page functionality 
    about_me = db.Column(db.String(140), nullable = True)
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.user_name} {self.email} {self.password} {self.about_me}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def get_reset_token(self, user_id):
        try:
            payload = {
                'reset_password': datetime.datetime.utcnow() + datetime.timedelta(seconds=10),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            print('encode: ', jwt.encode(
                payload,
                key=os.getenv('SECRET_KEY'),
                algorithm='HS256'
            ))
            return jwt.encode(
                payload,
                key=os.getenv('SECRET_KEY'),
                algorithm='HS256'
            )

        except Exception as e:
            return e

    @staticmethod
    def verify_email(email):

        user = User.query.filter_by(email=email).first()

        return user

    @staticmethod
    def verify_reset_token(token):
        try:
            payload = jwt.decode(token, key=os.getenv('SECRET_KEY'), algorithm='HS256')
            print('payload: ', payload)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Login in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.email} {self.password}"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
