from flask_sqlalchemy import SQLAlchemy
from Event import db
from flask.views import MethodView

class User(db.Model):
    __tablename__ = "user"
    
    user_id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    avatar = db.Column(db.String(200), nullable=False)


    def __init__(self, display_name, email, avatar):
        self.display_name = display_name

        self.email = email
        self.avatar = avatar

    def __repr__(self):
        return f'Display Name: {self.display_name}, Email: {self.email}'

    # safely add record/object to db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    # safely update record/object in db
    def update(self):
        db.session.commit()

    # safely delete record/object from db
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # output object properties in clean dict format
    def format(self):
        return {
            "user_id": self.user_id,
            "display_name": self.display_name,
            "email": self.email,
            "avatar": self.avatar
        }


class Event(db.Model):
    __tablename__ = "event"

    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey(
        "user.user_id"), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    start_at = db.Column(db.DateTime(), nullable=False)
    end_at = db.Column(db.DateTime(), nullable=False)
    thumbnail = db.Column(db.String(200), nullable=False)

    def __init__(self, title, description, creator, location, start_at, end_at, thumbnail):
        self.title = title
        self.description = description
        self.creator = creator
        self.location = location
        self.start_at = start_at
        self.end_at = end_at
        self.thumbnail = thumbnail

    def __repr__(self):
        return f'Title: {self.title}, Description: {self.description}, Creator: {self.creator}, Location: {self.location}, Starts: {self.start_at}, Ends: {self.end_at}'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "event_id": self.event_id,
            "title": self.title,
            "description": self.description,
            "creator": self.creator,
            "location": self.location,
            "start_at": self.start_at,
            "end_at": self.end_at,
            "thumbnail": self.thumbnail
        }

class EventComment(db.Model):
    """Model schema for the comments in the events section"""
    __tablename__ = "eventcomments"

    id = db.Column(db.Integer, primary_key = True) # Primary Table Key
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    body = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False) # Timestamp column
    
    #Add relationships to Event and User models
    event = db.relationship('Event', backref=db.backref('comments', lazy = True))
    user = db.relationship('User', backref=db.backref('comments', lazy=True))


    def __init__(self,event_id,user_id, body, image):
        self.body = body
        self.image = image
        self.event_id = event_id
        self.user_id = user_id

    def __repr__(self):
        return f'event_id: {self.event_id}, user_id: {self.user_id}, body: {self.body}, image: {self.image}'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "event_id": self.event_id,
            "user_id": self.user_id,
            "body": self.body,
            "image": self.image
        }    
