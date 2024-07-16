import json
from PIL import Image
from estimate_used_color_scheme import rgb_to_hsl
from utils.color_utils import hex_to_rgb, print_colored_text, hsl_to_rgb, rgb_to_hex, merge_similar_color

IS_PRINT_HUE_DATA = False  # 抽出した色相の情報を表示させるかどうかを保存する固定値


# ある配色で使われた配色技法を推定する関数
def estimate_used_color_scheme_method(json_color_scheme):
    estimate_used_hue(json_color_scheme)


# ある配色で使われた色相を推定する関数
def estimate_used_hue(json_color_scheme):
    # print(color_scheme)
    hue_array = []
    used_color_schemes_method = []

    for json_color in json_color_scheme:
        # print(json_color)
        color_info = json_color['color']
        rate = json_color['rate']
        color_rgb = hex_to_rgb(color_info)
        color_hsl = rgb_to_hsl(color_rgb)
        hue = color_hsl[0]
        saturation = color_hsl[1]
        lightness = color_hsl[2]

        # 彩度が10(暫定値)以上の場合，有彩色としてスロットに追加
        if ((saturation > 10) & (lightness < 95)):
            hue_array.append(hue)
            used_color_schemes_method.append([hsl_to_rgb(hue, 50, 50), rate])

    if (IS_PRINT_HUE_DATA):
        # 読込んだ画像の情報の出力
        file_path = json_color_scheme[0]['illustName']
        # img = Image.open(file_path)
        # img.show()
        print(file_path)

    if (False):
        for color_info in used_color_schemes_method:
            print_colored_text("■■■■■■", color_info[0])
            print(f"hsl: {rgb_to_hsl(color_info[0])}, rate: {color_info[1]}")

        print("---- ↓ -----")

    merged_used_color_schemes_method = merge_similar_color(used_color_schemes_method, 5)

    if (IS_PRINT_HUE_DATA):
        for color_info in merged_used_color_schemes_method:
            print_colored_text("■■■■■■", color_info[0])
            print(f"hsl: {rgb_to_hsl(color_info[0])}, rate: {color_info[1]}")

    if (IS_PRINT_HUE_DATA):
        print("\n")


def main():

    with open("tmp/estimate_used_color_scheme/data/output/log_used_color_scheme.json", "r") as file:
        json_data = json.load(file)

    for color_scheme in json_data:
        # estimate_used_hue(color_scheme)
        estimate_used_color_scheme_method(color_scheme)

    # print(json_data)


if __name__ == "__main__":
    main()
