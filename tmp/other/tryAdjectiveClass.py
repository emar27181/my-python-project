class Adjective:
    def __init__(self, num, adverb, saturation, value, vector):
        self.num = num
        self.adverb = adverb
        self.saturation = saturation
        self.value = value
        self.vector = vector


# 空の配列
adjective_list = []

# データを用意
data = [
    (1, "明るい", 70, 80, [0.1, 0.3, 0.5]),
    (2, "暗い", 20, 60, [0.4, 0.6, 0.8]),
    (3, "鮮やかな", 90, 90, [0.2, 0.4, 0.6])
]

# クラスのインスタンスを生成し、配列に追加
for item in data:
    adj = Adjective(*item)  # タプルの要素を展開して引数に渡す
    adjective_list.append(adj)

# 配列の要素を表示
for adj in adjective_list:
    print(adj.num, ".", adj.adverb,
          ": ( ", adj.saturation, ",", adj.value, ")", adj.vector)
