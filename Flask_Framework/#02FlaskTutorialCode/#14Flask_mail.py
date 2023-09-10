import json
from flask import Flask
from flask_mail import *
app =Flask(__name__)

with open('config.json', 'r') as f:
   params = json.load(f)['params']
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = params["gmail.user"]
app.config['MAIL_PASSWORD'] = params["gmail.password"]
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello msg send successfully', sender = 'prajapatsurendra741545@gmail.com', recipients = ['prajapatsurendra78980@gmail.com'])
   msg.body = "Hello mail-sending is currectly work using flask framework"
   with app.open_resource("/home/surendra/hello_flask/clean_blog_project/static/assets/img/contact-bg.jpg") as fp:
        msg.attach("contact-bg.jpg", "image/jpg", fp.read())
   mail.send(msg)
   return "Message wass Sent"

if __name__ == '__main__':
   app.run(debug = True)