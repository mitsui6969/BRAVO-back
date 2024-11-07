from flask import jsonify, request
from flask import Blueprint
from app.db import db, Choices
import json
import os


end_page = Blueprint('end', __name__)

@end_page.route('/end')
def send_end():
    # 今までの選択を取得
    load_map = ""
    for chapter_num in range(1,6):
        choice_record = Choices.query.filter_by(chapter=chapter_num).first()
        if choice_record:
            load_map += str(choice_record.choice)
        else:
            load_map += ""

    # 分岐
    if load_map == "1111":
        end_id = 1
    elif load_map == "2222":
        end_id = 2
    elif load_map == "1121":
        end_id = 4
    elif load_map == "2212":
        end_id = 5
    else:
        end_id = 3

    # JSONファイルを読み込んで返す
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'end', 'end.json')

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            end_data = json.load(file)
        
        return jsonify({"json_file": end_data, "end_id": end_id-1})
    else:
        return jsonify({"error": "Chapter not found"}), 404
