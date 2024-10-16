from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS設定を追加

@app.route('/')
def hello():
    print("api送れたよー!")
    return "Hello from Flask!"
