from flask import Flask, jsonify, redirect, url_for, request
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.debug("This is a debug test message(logging)")
    print("This is a debug test message(print)")
    return redirect('/api/data')


@app.route('/api/receive-data', methods=['GET', 'POST'])
def receive_data():  # データの受信
    print("receive_data() is called(受信)")
    inputData = request.json.get('data')  # フロントエンドからデータを受信
    print("inputData: ", inputData)
    with open('data/input/InputData.txt', 'a') as file:
        file.write(inputData + '\n')

    return jsonify({"message": "Data sent successfully!(inputData: "+inputData+")"})


@app.route('/api/send-data', methods=['GET', 'POST'])
def send_data():  # データの送信
    print("send_data() is called(送信)")

    with open('data/input/InputData.txt', 'r') as file:
        outputData = file.read()
        print("outputData: ", outputData)
    data = {'message': outputData}
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
