from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000


# 色の差をΔEを用いて計算する関数
def color_difference_delta_e(color1, color2):
    # RGBからLab色空間に変換
    color1_rgb = sRGBColor(*color1, is_upscaled=True)
    color2_rgb = sRGBColor(*color2, is_upscaled=True)

    color1_lab = convert_color(color1_rgb, LabColor)
    color2_lab = convert_color(color2_rgb, LabColor)

    # ΔE（CIE 2000）を計算
    delta_e = delta_e_cie2000(color1_lab, color2_lab)
    return float(delta_e)


# テスト実行
'''
print(f'ΔEの色差: {color_difference_delta_e((255, 0, 0), (255, 0, 0))}')
print(f'ΔEの色差: {color_difference_delta_e((255, 128, 0), (255, 0, 0))}')
print(f'ΔEの色差: {color_difference_delta_e((255, 0, 0), (255, 255, 0))}')
print(f'ΔEの色差: {color_difference_delta_e((0, 0, 0), (255, 255, 255))}')
'''
