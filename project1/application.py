import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import render_template, request
from Users import *
from datetime import datetime

app = Flask(__name__)

# # Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# # Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register",methods=["GET","POST"])
def register():
    if(request.method == "POST"):
        Users.query.all()
        name = request.form.get("name")
        pwd = request.form.get("pwd")
        email = request.form.get("email")
        gender = request.form.get("gender")
        user_details = Users(name= name, email= email, gender= gender,password= pwd,datetime = datetime.now())
        try:
            db.session.add(user_details)
            db.session.commit()
            print("name : " ,name)
            print("password : ",pwd)
            print("email: ",email)
            print("gender: ",gender)
            return render_template("hello.html", name=name)
        except Exception:
            return render_template("errorpage.html")
    return render_template("Register.html")

@app.route("/admin")
def table():
    users = Users.query.all()
    return render_template("admin.html",user_details=users)

@app.route("/auth")
def login():
    if(request.method == "POST"):
        if not request.form.get("username"):
            return render_template("loginerror.html")
        elif not request.form.get("email"):
            return render_template("loginerror.html")
        elif not request.form.get("password")
            return render_template("loginerror.html")

