from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Configuration


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://datastore:5432/postgres_db'
db = SQLAlchemy(app)
