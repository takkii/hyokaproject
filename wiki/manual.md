### 変更履歴

- [x] バックエンド実装から、顔写真の比較と精度評価をする

- [x] 精度評価、結果の検証と動作確認をする

- [x] bootstrapをレイアウトに適用する

- [x] style.css、テキストの中央揃えをcssで実行する

- [x] 精度評価、index.htmlに統一しメッセージをpython処理で表示する

- [x] 精度評価、アタリの単語をランダムで表示する

- [x] アタリとハズレで色付け、ハズレのメッセージを英文で追加しました。

- [x] python-dotenv、値やPATHの直書きを封じました。

- [x] golden-eagle、精度評価を.envから呼び出す仕様にしました。

```markdown
# プロジェクトに移動
cd hyokaproject

# 依存ライブラリ解消
pip3 install -r requirements.txt 

# 79，80行目付近, ユーザ名とパスワードなどをローカルDB用に変更
hyokaproject/settings.py

# mysql or mariadb、hyokaproject_developを手動でも作れる
mysql -u root -p
create database hyokaproject_develop;

# DBマイグレーションをする
python manage.py migrate

# before_param, after_paramに比較する顔写真を設定
# 必要であれば、golden-eagleと通常の精度評価を調整
.env

# 起動 http://localhost:8000/
python manage.py runserver  
```

_※ 上記設定例は、必要があれば更新する。_

> 更新: 2025/08/27 🆙