import MeCab
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
DEBUG = True

# Mecabで形容詞を抽出してベクトル表現を作成する関数
def extract_adjectives(text):
    mecab = MeCab.Tagger("-Owakati")
    node = mecab.parseToNode(text)
    adjectives = []
    while node:
        if "形容詞" in node.feature.split(",")[0]:
            adjectives.append(node.surface)
        node = node.next
    return adjectives

# 形容詞のベクトル表現を作成する関数
def create_vector_representation(adjectives, word_embeddings):
    vectors = []
    for adj in adjectives:
        if adj in word_embeddings:
            vectors.append(word_embeddings[adj])
    return np.array(vectors)

# コサイン類似度を計算する関数
def compute_cosine_similarity(vectors):
    if len(vectors) < 2:
        return None
    similarities = cosine_similarity(vectors)
    return similarities[0, 1]  # 最初の2つの形容詞の類似度を返す

# Word Embeddings (単語のベクトル表現)を用意する（ダミーデータ）
word_embeddings = {
    "大きい": np.array([0.9, 0.1, 0.9]),
    "小さい": np.array([0.1, 1.0, 0.1]),
    "高い": np.array([0.8, 0.2, 0.9]),
    "低い": np.array([0.0, 0.8, 0.1])
}

# テキストから形容詞を抽出してベクトル表現を作成
text = "この虫は小さいが、態度は大きいです"
text = "この本はとても大きいし、値段も高いです"
text = "この家は小さいが、家賃は高いです"
text = "この子は背は低いし、態度も小さい"

adjectives = extract_adjectives(text)
vectors = create_vector_representation(adjectives, word_embeddings)


# コサイン類似度を計算
similarity = compute_cosine_similarity(vectors)

print("形容詞:", adjectives)
print("コサイン類似度:", similarity)
