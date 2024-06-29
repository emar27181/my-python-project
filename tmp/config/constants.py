# 固定値の宣言
EVALUATED_ILLUST_COUNT = 10  # 次の色が含まれているかどうか比較されたイラストの枚数
IS_EVALUATED_TIMING_DRAW_COLOR = [0, 1]  # どのタイミングに塗られた色を評価するか保存する配列

# 現在使用している固定値は以下
LIGHTNESS_LIST = [[], [-10, 10], [-20, 20]]  # どの明度の差によってバリエーションが追加されたかを保存する配列
TIME_LIST = [[1]]
SIM_MIN = 10
SIM_MAX = 10

EVALUATED_PARAMETER = "LIGHT"  # "SAME", "TIME", "LIGHT"
