#!/usr/bin/env python3

'''
コーパス作成用スクリプト
TODO:大きなデータを扱いうる仕様とすべき．
'''

from os import path
import re
from sys import argv, exit, stderr


def load_data(fpath):
    with open(fpath) as f:
        data = f.readlines()

    return data


def containsAny(str, set):
    return 1 in [c in str for c in set]


def containsWhich(str, set):
    return [c for c in set if c in str]


def add_index(word):
    if len(word) < 2:
        return "{0}/{0}".format(word)
    index = word[:2]
    return "{}/{}".format(index, word)


def make_corpus(data):
    n_data = []
    p = re.compile('[^,.\w\s]')
    bad_line_cnt = 0
    all_line_cnt = 0
    for line in data:
        all_line_cnt += 1
        error_flag = False
        if p.search(line):
            bad_line_cnt += 1
            continue
        words = line.split()
        converted_words = []
        for word in words:
            n_word = add_index(word)
            s_chara = containsWhich(n_word, set([',', '.', '"', '..', ',,']))
            if s_chara:
                if len(s_chara) > 1:
                    error_flag = True
                    break
                if len(word) == 1:
                    converted_words.append(n_word)
                else:
                    n_word = n_word.replace(s_chara[0], '')
                    converted_words.append(n_word)
                    converted_words.append('{0}/{0}'.format(s_chara[0]))
            else:
                converted_words.append(n_word)
        if error_flag:
            continue
        n_data.append(' '.join(converted_words))
    print('all line = {}, bad line = {}.'.format(all_line_cnt, bad_line_cnt), 
          file=stderr)
    return n_data


def save_data(name, data):
    with open('corpus/{}.txt'.format(name), 'a') as f:
        for d in data:
            f.write('{}\n'.format(d))


if __name__ == '__main__':
    if len(argv) == 1:
        exit('ファイルパスを指定して下さい')

    for fpath in argv[1:]:
        data = load_data(fpath)
        n_data = make_corpus(data)
        base = path.basename(fpath)
        name = path.splitext(base)[0]
        save_data(name, n_data)
