# 環境構築用後で消す
from flask import jsonify, request
from flask import Blueprint
from app.db import db, Item

develop_page = Blueprint('develop', __name__)

@develop_page.route('/')
def hello():
    return "Hello from Flask!"

@develop_page.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

@develop_page.route('/items', methods=['POST'])
def add_item():
    name = request.json['name']
    item = Item(name=name)
    db.session.add(item)
    db.session.commit()
    return jsonify(str(item)), 201

@develop_page.route("/deletItem", methods=["POST"])
def delete():
    item_id = request.json['item_id']
    item = Item.query.filter_by(id=item_id).first()
    # 取得したTodoをデータベースセッションから削除
    db.session.delete(item)
    db.session.commit()
    # タスク削除後、ホームページにリダイレクト
    return jsonify({'message': 'Item deleted successfully'}), 200

