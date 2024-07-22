from utils.color_utils import hex_to_rgb, print_colored_text
import json

# JSONファイルのパスを指定
file_path = 'tmp/estimate_used_color_scheme/data/output/log_used_color_scheme_NCG.json'
# file_path = 'tmp/estimate_used_color_scheme/data/output/log_used_color_scheme_gaako_instagram.json'

# JSONファイルを開く
with open(file_path, 'r') as file:
    # JSONファイルの内容を読み込む
    data = json.load(file)

data = [entry for entry in data if entry]

# データを表示
for color_info in data:

    # if (len(color_info) <= 3):
    #    continue
    for color in color_info:
        color_hex = color["color"]
        color_rgb = hex_to_rgb(color_hex)

        print_colored_text("■", color_rgb)

    print("\n")
