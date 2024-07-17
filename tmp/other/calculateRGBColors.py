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
redArray = []
greenArray = []
blueArray = []
count = 0

for key, value in data.items():
    if value != 0:
        count = count + 1

# joy(yellow): (255, 255, 0)
if data["joy"] != 0:
    redArray.append((data["joy"] / 10) * 255)
    greenArray.append((data["joy"] / 10) * 255)
    blueArray.append((data["joy"] / 10) * 0)

# trust(yellow green): (173, 255, 47)
if data["trust"] != 0:
    redArray.append((data["trust"] / 10) * 173)
    greenArray.append((data["trust"] / 10) * 255)
    blueArray.append((data["trust"] / 10) * 47)

# fear(green): (0, 255, 0)
if data["fear"] != 0:
    redArray.append((data["fear"] / 10) * 0)
    greenArray.append((data["fear"] / 10) * 255)
    blueArray.append((data["fear"] / 10) * 0)

# surprise(light blue): (173, 216, 230)
if data["joy"] != 0:
    redArray.append((data["surprise"] / 10) * 173)
    greenArray.append((data["surprise"] / 10) * 216)
    blueArray.append((data["surprise"] / 10) * 230)

# sadness(blue): (0, 0, 255)
if data["sadness"] != 0:
    redArray.append((data["sadness"] / 10) * 0)
    greenArray.append((data["sadness"] / 10) * 0)
    blueArray.append((data["sadness"] / 10) * 255)

# disgust(purple): (128, 0, 128)
if data["disgust"] != 0:
    redArray.append((data["disgust"] / 10) * 128)
    greenArray.append((data["disgust"] / 10) * 0)
    blueArray.append((data["disgust"] / 10) * 128)

# anger(red): (255, 0, 0)
if data["anger"] != 0:
    redArray.append((data["anger"] / 10) * 255)
    greenArray.append((data["anger"] / 10) * 0)
    blueArray.append((data["anger"] / 10) * 0)

# anticipation(orange) : (255, 165, 0)
if data["anticipation"] != 0:
    redArray.append((data["anticipation"] / 10) * 255)
    greenArray.append((data["anticipation"] / 10) * 165)
    blueArray.append((data["anticipation"] / 10) * 0)

for redValue, greenValue, blueValue in zip(redArray, greenArray, blueArray):
    redValue = round(redValue )
    greenValue = round(greenValue)
    blueValue = round(blueValue)
    print("(", redValue, greenValue, blueValue, ")")