from flask import Flask
app = Flask('/')

@app.route('/')
def index():
    str="""
<html>
<body>
<h1>Hello Surendra</h1>
<p>Welcome To Surendra URl in Flask framework</p>
</body>
</html>
"""

    return str

if __name__ == "__main__":
     app.run(debug=True)
