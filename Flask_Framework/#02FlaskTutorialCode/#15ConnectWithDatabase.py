from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_mail import Mail
import mysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/detail'
app.config['SQLALCHEMY_MODUFICATIONS'] = True
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    gmail = db.Column(db.String(120), unique=False, nullable=False)

@app.route('/')
def index():
    fname="Surendra"
    email="SPDB@gmail.com"
    entry = Contacts(name=fname, gmail=email)
    db.session.add(entry)
    db.session.commit()

    return "Succesful sending"


if __name__ == '__main__':
    app.run(debug=True)