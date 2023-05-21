import requests

#APIキーを取得するにはプリペイドカード(バンドルカード)は使えないっぽい
#Paypalならいける？？
API_KEY = "あなたのAPIキーをここに入力してください。"
END_POINT = "https://language.googleapis.com"
URL = f"https://language.googleapis.com/v1/documents:analyzeSentiment?key={API_KEY}"

analyzeText = "メロスは激怒した"

headers = {'Content-Type': 'application/json'}
body = {
    'document': {
        'type': 'PLAIN_TEXT',
        'language': 'JA',
        'content': analyzeText
    }
}

res = requests.post(URL, headers=headers, json=body)

res.json()
print(res.json())
