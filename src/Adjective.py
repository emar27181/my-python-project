import spacy
nlp = spacy.load('ja_ginza')
DEBUG = False


class Adjective:
    def __init__(self, num, adverb, saturation, value):
        self.num = num
        self.adverb = adverb
        self.saturation = saturation
        self.value = value

    def getSaturation(self):
        return self.saturation

    def getValue(self):
        return self.value

    def getVector(self):
        # 入力された文章自体のベクトルを初期実装としてreturn
        doc = nlp(self.adverb)
        vector = doc.vector
        return vector


# 空の配列
adjective_list = []

# データを用意
data = [
    (1, "明るい", 70, 80),
    (2, "暗い", 20, 60),
    (3, "鮮やかな", 90, 90)
]

# クラスのインスタンスを生成し、配列に追加
for item in data:
    adj = Adjective(*item)  # タプルの要素を展開して引数に渡す
    adjective_list.append(adj)

# 配列の要素を表示
for adj in adjective_list:
    print(adj.num, ".", adj.adverb, ": (", adj.saturation, ",", adj.value, ")")
    if (DEBUG):
        print(adj.getVector())

x = adjective_list[0].getSaturation()
print(x)
y = adjective_list[0].getValue()
print(y)
z = adjective_list[2].getVector()
# print(z)
