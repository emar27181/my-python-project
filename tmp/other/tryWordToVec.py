import spacy
nlp = spacy.load('ja_ginza')
doc1 = nlp('明るい')

for sent in doc.sents:
    for token in sent:
        print(
            token.i,
            token.text,
            token.vector,
            token.vector.shape,
        )