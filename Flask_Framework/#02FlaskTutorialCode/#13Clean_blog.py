from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():

    return render_template('#1index.html')

@app.route("/about")
def harry():
    return render_template('about.html', name2= )

@app.route("/contact")
def contact():
    return render_template('contact.html')

app.run(debug=True)
