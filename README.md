# ticketcamp-scalping
[チケットキャンプ](https://ticketcamp.net) で定額以上で販売されたチケットの金額を集計するプログラム

## 使い方
python3 をインストールしてから、次のコマンドを実行すると、「プリティーリズム」「キンプリ」シリーズのチケット情報が CSV 形式で取得できます。
```sh
pip install -r requirements.txt
scrapy crawl ticketcamp -o prettyrhythm.csv
```
