from configparser import ConfigParser
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

config = ConfigParser()
config.read('config/configuration.conf')
db_options = dict(config['DATABASE'])
app.config['SQLALCHEMY_DATABASE_URI'] = db_options['sqlite_connection_string']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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


@app.route("/users", methods=['GET'])
def users():
    users = get_users()
    data = jsonify([{user.id: user.name} for user in users])
    return data


# services
def get_users():
    return User.query.all()


def save_user(user):
    db.session.add(user)
    db.session.commit()
    return user


# test code
if __name__ == '__main__':

    db.drop_all()
    db.create_all()

    matt = User('Matt')
    wes = User('Wes')
    save_user(matt)
    save_user(wes)
    
    app.run(debug=True)



