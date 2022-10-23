# 確率計算

帽子の中に青玉(5個)、赤玉(4個)、緑玉(2個)が入れてからランダムに4個を抽出。
<br>
抽出結果に赤玉(1個)、緑玉(2個)を含む確率を多数の実験からカウント。

## 1. 実行準備

リモートリポジトリから取得後に Python を対話モードで起動

```
$ git clone https://github.com/Makoto-Araki/boilerplate-time-calculator.git
$ cd boilerplate-time-calculator
$ python (対話モードで起動)
```

## 2. 帽子クラス

インスタンス生成時に各色の玉数を指定、ランダムに4個抽出するメソッド実行

```
>>> hat = prob_calculator.Hat(blue=5, red=4, green=2)
>>> hat.draw(4)                    # ランダムに4個抽出
['green', 'blue', 'green', 'red']  # 抽出結果
```

## 3. 関数実行

内部で帽子インスタンスからメソッド実行、赤玉(1個)、緑玉(2個)を含む確率をカウント

```
>>> hat = prob_calculator.Hat(blue=5, red=4, green=2)
>>> probability = prob_calculator.experiment(
>>>     hat=hat,                                # 帽子インスタンス
>>>     expected_balls={"red": 1, "green": 2},  # ターゲットの組み合わせ
>>>     num_balls_drawn=4,                      # 抽出数
>>>     num_experiments=3000                    # 実験回数
>>> )
>>> print("Probability:", probability)
Probability: 0.078  # 確率7%(0.07)
```