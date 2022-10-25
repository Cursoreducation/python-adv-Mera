from flask import Flask

app = Flask(__name__)

with app.app_context():
    from routes.main import *
    from routes.plants import *


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)