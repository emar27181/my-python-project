import json
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from estimate_used_color_scheme import rgb_to_hsl
from calculate_color_difference import color_difference_delta_e
from utils.color_utils import hex_to_rgb, print_colored_text, hsl_to_rgb, rgb_to_hex, merge_similar_color, calc_angle_diff
from utils.color_class import ColorScheme
import math

IS_PRINT_HUE_DATA = False  # 抽出した色相の情報を表示させるかどうかを保存する固定値


# ある配色で使われた配色技法を推定する関数
def estimate_used_color_scheme_method(json_color_scheme):

    if (len(json_color_scheme) == 0):
        return None

    used_color_scheme_method = ColorScheme.INIT
    used_colors = estimate_used_hue(json_color_scheme)
    used_hues = []
    hue_diffs = []

    # 確認用出力
    file_path = json_color_scheme[0]['illustName']
    print("============================================")
    print(f"file_path: {file_path}")
    print(f"使われた色の数は {len(used_colors)} 色です．")
    for color_info in used_colors:
        # print(f"hue_info: {hue_info}")
        color_rgb = color_info[0]
        color_hsl = rgb_to_hsl(color_rgb)
        used_hues.append(color_hsl[0])

        print_colored_text("■■■■■■", color_rgb)
        print(f"hue: {color_hsl[0]}, hsl: {color_hsl}")

    # 色相差の計算
    # print(f"used_hues: {used_hues}")
    for i in range(0, len(used_hues)):
        hue_diff = calc_angle_diff(used_hues[0], used_hues[i])
        hue_diffs.append(hue_diff)
        # print(f"[0] : [{i}] = {hue_diff}")

    hue_diffs.sort()
    print(f"hue_diffs: {hue_diffs}")

    print("")

    # 使用した配色技法の推定
    # 色の数が1色だった場合
    if (len(used_colors) == 1):
        used_color_scheme_method = ColorScheme.IDENTITY_COLOR

    # 色の数が2色だった場合
    elif (len(used_colors) == 2):
        if (hue_diffs[1] >= 165):
            used_color_scheme_method = ColorScheme.DYAD_COLOR
        elif (is_angle_between_angles(hue_diffs[1], 75, 105)):
            # elif ((75 <= hue_diffs[1]) & (hue_diffs[1] <= 105)):
            used_color_scheme_method = ColorScheme.INTERMEDIATE_COLOR
        elif (is_angle_between_angles(hue_diffs[1], 105, 165)):
            used_color_scheme_method = ColorScheme.OPONENT_COLOR
        elif (is_angle_between_angles(hue_diffs[1], 15, 45)):
            used_color_scheme_method = ColorScheme.ANALOGY_COLOR

    # 色の数が3色だった場合
    elif (len(used_colors) == 3):
        if ((hue_diffs[1] <= 30) & (hue_diffs[2] <= 60)):
            used_color_scheme_method = ColorScheme.DOMINANT_COLOR
        elif (((120 <= hue_diffs[1]) & (hue_diffs[1] <= 150)) & ((120 <= hue_diffs[2]) & (hue_diffs[2] <= 150))):
            used_color_scheme_method = ColorScheme.TRIAD_COLOR_SCHEME
        elif ((hue_diffs[1] >= 150) & (hue_diffs[2] >= 150)):
            used_color_scheme_method = ColorScheme.SPLIT_COMPLEMENTARY_COLOR
        elif (is_angle_between_angles(hue_diffs[1], 15, 60) & is_angle_between_angles(hue_diffs[2], 135, 165)):
            # elif ((hue_diffs[1] <= 45) & (hue_diffs[2] >= 150)):
            used_color_scheme_method = ColorScheme.SPLIT_COMPLEMENTARY_COLOR
        elif (is_angle_between_angles(hue_diffs[2], 15, 60) & is_angle_between_angles(hue_diffs[1], 135, 165)):
            # elif ((hue_diffs[1] >= 150) & (hue_diffs[2] <= 45)):
            used_color_scheme_method = ColorScheme.SPLIT_COMPLEMENTARY_COLOR

    # 色の数が3色だった場合
    elif (len(used_colors) == 4):
        if (is_angle_between_angles(hue_diffs[1], 75, 105) & is_angle_between_angles(hue_diffs[2], 75, 105) & (hue_diffs[3] >= 165)):
            used_color_scheme_method = ColorScheme.TETRADE_COLOR
    elif (len(used_colors) == 5):
        used_color_scheme_method = ColorScheme.PENTAD_COLOR
    elif (len(used_colors) == 6):
        used_color_scheme_method = ColorScheme.HEXAD_COLOR
    else:
        used_color_scheme_method = ColorScheme.ERROR

    print(f"推定された配色技法は {used_color_scheme_method} です．")

    print("============================================\n")


