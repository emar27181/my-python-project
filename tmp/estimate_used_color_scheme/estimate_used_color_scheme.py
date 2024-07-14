# 使用された色を推定するプログラム

from PIL import Image
from collections import Counter
from calculate_color_difference import color_difference_delta_e


# 画像を読み込む
def estimate_used_color_scheme():
    image_path = 'tmp/estimate_used_color_scheme/data/input/NCG290-1920x1200.jpg'  # 画像のパスを指定
    image = Image.open(image_path)

    # 画像をRGBに変換
    image = image.convert('RGB')

    # 画像のピクセルデータを取得
    pixels = list(image.getdata())

    # カラーコードとその出現回数をカウント
    color_counter = Counter(pixels)

    used_color_schemes = []  # 使用した配色を保存する変数の初期化

    # カラーコードと出現回数を表示
    for color, count in color_counter.most_common():
        hsl = rgb_to_hsl(color)
        saturation = hsl[1]

        if (count >= 10000):
            # if ((count >= 10000) & (saturation >= 30)):
            used_color_schemes.append([color, count])
            print_colored_text("■■■■■■■■■■■■", color)
            print(f'Count: {count}, ColorCode: {rgb_to_hex(color)}, RGB: {color}, HSL: {rgb_to_hsl(color)}')
            print("")

    print(f'used_color_scheme: {used_color_schemes}')


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
    print(f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text}\033[0m")


def main():
    estimate_used_color_scheme()
    print(f'ΔEの色差: {color_difference_delta_e((243, 243, 243), (255, 255, 255))}')
    print(f'ΔEの色差: {color_difference_delta_e((157, 190, 209), (144, 181, 200))}')


if __name__ == "__main__":
    main()
