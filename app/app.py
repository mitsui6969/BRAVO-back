from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.database import db, Item

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello():
    return "Hello from Flask!"

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([str(item) for item in items])

@app.route('/items', methods=['POST'])
def add_item():
    name = request.json['name']
    item = Item(name=name)
    db.session.add(item)
    db.session.commit()
    return jsonify(str(item)), 201

db.init_app(app)
