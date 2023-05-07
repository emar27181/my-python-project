import MeCab
with open("data/input/test_input.txt", "r") as file:
    inputText = file.read()

mecab = MeCab.Tagger("-Owakati")

# input_file = 'data/input/test_input.txt'
print("inputText:  " + inputText)