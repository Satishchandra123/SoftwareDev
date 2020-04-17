from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "Registered users"
    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, primary_key=True)
    gender = db.Column(db.String, nullable=False)
    datetime = db.Column(db.String, nullable=False)