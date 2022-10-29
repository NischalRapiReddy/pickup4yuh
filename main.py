import requests
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    url = "http://getpickuplines.herokuapp.com/lines/random"
    res = requests.get(url).json()
    line = res['line']
    return render_template("index.html", pickupLine=line)

app.run(debug=False, host='0.0.0.0')