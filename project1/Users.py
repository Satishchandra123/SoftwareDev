from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):

    __tablename__ = "Registered users"
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, primary_key=True)
    gender = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    datetime = db.Column(db.String, nullable=False)