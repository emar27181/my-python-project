# 使用された色を推定するプログラム

from PIL import Image
from collections import Counter
from calculate_color_difference import color_difference_delta_e
import numpy as np
import config.constants


# 読み込まれた画像の使用配色を推定する関数
def estimate_used_color_scheme(image_path):
    # image_path = 'tmp/estimate_used_color_scheme/data/input/NCG290-1920x1200.jpg'  # 画像のパスを指定
    # image_path = 'tmp/estimate_used_color_scheme/data/input/NCG260-2000x1200.jpg'  # 画像のパスを指定
    # image_path = 'tmp/estimate_used_color_scheme/data/input/NCG297-2-1920x1920.jpg'  # 画像のパスを指定
    image = Image.open(image_path)

    print("\n")
    print(f"loading {image_path}")

    image = image.convert('RGB')  # 画像をRGBに変換
    pixels = list(image.getdata())  # 画像のピクセルデータを取得
    color_counter = Counter(pixels)  # カラーコードとその出現回数をカウント

    used_color_schemes = []  # 使用した配色を保存する変数の初期化

    # 配色(カラーコードと出現回数)を計測
    for color, count in color_counter.most_common():
        hsl = rgb_to_hsl(color)
        saturation = hsl[1]

        if (count >= 10000):
            # if ((count >= 10000) & (saturation >= 30)):
            used_color_schemes.append([color, count])

            if (config.constants.IS_PRINT_COLOR_SCHEME_BEFORE_MEREGED):
                print_colored_text("■■■■■■■■■■■■", color)
                print(f'Count: {count}, ColorCode: {rgb_to_hex(color)}, RGB: {color}, HSL: {rgb_to_hsl(color)}')

    # print(f'used_color_scheme: {used_color_schemes}') # 確認用出力

    # 配色の中で同じ色を結合して保存
    merged_used_color_schemes = merge_similar_color(used_color_schemes, 5)

    # print(f"merged_used_color_schemes = {merged_used_color_schemes}") # 確認用出力

    if (config.constants.IS_PRINT_COLOR_SCHEME_BEFORE_MEREGED):
        print("------ ↓ ------")
    for color, count in merged_used_color_schemes:
        print_colored_text("■■■■■■■■■■■■", color)
        print(f'Count: {count}, ColorCode: {rgb_to_hex(color)}, RGB: {color}, HSL: {rgb_to_hsl(color)}')

    return merged_used_color_schemes


# 使用配色のうちΔE値が5以下の色を結合する関数
def merge_similar_color(color_scheme, threshold):
    merged_colors = []  # 結合する色を保存する配列を初期化

    # 配色がある限り色を結合
    while len(color_scheme) > 0:
        base_color = color_scheme[0]  # 先頭の色をベースカラーに代入
        to_merge = [base_color]
        color_scheme = color_scheme[1:]

        # 先頭の色と先頭以外の色でΔEが閾値以下の場合があるかどうかの探索
        for i in range(len(color_scheme) - 1, -1, -1):  # 最後尾([len(~)-1])からから先頭([-1])まで検索

            # 先頭の色とi番目の色が同じ色だった場合
            if color_difference_delta_e(base_color[0], color_scheme[i][0]) <= threshold:
                to_merge.append(color_scheme[i])  # 結合する色を保存するスロットにi番目の色を追加
                color_scheme.pop(i)  # 結合されるi番目の色を削除

        # 色の加重平均と合算された出現回数を色を結合する配列に追加
        merge_color_total_count = sum([color[1] for color in to_merge])  # 出現回数の合算
        merge_color_rgb = np.average([color[0] for color in to_merge], axis=0, weights=[color[1] for color in to_merge])
        merge_color_rgb = np.round(merge_color_rgb).astype(int)
        merged_colors.append([merge_color_rgb, merge_color_total_count])
    return merged_colors


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])


def rgb_to_hsl(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    r /= 255.0
    g /= 255.0
    b /= 255.0

    max_val = max(r, g, b)
    min_val = min(r, g, b)
    delta = max_val - min_val

    # 輝度の計算
    l = (max_val + min_val) / 2.0

    # 彩度の計算
    if delta == 0:
        s = 0.0
    else:
        s = delta / (1 - abs(2 * l - 1))

    # 色相の計算
    if delta == 0:
        h = 0.0
    elif max_val == r:
        h = 60 * (((g - b) / delta) % 6)
    elif max_val == g:
        h = 60 * (((b - r) / delta) + 2)
    elif max_val == b:
        h = 60 * (((r - g) / delta) + 4)

    return (round(h), round(100 * s), round(100 * l))


def print_colored_text(text, rgb):
    # RGBから16進数カラーコードに変換
    hex_color = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

    # ANSIエスケープシーケンスを使って色を設定
    print(f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text}\033[0m", end="  ")


def main():
    estimate_used_color_scheme('tmp/estimate_used_color_scheme/data/input/NCG297-2-1920x1920.jpg')

    """
    print(f'ΔEの色差: {color_difference_delta_e((243, 243, 243), (255, 255, 255))}')
    print(f'ΔEの色差: {color_difference_delta_e((157, 190, 209), (144, 181, 200))}')
    print(f'ΔEの色差: {color_difference_delta_e((76, 76, 76), (128, 128, 128))}')
    """


if __name__ == "__main__":
    main()
