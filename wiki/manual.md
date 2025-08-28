### 変更履歴

- [x] バックエンド実装から、顔写真の比較と精度評価をする

- [x] 精度評価、結果の検証と動作確認をする

- [x] bootstrapをレイアウトに適用する

- [x] style.css、テキストの中央揃えをcssで実行する

- [x] 精度評価、index.htmlに統一しメッセージをpython処理で表示する

- [x] 精度評価、アタリの単語をランダムで表示する

- [x] アタリとハズレで色付け、ハズレのメッセージを英文で追加する

- [x] python-dotenv、通常の精度評価の浮動小数点数やPATHの直書きを封じる

- [x] golden-eagle、上記と同様に精度評価の浮動小数点数を.envから呼び出す仕様にする

```markdown
# プロジェクトに移動する
cd hyokaproject

# 依存ライブラリ解消する
pip3 install -r requirements.txt 

# mysql or mariadb、hyokaproject_developを手動で作る
mysql -u root -p
create database hyokaproject_develop;

# DBマイグレーションをする
python manage.py migrate

※ DBは現在使わないので、起動のために必要

# before_param, after_paramに比較する顔写真のPATHを追加
# 初期値を設定済、必要であればgolden-eagleと通常の精度評価を調整
# hyokaproject/settings.py
# 79-80行目付近のユーザ名とパスワードなどを.envに設定する
.env

# 起動 http://localhost:8000/
python manage.py runserver  
```

_※ 上記設定例は、必要があれば更新する。_

> 更新: 2025/08/29 🆙