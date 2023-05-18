import spacy
nlp = spacy.load('ja_ginza')

text_list = []
doc_list = []
# texts = ['明るい赤', 'あかるい赤', '明るい緑', '明るい橙', 'まぶしい赤', '暗い赤']
texts = ['赤', '緑', '橙', '青', '紫']
texts = ['明るい赤', '明るいピンク', '明るい緑', '明るい橙', '明るい青', '明るい紫']
# texts = ['明るい', 'あかるい', '暗い', 'まぶしい']

for text in texts:
    text_list.append(text)
    doc_list.append(nlp(text))

for i, doc1 in enumerate(doc_list):
    for j, doc2 in enumerate(doc_list[i:]):
        if (i != (i+j)):
            # print(i, i + j)
            print("\n" + text_list[i] + " : " + text_list[i+j])
            print(doc_list[i].similarity(doc_list[i+j]))

