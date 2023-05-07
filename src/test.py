import MeCab

# MeCabの初期化
mecab = MeCab.Tagger()

# 形態素解析の実行
imputText = "これはテスト用の文章です。"
result = mecab.parse(imputText)
lines = result.split('\n')

nouns = []
verbs = []
adjectives = []

print("print all: \n" + result)
# print("print check: \nresult[0]: " + result[0] + result[1] )

"""
for line in lines:
    if line == 'EOS':
        break
    else:
        # 解析結果の各要素はタブ区切りで表されており、最初の要素が表層形、次の要素が品詞情報などです
        surface, feature = line.split('')
        features = feature.split(',')
        pos = features[0]   # 品詞情報はfeaturesの最初の要素にあります

        # 品詞ごとに結果を保存
        if pos == '名詞':
            nouns.append(surface)
        elif pos == '動詞':
            verbs.append(surface)
        elif pos == '形容詞':
            adjectives.append(surface)
        # 他の品詞に対応する処理も追加

# 品詞ごとに保存された結果を表示
print("名詞:", nouns)
print("動詞:", verbs)
print("形容詞:", adjectives)
"""

