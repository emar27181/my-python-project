from estimate_used_color_scheme import estimate_used_color_scheme, rgb_to_hex
from config.constants_dev import LOAD_DIRECTORY_PATH
import json
import numpy as np
import os


# 読込んだイラストの使用配色をjson形式で保存する関数
def generate_json_used_color_scheme(image_path):
    used_color_schemes = estimate_used_color_scheme(image_path)
    # print(f"used_color_schemes = { used_color_schemes}")

    # JSON用のリストを作成
    json_data = []
    for color_scheme in used_color_schemes:
        hex = rgb_to_hex(color_scheme[0].tolist())
        color_dict = {
            "color": hex,  # NumPy配列をリストに変換
            "rate": round(10 * color_scheme[1]) / 1000,
            "amount": -1
        }
        json_data.append(color_dict)

    first_element = {
        "illustName": image_path,
        "color": json_data[0]["color"],
        "rate": json_data[0]["rate"],
        "amount": -1
    }

    json_data = [first_element] + json_data[1:]

    json_string = json.dumps(json_data, indent=4)  # JSON文字列に変換
    # print(json_string)  # 結果のJSON文字列を表示
    # print(json_data)  # 結果のJSON文字列を表示
    return json_data


def save_json_used_color_scheme():
    json_data = []

    # directory_path = 'tmp/estimate_used_color_scheme/data/input/gaako/'
    # jpg_files = [file for file in os.listdir(directory_path) if file.endswith('.jpg')]  # .jpgファイルの名前をすべて配列に保存
    image_files = [file for file in os.listdir(LOAD_DIRECTORY_PATH) if file.endswith('.jpg')]  # .jpgファイルの名前をすべて配列に保存
    image_files = [file for file in os.listdir(LOAD_DIRECTORY_PATH) if file.endswith('.png')]  # .pngファイルの名前をすべて配列に保存

    print(image_files)

    for file_name in image_files:
        add_json_data = generate_json_used_color_scheme(f"{LOAD_DIRECTORY_PATH}{file_name}")
        json_data.append(add_json_data)

    # print(json_data)

    file_path = 'tmp/estimate_used_color_scheme/data/output/log_used_color_scheme.json'
    with open(file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"JSONデータが '{file_path}' に保存されました。")
    return json_data


def main():
    save_json_used_color_scheme()

    """
    generate_json_used_color_scheme('tmp/estimate_used_color_scheme/data/input/NCG297-2-1920x1920.jpg')
    generate_json_used_color_scheme('tmp/estimate_used_color_scheme/data/input/NCG260-2000x1200.jpg')
    generate_json_used_color_scheme('tmp/estimate_used_color_scheme/data/input/NCG290-1920x1200.jpg')
    """


if __name__ == "__main__":
    main()
