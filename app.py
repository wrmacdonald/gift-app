import configparser
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config/configuration.conf')
db_options = dict(config['DATABASE'])
app.config['SQLALCHEMY_DATABASE_URI'] = db_options['sqlite_connection_string']
db = SQLAlchemy(app)


# model
class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name: str):
        self.name = name


db.drop_all()
db.create_all()

# routes
@app.route("/")
def hello_world():
    return render_template('home.html.jinja', users=User.query.all())


if __name__ == '__main__':
    user = User('Wes')
    db.session.add(user)
    db.session.commit()
    for user in User.query.all():
        print(f'id: {user.id} name: {user.name}')
    app.run(debug=True)



