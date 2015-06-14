#!/usr/bin/evn python3

import Mykytea
import re


def get_mk():
    opt = "-model /usr/local/share/kytea/model.bin"
    mk = Mykytea.Mykytea(opt)
    return mk

def get_kytea_txt(mk, txt):
    n_txt = mk.getTagsToString(txt)
    p = re.compile('\s\s/UNK')
    n_txt = re.sub(p, '', n_txt)
    return n_txt

if __name__ == '__main__':
    mk = get_mk()
    while True:
        txt = input()
        n_txt = get_kytea_txt(mk, txt)
        print(n_txt)
