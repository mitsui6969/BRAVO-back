from app.app import app
from app.db import init_db

init_db(app)

if __name__ == '__main__':
    app.run(port=5000)