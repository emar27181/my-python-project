from flask import Flask, jsonify, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.json.get('data')  # 2 フロントエンドから受信したデータ
    {"greeting": "Hello! {}".format(data)}


@app.route('/api/data', methods=['GET', 'POST'])
def post_data():
    data = {'message': 'This is the data from Flask!'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
