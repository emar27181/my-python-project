# 「sentiment-analysis（感情分析）」のパイプライン
from transformers import pipeline
classifier = pipeline("sentiment-analysis")

# 「I hate you（嫌い）」を感情分析
result = classifier("I hate you")[0]
print(f"label: {result['label']}, with score: {round(result['score'], 4)}")

# 「I love you（好き）」を感情分析
result = classifier("I love you")[0]
print(f"label: {result['label']}, with score: {round(result['score'], 4)}")