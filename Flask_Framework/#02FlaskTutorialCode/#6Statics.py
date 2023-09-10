from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/surendra")
def surendra():
    return "Hello Surendra Prajapat"

app.run(debug=True)
