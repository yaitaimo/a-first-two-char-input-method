# a-first-two-char-input-method

[京都テキスト解析ツールキット（KyTea）](http://www.phontron.com/kytea/)を利用する．  
入力を2文字区切りのヒント文として扱い（実際には1文字としても扱うことが出来る），もっとも可能性の高い単語の組み合わせとして文の出力を行うシステムを構築する．  
ただし，英文のみを対象とする．

例えば，学習済みの sample.dat を用いて，以下の用に解が得られる．  
```
$ python3 run.py -model sample.dat
Thisape.
Th/there is/is a/a pe/people ./.
```

（sample.dat のダウンロードは[こちら](https://github.com/yaitaimo/a-first-two-char-input-method/releases/tag/1)）

## 利用の流れ

1. 文書を用意し，コーパスを作成する  
2. 1で作ったコーパスに対して，KyTeaのモデルを構築する  
3. 2で構築したモデルを使って変換をためしてみる  

### 1. コーパスの作成
Create corpus with what kind of documents you need. (English only)  
The documents' format must be following.

"""
This is a pen.  
How are you today.  
Children are playing outside.  
...  
"""  

```
$ echo "This is a pen." > test.txt

$ python3 make_corpus.py test.txt

$ cat corpus/test.txt  
Th/This is/is a/a pe/pen ./.
```

### 2. コーパスを用いたモデルの構築  
Train KyTea model into `model.dat`.
```
$ train-kytea -full corpus/test.txt -model model.dat
```

### 3. 入力された文字列を適当な文章に変換  
Convert input string to appropriate sentence.  
```
$ python3 run.py -model model.dat  
Thisape.
Th/This is/is a/a pe/pen ./.
```

## 環境
- KyTea
  - For mac: `brew install kytea` 

- Python 3 
  - Mykytea-python

```
$ pip3 install -r requirements.txt
```
