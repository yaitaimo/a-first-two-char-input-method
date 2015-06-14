#!/usr/bin/env python3

'''
コーパス作成用スクリプト
TODO:大きなデータを扱いうる仕様とすべき．
'''

from re
from sys import argv, exit


def load_data():
    if len(argv) == 1:
        exit('ファイル名を指定して下さい')

    with open(argv[1]) as f:
        data = f.readlines()

    return data


def containsAny(str, set):
    return 1 in [c in str for c in set]


def containsWhich(str, set):
    return 1 in [c in str for c in set if c in str]


def add_index(word):
    if len(word) < 2:
        return "{0}/{0}".format(word)
    index = word[:2]
    return "{}/{}".format(index, word)


def make_corpus():
    n_data = []
    p = re.compile('[^,.\w]')
    for line in data:
        if p.search(line):
            continue
        words = line.split()
        for word in words:
            n_word = add_index(word)
            s_cahra = containsWhich([n_word, set(',', '.', '"')])
            if s_chara:
                if len(s_chara) > 1:
                    exit('Can\'t treat "{}"'.format(line))
                n_word.replace(s_chara[0], "")
                converted_words.append(n_word)
                converted_words.append('{0}/{0}'.foramt(s_chara[0]))
            else:
                converted_words.append(n_word)
        n_data.append(' '.join(converted_words))
    return n_data


def save_data(data):
    with open('two_chara_index.corpus', 'a') as f:
        for d in data:
            f.write('{}\n'.format(d))


if __name__ = '__main__':
    data = load_data()
    n_data = make_corpus(data)
    save_data(n_data)
