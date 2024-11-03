from flask import jsonify, request
from flask import Blueprint
from app.db import db, Choices
import json
import os


story_page = Blueprint('story', __name__)

@story_page.route('/story/3', methods=['GET'])
def send_chapter3():
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'story', 'chapter3.json')

    # JSONファイルを読み込んで返す
    with open(file_path, 'r', encoding='utf-8') as file:
        chapter3_data = json.load(file)
    
    return jsonify(chapter3_data)