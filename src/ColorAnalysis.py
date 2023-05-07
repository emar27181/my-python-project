import MeCab
with open("data/input/ColorInput.txt", "r") as file:
    inputText = file.read()
print("inputText:\n " + inputText + "\n")

mecab = MeCab.Tagger("-Owakati")
node = mecab.parseToNode(inputText)

while node:
    print(node.surface+': '+node.feature.split(",")[0])
    node = node.next

"""
with open("data/output/ColorOutput.txt", "w") as file:
    file.write(result)
"""
