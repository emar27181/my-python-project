
# from tmp import tryEmotionAnalyzeWithGPT
import EmotionAnalyzeWithGPT
from EmotionAnalyzeWithGPT import analyze_emotion #新たに宣言した関数をいずれ読み込む(2023/09/24)
import logging
from flask_cors import CORS
from flask import Flask, jsonify, redirect, url_for, request
import os

# カレントディレクトリを app ディレクトリに設定
# current_dir = os.path.dirname(os.path.abspath(__file__))
# os.chdir(current_dir)


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.debug("This is a debug test message(logging)")
    print("This is a debug test message(print)")
    return redirect('/api/send-data')


@app.route('/api/receive-data', methods=['GET', 'POST'])
def receive_data():  # データの受信
    print("receive_data() is called(受信)")
    inputData = request.json.get('data')  # フロントエンドからデータを受信
    print("inputData: ", inputData)
    with open('data/input/InputData.txt', 'w') as file:
        file.write(inputData + '\n')  # 入力ファイルの更新
    # EmotionAnalyzeWithGPT()  # 実行しようと思うとバグが発生(2023/09/24)

    return jsonify({"message": "Data sent successfully!(inputData: "+inputData+")"})



@app.route('/api/analyze-emotion', methods=['GET', 'POST'])
def call_analyze_emotion():
    analyze_emotion()
    with open('data/input/InputData.txt', 'r') as input_file:
        input_data = input_file.read()
    return jsonify({"message": "analeyze_emotion() was called (input: "+input_data+" )"})



@app.route('/api/input-sentence-now', methods=['GET', 'POST'])
def send_input_sentence():
    with open('data/input/InputData.txt', 'r') as file:
        input_sentence = file.read()
    return input_sentence


@app.route('/api/send-data', methods=['GET', 'POST'])
def send_data():  # データの送信
    print("send_data() is called(送信)")

    with open('data/output/OutputData.json', 'r') as file:
        outputData = file.read()
        print("outputData: ", outputData)
    data = {'message': outputData}
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
