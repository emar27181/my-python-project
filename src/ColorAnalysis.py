import MeCab
with open("data/input/ColorInput.txt", "r") as file:
    inputText = file.read()
print("inputText:\n " + inputText + "\n")

# mecab = MeCab.Tagger("-Owakati")
mecab = MeCab.Tagger()
result = mecab.parse(inputText)

print("result all: \n" + result)

with open("data/output/ColorOutput.txt", "w") as file:
    file.write(result)