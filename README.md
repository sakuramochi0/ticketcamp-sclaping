# ticketcamp-scalping
[チケットキャンプ](https://ticketcamp.net) で定額以上で販売されたチケットの金額を集計するプログラム

## 使い方
python3 をインストール後、次のコマンドを実行すると、「プリティーリズム」「キンプリ」シリーズのチケット情報が CSV 形式で取得できます。
```sh
pip install -r requirements.txt
scrapy crawl ticketcamp -o prettyrhythm.csv
```

## データの活用例
- [チケットキャンプで取引されたプリティーリズム/キンプリのチケットに関するいろいろな数字💴](https://docs.google.com/spreadsheets/d/1daM1WO5JkqrsLcTQziEpXz5Dx30k2pIp3X35jHU5JYc/edit?usp=sharing)
  - 2017年7月28日現在の、プリティーリズム/キンプリに関するチケットの数字を集計したものです。
  ![2017/07/28までに取引されたプリティーリズム/キンプリのチケット総額内訳](https://docs.google.com/spreadsheets/d/1daM1WO5JkqrsLcTQziEpXz5Dx30k2pIp3X35jHU5JYc/pubchart?oid=974114977&format=image)

## ライセンス
- GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
チケット転売問題を解決し、さまざまなイベントの出演者・参加者の利益を守るために、少しでも役に立つことを願っています。
