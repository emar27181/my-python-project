import spacy
nlp = spacy.load('ja_ginza')
DEBUG = False


def getVector(text):
    # 入力された文章自体のベクトルを初期実装としてreturn
    doc = nlp(text)
    vector = doc.vector
    return vector


class Adjective:
    def __init__(self, num, text, saturation, value):
        self.num = num
        self.text = text
        self.saturation = saturation
        self.value = value
        self.vector = getVector(self.text)
        self.doc = nlp(text)

    def getSaturation(self):
        return self.saturation

    def getValue(self):
        return self.value


# 空の配列
adjective_list = []

# データを用意
data = [
    (0, "明るい", 70, 80),
    (1, "白い", 15, 90),
    (2, "パステルな", 35, 90),
    (3, "薄い", 40, 85),
    (4, "ビビットな", 60, 90),
    (5, "眩しい", 70, 90),
    (6, "鮮やかな", 90, 90),
    (7, "原色の", 100, 100),
    (8, "淡い", 50, 75),
    (9, "透き通る", 45, 70),
    (10, "濃い", 80, 60),
    (11, "深い", 85, 45),
    (12, "灰色の", 15, 20),
    (13, "鼠色の", 15, 50),
    (14, "和風の", 65, 25),
    (15, "漆黒の", 90, 25),
    (16, "黒い", 90, 10),
]

# Adjectiveクラスのインスタンスを生成し、配列に追加
for item in data:
    adj = Adjective(*item)  # タプルの要素を展開して引数に渡す
    adjective_list.append(adj)

# 配列の要素を表示
for adj in adjective_list:
    print(adj.num, ".", adj.text, ": (", adj.saturation, ",", adj.value, ")")
    if (DEBUG):
        print(adj.vector)

def caluculateMaxSimilarity(doc):
    maxSim = -1
    for adj in adjective_list:
        print("\n", adj.text)
        print(doc.similarity(adj.doc))

x = "明るい"
docX = nlp(x)
caluculateMaxSimilarity(docX)
