from flask import jsonify, request
from flask import Blueprint
from app.db import db, Choices
import json
import os


story_page = Blueprint('story', __name__)

@story_page.route('/story/<int:chapter_id>', methods=['GET'])
def send_chapter(chapter_id):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'story', f'chapter{chapter_id}.json')

    # JSONファイルを読み込んで返す
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            chapter3_data = json.load(file)
        
        return jsonify(chapter3_data)
    else:
        return jsonify({"error": "Chapter not found"}), 404
    

@story_page.route('/story/save', methods=['POST'])
def save_branch():
    data = request.get_json()
    print("受信したデータ:", data)

    choice_num = data.get('choice')
    chapter_num = data.get('chapter')

    # choice_num = request.json['choice']
    # chapter_num = request.json['chapter']
    new_choices = Choices(choice=choice_num, chapter=chapter_num)
    db.session.add(new_choices)
    db.session.commit()
    return jsonify(str(new_choices)), 201
