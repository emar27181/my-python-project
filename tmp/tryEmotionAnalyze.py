
from transformers import pipeline
from transformers import BertForSequenceClassification
from transformers import BertJapaneseTokenizer

model = BertForSequenceClassification.from_pretrained(
    'cl-tohoku/bert-base-japanese-whole-word-masking')
tokenizer = BertJapaneseTokenizer.from_pretrained(
    "cl-tohoku/bert-base-japanese-whole-word-masking")
nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
# 以下のモデルでは日本語の感情分析に特化しているが、オンラインデータが消されてしまった？
# nlp = pipeline("sentiment-analysis", model="daigo/bert-base-japanese-sentiment", tokenizer="daigo/bert-base-japanese-sentiment")

print(nlp("この商品を買ってよかったです"))
print(nlp("きれいな湖"))
print(nlp("この本は最悪です"))
