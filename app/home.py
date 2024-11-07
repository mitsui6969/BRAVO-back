from flask import jsonify
from flask import Blueprint
from app.db import db, Choices


home_page = Blueprint('home', __name__)

@home_page.route('/home', methods=["GET"])
def chapter_data():
    datas = Choices.query.all()
    return jsonify([{'chapter': data.chapter, 'choice': data.choice} for data in datas])


@home_page.route("/home/reset", methods=["POST"])
def reset_chapter():
    datas = Choices.query.all()

    # 全てのデータをデータベースセッションから削除
    if datas:
        for data in datas:
            db.session.delete(data)
    
        db.session.commit()
    # タスク削除後、ホームページにリダイレクト
    return jsonify({'message': 'Datas deleted successfully'}), 200