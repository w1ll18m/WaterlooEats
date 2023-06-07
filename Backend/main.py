from flask import Flask, Blueprint, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from os import path

DB_NAME = 'waterlooeats.db'
SECRET_KEY = 'temporary_key'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SECRET_KEY'] = SECRET_KEY

from database import product

db = SQLAlchemy(app)

if not path.exists('instance/' + DB_NAME):
    with app.app_context():
        db.create_all()
    print("Created Database")

@app.route('/')
def home():
    return "This is just to test various features"

if __name__ == '__main__':
    app.run(debug=True)