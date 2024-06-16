from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Rezept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anleitung = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(50))
    zeit = db.Column(db.Integer)
    schwierigkeit = db.Column(db.String(50))  # Annahme, dass `schwierigkeit` ein String ist
    kategorie_name = db.Column(db.String, db.ForeignKey('kategorie.name'))
    bewertung = db.Column(db.Float)
    zutaten= db.relationship('Zutat', backref='rezept')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.Integer, unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    rezepte = db.relationship('Rezept', backref='user')

class Kategorie(db.Model):
    name = db.Column(db.String(20), primary_key=True)   

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Zutat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    menge = db.Column(db.Float)

class Bewertung(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rezept_id = db.Column(db.Integer, db.ForeignKey('rezept.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    bewertung = db.Column(db.Integer)



