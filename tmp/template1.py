import MeCab

mecab= MeCab.Tagger('-Owakati')

text="これはテスト用の文章です。"

#parseToNodeで形態素解析
node = mecab.parseToNode(text)

#形態素1つ1つを処理
while node:
    print('****************************')
    print('[['+node.surface+']]')
    print('[品詞]0:'+node.feature.split(",")[0])
    print('[品詞細分類1]1:'+node.feature.split(",")[1])
    print('[品詞細分類2]2:'+node.feature.split(",")[2])
    print('[品詞細分類3]3:'+node.feature.split(",")[3])
    print('[活用型]4:'+node.feature.split(",")[4])
    print('[活用系]5:'+node.feature.split(",")[5])
    print('[原形]6:'+node.feature.split(",")[6])
    if len(node.feature.split(",")) >= 8:
        print('[読み]7:'+node.feature.split(",")[7])
        print('[発音]8:'+node.feature.split(",")[8])
    node = node.next