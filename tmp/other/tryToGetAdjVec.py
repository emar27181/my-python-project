import spacy
import numpy as np

# Ginzaモデルを読み込む
nlp = spacy.load("ja_ginza")

# 入力テキスト
text = "この本はとても面白いです"

# テキストをGinzaで解析する
doc = nlp(text)

# 形容詞のベクトルを格納するリスト
vectors = []

# 形容詞のみの部分を抽出してベクトルを取得する
for token in doc:
    if token.pos_ == "ADJ":  # 形容詞の場合
        vector = token.vector
        vectors.append(vector)

# ベクトルをNumPy配列に変換
vectors = np.array(vectors)

# 形容詞のベクトルを表示
for vector in vectors:
    print(vector)