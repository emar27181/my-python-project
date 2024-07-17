# 「sentiment-analysis（感情分析）」のパイプライン
from transformers import pipeline
classifier = pipeline("sentiment-analysis")

paragraphs = ["I hate you", "I love you", "I like you", "I don't hate you", "I don't love you", "I don't like you",
              "I have a big dream", "It is difficult for me to speak English well",
              "I have a neutral opinion", "deep blue", "shiny red", "deep black", "deep white",
              "dackd desac", "hoge hoge", "positive negative", "negative positive"]

for paragraph in paragraphs:
    result = classifier(paragraph)[0]
    print(
        f"label: {result['label']}, with score: {round(result['score'], 4)}, paragraph: {paragraph}")
