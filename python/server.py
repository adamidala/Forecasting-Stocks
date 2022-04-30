from flask import Flask
import requests

app = Flask(__name__)

#GET DATA STOCK
stock = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=DQJ092TSFPDF9EKZ")
try:
    stock_parsed = stock.json()
except:
    pass

@app.route('/')
def index():
    return "en cours de dev"


@app.route('/data')
def index():
    if stock_parsed:
        return stock_parsed["Weekly Time Series"]
    else:
        return 'jean et adam'




app.run(host='0.0.0.0', port=3000)