from estimate_used_color_scheme import estimate_used_color_scheme
import json
import numpy as np


# 読込んだイラストの使用配色をjson形式で保存する関数
def generate_json_used_color_scheme(image_path):
    used_color_schemes = estimate_used_color_scheme(image_path)
    print(f"used_color_schemes = { used_color_schemes}")

    # JSON用のリストを作成
    json_data = []
    for color_scheme in used_color_schemes:
        color_dict = {
            "color": color_scheme[0].tolist(),  # NumPy配列をリストに変換
            "amount": color_scheme[1]
        }
        json_data.append(color_dict)

    json_string = json.dumps(json_data, indent=4)  # JSON文字列に変換
    print(json_string)  # 結果のJSON文字列を表示


def main():
    generate_json_used_color_scheme('tmp/estimate_used_color_scheme/data/input/NCG297-2-1920x1920.jpg')
    generate_json_used_color_scheme('tmp/estimate_used_color_scheme/data/input/NCG260-2000x1200.jpg')
    generate_json_used_color_scheme('tmp/estimate_used_color_scheme/data/input/NCG290-1920x1200.jpg')


if __name__ == "__main__":
    main()
