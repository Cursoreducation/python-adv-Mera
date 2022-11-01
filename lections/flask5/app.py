from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("config.Config")
app.secret_key = "blablabla"
db = SQLAlchemy()

db.init_app(app)


migrate = Migrate(app, db)

with app.app_context():
    from routes import *
    from models.models import *


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)