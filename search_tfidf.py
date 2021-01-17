from math import log
from janome.tokenizer import Tokenizer
from util import *

# データセットを読み込み
documents = 



# 注目する単語（トークン）が名詞であるかどうか



# テキストから名詞の列を抽出



# 名詞の個数をカウント



# TF値を計算



# （あらかじめ計算された）TF値を参照



# 全ての単語のTF値を計算



# 注目する単語（トークン）が名詞列に含まれるか




# 辞書の要素をインクリメント


# IDF辞書を更新



# 全ての単語のIDF値を計算



# TF値およびIDF値を表示
def print_tf_idf_values(query):
    # キーワードを表示
    tokens = get_nowns(query)
    print('keywords: ', end='')
    for token in tokens:
        print(token.surface + ', ', end='')
    print()

    # TFを表示
    print('--- TF values ---')
    for i in range(len(documents)):
        print('{}: '.format(documents[i][2]), end='')
        for token in tokens:
            print('{:.5f}, '.format(get_tf_value(token.surface, i)), end='')
        print()

    print('--- IDF values ---')
    print('IDF: ', end='')
    for token in tokens:
        print('{:.5f}, '.format(dic_idf[token.surface]), end='')
    print()


# Main

