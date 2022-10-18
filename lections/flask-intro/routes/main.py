from app import app
from flask import render_template


@app.route('/')
def hello():
    return "hello world"


@app.route("/keklol")
def keklol():
    return "Hello this is really kek!"


@app.route("/hello/<string:name>/<string:last_name>")
def hello_user(name, last_name):
    return render_template("index.html", name=name, last_name=last_name)


# @app.route("/news/<int:id>")
# def news(id):
#     #news= SELECT * FROM news WHERE id=id
#     return news