
from transformers import pipeline
from transformers import BertForSequenceClassification
from transformers import BertJapaneseTokenizer

model = BertForSequenceClassification.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
tokenizer = BertJapaneseTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

print(nlp("この商品を買ってよかったです"))
print(nlp("きれいな湖"))
print(nlp("この本は最悪です"))
