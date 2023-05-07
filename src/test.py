import MeCab

# MeCabの初期化
mecab = MeCab.Tagger()

# 形態素解析の実行
result = mecab.parse("これはテスト用の文章です。")

# 解析結果の表示
print(result)