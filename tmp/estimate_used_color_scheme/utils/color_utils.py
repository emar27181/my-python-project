import numpy as np
from calculate_color_difference import color_difference_delta_e


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


# 引数で受け取ったRGB値の文字を表示させる関数
def print_colored_text(text, rgb):
    # RGBから16進数カラーコードに変換
    hex_color = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

    # ANSIエスケープシーケンスを使って色を設定
    print(f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text}\033[0m", end="  ")


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])


def hsl_to_rgb(h, s, l):
    s /= 100
    l /= 100

    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    elif 300 <= h < 360:
        r, g, b = c, 0, x
    else:
        r, g, b = 0, 0, 0

    r = (r + m) * 255
    g = (g + m) * 255
    b = (b + m) * 255

    return [int(r), int(g), int(b)]


"""
print(hsl_to_rgb(0, 100, 50))
print(hsl_to_rgb(180, 50, 50))
"""

"""
print(hex_to_rgb("#000000"))
print(hex_to_rgb("#FFFFFF"))
print(hex_to_rgb("#FF0000"))
print(hex_to_rgb("#FF5500"))
"""


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
