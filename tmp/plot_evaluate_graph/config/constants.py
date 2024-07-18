# 固定値の宣言
EVALUATED_ILLUST_COUNT = 10  # 次の色が含まれているかどうか比較されたイラストの枚数
IS_EVALUATED_TIMING_DRAW_COLOR = [0, 1]  # どのタイミングに塗られた色を評価するか保存する配列

# 現在使用している固定値は以下
LIGHTNESS_LIST = []  # どの明度の差によってバリエーションが追加されたかを保存する配列
TIME_LIST = []
SIM_MIN = 0
SIM_MAX = 0

# 読込むイラストレーターのディレクトリ名
LOAD_ILLUST_DIR_NAME = "NCG"

EVALUATED_PARAMETER = "SAME"  # "CUSTOM", "SAME", "TIME", "LIGHT"

# 同一色判定の閾値の差が異なる固定値の設定
if (EVALUATED_PARAMETER == "CUSTOM"):
    LIGHTNESS_LIST = [[-20, 20]]
    TIME_LIST = [[1]]
    SIM_MIN = 10
    SIM_MAX = 10


# 同一色判定の閾値の差が異なる固定値の設定
if (EVALUATED_PARAMETER == "SAME"):
    LIGHTNESS_LIST = [[-20, 20]]
    TIME_LIST = [[0, 1, 2]]
    SIM_MIN = 5
    SIM_MAX = 15

# 明度のバリエーションが異なる固定値の設定
elif (EVALUATED_PARAMETER == "LIGHT"):
    LIGHTNESS_LIST = [[], [-10, 10], [-20, 20]]
    TIME_LIST = [[1]]
    SIM_MIN = 10
    SIM_MAX = 10

# 描画するタイミングが異なる固定値の設定
elif (EVALUATED_PARAMETER == "TIME"):
    LIGHTNESS_LIST = [[-20, 20]]
    TIME_LIST = [[0], [1], [2], [0, 1, 2]]
    SIM_MIN = 10
    SIM_MAX = 10
