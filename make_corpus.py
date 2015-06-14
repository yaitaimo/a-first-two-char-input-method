#!/usr/bin/env python3

'''
コーパス作成用スクリプト
TODO:大きなデータを扱いうる仕様とすべき．
'''

import sys


def load_data():
    pass


def add_index(word):
    if len(word) < 2:
        return "{}/{}".format(word, word)
    index = word[:2]
    return "{}/{}".format(index, word)

def make_corpus():
    n_data = []
    for line in data:
        words = line.split()
        # TODO:どうやって","や"."を分割したらよいか
        converted_words = map(add_index, words)
        n_data.append(' '.join(converted_words))
    return n_data


if __name__ = '__main__':
    data = load_data()
    n_data = make_corpus(data)