def is_angle_between_angles(angle, angle_start, angle_end):
    return ((angle_start <= angle) & (angle <= angle_end))

# ある配色で使われた色相を推定する関数


def estimate_used_hue(json_color_scheme):
    # print(color_scheme)
    hue_array = []
    used_hues = []

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
            used_hues.append([hsl_to_rgb(hue, 50, 50), rate])
        """
        else:
            if (lightness > 50):
                used_hues.append([(255, 255, 255), rate])
            else:
                used_hues.append([(0, 0, 0), rate])
        """

    if (IS_PRINT_HUE_DATA):
        # 読込んだ画像の情報の出力
        file_path = json_color_scheme[0]['illustName']
        # img = Image.open(file_path)
        # img.show()
        print(file_path)

    if (False):
        for color_info in used_hues:
            print_colored_text("■■■■■■", color_info[0])
            print(f"hsl: {rgb_to_hsl(color_info[0])}, rate: {color_info[1]}")

        print("---- ↓ -----")

    # 使用した色相らをΔE値15以下のもので結合
    # 使用色の抽出(ΔE=5)と違い使用配色の抽出はΔE=15が良さそう？
    merged_used_hues = merge_similar_color(used_hues, 15)

    if (IS_PRINT_HUE_DATA):
        for color_info in merged_used_hues:
            print_colored_text("■■■■■■", color_info[0])
            print(f"hsl: {rgb_to_hsl(color_info[0])}, rate: {color_info[1]}")

    if (IS_PRINT_HUE_DATA):
        print("\n")

    return merged_used_hues


def main():

    with open("tmp/estimate_used_color_scheme/data/output/log_used_color_scheme.json", "r") as file:
        json_data = json.load(file)

    for color_scheme in json_data:
        # estimate_used_hue(color_scheme)
        estimate_used_color_scheme_method(color_scheme)

    # print(json_data)

    if (False):
        # テスト
        # 色相差とΔE値はどれぐらい近い？(ex: 色相が5度離れたらΔEも5になる？)
        print(hsl_to_rgb(0, 100, 50))

        print(color_difference_delta_e(hsl_to_rgb(0, 50, 50), hsl_to_rgb(5, 50, 50)))  # ΔE = 3.2
        print(color_difference_delta_e(hsl_to_rgb(0, 50, 50), hsl_to_rgb(10, 50, 50)))  # ΔE = 7.1
        print(color_difference_delta_e(hsl_to_rgb(0, 50, 50), hsl_to_rgb(15, 50, 50)))  # ΔE = 11.0

        print(color_difference_delta_e(hsl_to_rgb(180, 50, 50), hsl_to_rgb(185, 50, 50)))  # ΔE = 5.1
        print(color_difference_delta_e(hsl_to_rgb(180, 50, 50), hsl_to_rgb(190, 50, 50)))  # ΔE = 10.0
        print(color_difference_delta_e(hsl_to_rgb(160, 50, 50), hsl_to_rgb(195, 50, 50)))  # ΔE = 28.2

        # 色相によって差が異なるっぽい？？当然だけどLAB色空間の比較だからHSL色空間の数字が参考になるわけじゃないっぽい


if __name__ == "__main__":
    main()
