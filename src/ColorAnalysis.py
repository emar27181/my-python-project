import MeCab
with open("data/input/ColorInput.txt", "r") as file:
    inputText = file.read()
print("inputText:\n" + inputText + "\n")

mecab = MeCab.Tagger("-Owakati")
node = mecab.parseToNode(inputText)

print("outputText:")
with open("data/output/ColorOutput.txt", "w") as file:
    while node:
        print(node.surface+': '+node.feature.split(",")[0])
        file.write(node.surface+': '+node.feature.split(",")[0] + "\n")
        node = node.next

