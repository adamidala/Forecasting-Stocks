from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'jean et adam'

app.run(host='0.0.0.0', port=3000)