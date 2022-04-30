from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():

    return "adam et jean"

app.run(host='0.0.0.0', port=81)
