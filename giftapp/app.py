from flask import Flask, jsonify, render_template
from database.database import init_db
from database.models import User
from services import UserService

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('home.html.jinja')


@app.route("/users", methods=['GET'])
def users():
    users = UserService.get_users()
    data = jsonify([{user.id: user.name} for user in users])
    return data


if __name__ == '__main__':

    init_db()

    matt = User('Matt')
    wes = User('Wes')
    UserService.save_user(matt)
    UserService.save_user(wes)

    app.run(debug=True)


