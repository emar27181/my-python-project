data = {}

# データの読み込み
with open('data/output/OutputData.txt', 'r') as file:
    for line in file:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = int(value.strip())
            data[key] = value
            # print(f"{key}: {value}")

print("data:", data)

# RGBの計算
hueArray = []
saturationArray = []
lightnessArray = []
count = 0

for key, value in data.items():
    if value != 0:
        count = count + 1

# ※以下PCCS色相環参照
# https://www.i-ryo.com/entry/2019/02/24/211711

# joy(yellow)
if data["joy"] != 0:
    hueArray.append(53)
    saturationArray.append(data["joy"] * 10)
    lightnessArray.append(data["joy"] * 10)

# trust(yellow green)
if data["trust"] != 0:
    hueArray.append(66)
    saturationArray.append(data["trust"] * 10)
    lightnessArray.append(data["trust"] * 10)

# fear(green)
if data["fear"] != 0:
    hueArray.append(153)
    saturationArray.append(data["fear"] * 10)
    lightnessArray.append(data["fear"] * 10)

# surprise(light blue)
if data["joy"] != 0:
    hueArray.append(201)
    saturationArray.append(data["surprise"] * 10)
    lightnessArray.append(data["surprise"] * 10)

# sadness(blue)
if data["sadness"] != 0:
    hueArray.append(209)
    saturationArray.append(data["sadness"] * 10)
    lightnessArray.append(data["sadness"] * 10)

# disgust(purple)
if data["disgust"] != 0:
    hueArray.append(300)
    saturationArray.append(data["disgust"] * 10)
    lightnessArray.append(data["disgust"] * 10)

# anger(red)
if data["anger"] != 0:
    hueArray.append(344)
    saturationArray.append(data["anger"] * 10)
    lightnessArray.append(data["anger"] * 10)

# anticipation(orange) : (255, 165, 0)
if data["anticipation"] != 0:
    hueArray.append(19)
    saturationArray.append(data["anticipation"]*10)
    lightnessArray.append(data["anticipation"] * 10)

for hueValue, saturationValue, lightnessValue in zip(hueArray, saturationArray, lightnessArray):
    hueValue = round(hueValue)
    saturationValue = round(saturationValue)
    lightnessValue = round(lightnessValue)
    print("(", hueValue, saturationValue, lightnessValue, ")")
