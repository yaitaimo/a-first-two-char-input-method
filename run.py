#!/usr/bin/evn python3

import re
import sys

import Mykytea


def get_mk(opt=''):
    mk = Mykytea.Mykytea(opt)
    return mk

def get_kytea_txt(mk, txt):
    n_txt = mk.getTagsToString(txt)
    p = re.compile('\s\s/UNK')
    n_txt = re.sub(p, '', n_txt)
    return n_txt

if __name__ == '__main__':
    if len(sys.argv) != 1:
        mk = get_mk(' '.join(sys.argv[1:]))
    else:
        mk = get_mk()
    while True:
        try:
            txt = input()
        except EOFError:
            break
        n_txt = get_kytea_txt(mk, txt)
        print(n_txt)
