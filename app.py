from flask import Flask, jsonify, send_from_directory
from backend.services.pipeline import run_pipeline
from backend.services.binance_api import get_price

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

if __name__ == '__main__':
    app.run(debug=True)
