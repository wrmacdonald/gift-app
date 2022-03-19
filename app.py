from configparser import ConfigParser
from flask import Flask, jsonify
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

config = ConfigParser()
config.read('config/configuration.conf')
db_options = dict(config['DATABASE'])
app.config['SQLALCHEMY_DATABASE_URI'] = db_options['sqlite_connection_string']

db = SQLAlchemy(app)


# models
class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name: str):
        self.name = name


# routes
@app.route("/")
def hello_world():
    return render_template('home.html.jinja')


@app.route("/users")
def users():
    users = get_users()
    return jsonify([{user.id: user.name} for user in users])


# services
def get_users() -> object:
    return User.query.all()


if __name__ == '__main__':

    db.drop_all()
    db.create_all()

    user = User('Wes')
    db.session.add(user)
    db.session.commit()
    
    app.run(debug=True)



