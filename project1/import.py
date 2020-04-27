import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = "Books"
    id = db.Column(db.Integer,primary_key=True)
    isbn = db.Column(db.String,unique= True, nullable=False)
    title = db.Column(db.String,unique= False, nullable=False)
    author = db.Column(db.String,nullable=False)
    year = db.Column(db.Integer,nullable=False)

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

db.init_app(app)
def main():
    db.create_all()
    with open("books.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            newBook = Book(row[0],row[1],row[2], int(row[3]))
            db.session.add(newBook)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
