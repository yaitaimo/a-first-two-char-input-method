# a-first-two-char-input-method

京都テキスト解析ツールキット（KyTea）を利用して，入力を2文字区切りのヒント文として処理を行い（1文字も扱うことが出来る），もっとも可能性の高い単語の組み合わせとして文の出力を行うシステムを構築する．ただし，英文のみを対象とする．

例えば，学習済みの sample.dat を用いると，以下の用に解が得られる．
```
$ python3 run.py -model sample.dat
Thisape.
Th/there is/is a/a pe/people ./.
```

自分の利用したいドメインに対応した文書を用意し，そこからコーパスを作成し，KyTeaのモデルを構築することで，より適切な文章を組み立てることが可能となる．
（sample.dat のダウンロードは[こちら
](https://github.com/yaitaimo/a-first-two-char-input-method/releases/tag/1)）

## 環境構築
- [KyTea](http://www.phontron.com/kytea/)
  For mac: `brew install kytea` 

- Python 3 
  - Mykytea-python

```
$ pip3 install -r requirements.txt
```

## コーパスの作成
Create corpus with what kind of documents you need. (English only)
```
$ echo "This is a pen." > test.txt

$ python3 make_corpus.py test.txt

$ cat corpus/test.txt
Th/This is/is a/a pe/pen ./.
```
## コーパスを用いたモデルの構築
Training KyTea model.
```
$ train-kytea -full corpus/test.txt -model model.dat
```

## 2文字の入力を適当な文章に変換
Input any text, and get converted text.
```
$ python3 run.py -model model.dat
Thisape.
Th/This is/is a/a pe/pen ./.
```
