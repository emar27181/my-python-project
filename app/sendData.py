from flask import Flask, jsonify, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for("get_data"))

@app.route('/api/data', methods=['GET'])
def get_data():
    data = [
        {"id": 1, "name": "データ1"},
        {"id": 2, "name": "データ2"},
        {"id": 3, "name": "データ3"},
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
