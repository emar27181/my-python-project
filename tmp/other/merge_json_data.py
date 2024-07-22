import json

# 1. JSONファイルを読み込む

file_path1 = "tmp/other/data/input/inputOrderUsedColorsAmount_gaakoInstagram.json"
file_path2 = "tmp/other/data/input/inputOrderUsedColorsAmount_NCG.json"

with open(file_path1, 'r', encoding='utf-8') as f1:
    data1 = json.load(f1)

with open(file_path2, 'r', encoding='utf-8') as f2:
    data2 = json.load(f2)

# 2. JSONデータをマージする
# 例として、単純にdata1とdata2をリストとして結合する場合
merged_data = data1 + data2

# 3. マージしたデータを新しいJSONファイルに書き込む
with open('tmp/other/data/output/inputOrderUsedColorsAmount.json', 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=4)

print("JSONファイルがマージされました。")
