from app import app
from flask import Flask
from flask import render_template


@app.route('/')
def main():
    return render_template('calc_main.html')


@app.route('/calc/<int:x>/<int:y>')
def calc_sum(x, y):
    return render_template('calc.html', x=x, sign='+', y=y, res=x+y)