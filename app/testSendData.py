from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/api/data')

@app.route('/api/data', methods=['POST', 'GET'])
def send_data():
    data = {'message': 'This is the data from Flask!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
