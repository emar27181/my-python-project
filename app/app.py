from flask import Flask, jsonify, redirect, url_for, request
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

inputData = "initial Text"
outputData = "initial Text"


@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.debug("This is a debug test message(logging)")
    print("This is a debug test message(print)")
    return redirect('/api/data')


@app.route('/api/send-data', methods=['GET', 'POST'])
def send_data():  # データの送信
    print("send_data() is called(送信)")
    outputData = inputData +  " + test add text"
    data = {'message': outputData}
    return jsonify(data)


@app.route('/api/receive-data', methods=['GET', 'POST'])
def receive_data():  # データの受信
    # 2023/05/23時点では一つの入力データの保存しか保存できない
    print("receive_data() is called(受信)")
    inputData = request.json.get('data')  # フロントエンドからデータを受信
    print("inputData: ", inputData)
    return jsonify({"message": "Data sent successfully!(inputData: "+inputData+")"})


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
