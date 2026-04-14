from flask import Flask, jsonify, send_from_directory
from backend.services.pipeline import run_pipeline
from backend.services.binance_api import get_price
import json

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('.', path)

@app.route('/api/data')
def get_data():
    results = run_pipeline()
    for r in results:
        if r["ticker"] in ["BTC", "ETH"]:
            symbol = r["ticker"] + "USDT"
            r["price"] = get_price(symbol)
    return jsonify(results)

@app.route('/api/korean_stocks')
def get_korean_stocks():
    with open('korean_stock_portfolio.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
