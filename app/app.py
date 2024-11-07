# ここに集結させる
from flask import Flask
from flask_cors import CORS
from app.db import db
from app.develop import develop_page
from app.story import story_page
from app.home import home_page
from app.end import end_page

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(develop_page)
app.register_blueprint(story_page)
app.register_blueprint(home_page)
app.register_blueprint(end_page)

db.init_app(app)
