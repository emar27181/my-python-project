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
redValue = 0
greenValue = 0
blueValue = 0
count = 0

for key, value in data.items():
    if value != 0:
        count = count + 1

# joy(yellow): (255, 255, 0)
redValue += (data["joy"] / 10) * 255
greenValue += (data["joy"] / 10) * 255
blueValue += (data["joy"] / 10) * 0

# trust(yellow green): (173, 255, 47)
redValue += (data["trust"] / 10) * 173
greenValue += (data["trust"] / 10) * 255
blueValue += (data["trust"] / 10) * 47

# fear(green): (0, 255, 0)
redValue += (data["fear"] / 10) * 0
greenValue += (data["fear"] / 10) * 255
blueValue += (data["fear"] / 10) * 0

# surprise(light blue): (173, 216, 230)
redValue += (data["surprise"] / 10) * 173
greenValue += (data["surprise"] / 10) * 216
blueValue += (data["surprise"] / 10) * 230

# sadness(blue): (0, 0, 255)
redValue += (data["sadness"] / 10) * 0
greenValue += (data["sadness"] / 10) * 0
blueValue += (data["sadness"] / 10) * 255

# disgust(purple): (128, 0, 128)
redValue += (data["disgust"] / 10) * 128
greenValue += (data["disgust"] / 10) * 0
blueValue += (data["disgust"] / 10) * 128

# anger(red): (255, 0, 0)
redValue += (data["anger"] / 10) * 255
greenValue += (data["anger"] / 10) * 0
blueValue += (data["anger"] / 10) * 0

# anticipation(orange) : (255, 165, 0)
redValue += (data["anticipation"] / 10) * 255
greenValue += (data["anticipation"] / 10) * 165
blueValue += (data["anticipation"] / 10) * 0

redValue = round(redValue / count)
greenValue = round(greenValue / count)
blueValue = round(blueValue / count)

print("(", redValue, ", ", greenValue, ", ", blueValue, "), count: ", count)
