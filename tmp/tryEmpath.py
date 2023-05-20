import time
import requests

url = 'https://api.webempath.net/v2/analyzeWav'

#ここはご自分のKeyを入力ください
apikey = 'o3xOeGanuGaegs0sfWNCz43mjSpChd5qdv-3OJXv0BE'
payload = {'apikey': apikey}

wav = 'src/assets/new_sayonara_01.wav' # 「明るく」
data = open(wav, 'rb')
file = {'wav': data}

res = requests.post(url, params=payload, files=file)
print(res.json())

time.sleep(1)

wav = 'src/assets/new_sayonara_02.wav' # 「涙をこらえて」
data = open(wav, 'rb')
file = {'wav': data}

res = requests.post(url, params=payload, files=file)
print(res.json())