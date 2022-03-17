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


# # model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# routes
@app.route("/")
def hello_world():
    return render_template('home.html.jinja')


if __name__ == '__main__':
    app.run(debug=True)
