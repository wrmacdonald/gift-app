from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = '/Users/mmmatt/Documents/software projects/GiftPlannerApp/gift-app/development.db'
# db = SQLAlchemy(app)
#
# @app.route("/")
# def hello_world():
#     return render_template('home.html.jinja')
#
#
# # model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#

if __name__ == '__main__':
    app.run()
