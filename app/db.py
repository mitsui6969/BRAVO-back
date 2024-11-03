# データベース関連
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Item {self.name}>'


class Choices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    choice = db.Column(db.String(80), nullable=False)

    def __init__(self, choice):
        self.choice = choice

    def __repr__(self):
        return f'<Choices {self.index}>'

# データベースの初期化
def init_db(app):
    with app.app_context():
        db.create_all()
