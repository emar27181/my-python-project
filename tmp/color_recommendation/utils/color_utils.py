import numpy as np
# from calculate_color_difference import color_difference_delta_e


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

# 角度の差(0°~180°)を計算する関数


def calc_angle_diff(angle1, angle2):
    diff = abs(angle1 - angle2)
    return diff if diff <= 180 else 360 - diff
