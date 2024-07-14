# 使用された色を推定するプログラム

from PIL import Image
from collections import Counter


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

    # カラーコードと出現回数を表示
    for color, count in color_counter.most_common():
        if (count >= 10000):
            print(f'Color:  {color}, Count: {count}')


def main():
    estimate_used_color_scheme()


if __name__ == "__main__":
    main()
