### 変更履歴

- [x] バックエンド実装から、顔写真の比較と精度評価をする
- [x] 精度評価、結果の検証と動作確認をする
- [x] bootstrapをレイアウトに適用する
- [x] style.css、テキストの中央揃えをcssで実行する
- [x] 精度評価、index.htmlに統一しメッセージをpython処理で表示する
- [x] 精度評価、◯の単語をランダムで表示する
- [x] ◯と☒で色付け、☒のメッセージを英文で追加する
- [x] python-dotenv、通常の精度評価の浮動小数点数やPATHの直書きを封じる
- [x] golden-eagle、上記と同様に精度評価の浮動小数点数を.envから呼び出す仕様にする
- [x] bakachon、接続完了。2度呼び出されたときは2度目を消す。
- [x] 画像変換処理、JPEG→GIF。多重アクセスするとRuntimeErrorを発生させる。
- [x] 全体のリファクタリング、nyasocom_sun_pg_winに寄せる。

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

# zinbeijettをインストール
git clone git@github.com:takkii/zinbeijett.git
gem build zinbeijett.gemspec
gem install zinbeijett-3.0.1.pre.2025.08.09.gem

# pass.txt内探索
aqua -z pass.txt TRUE
# 1 : TRUE
```

_※ 設定例、開発または本番環境などに応じて適宜変更する。_

☆nyasocom_sun_pg_win、メンバーズカード(pass.txt)中のメッセージが変更されると動作しない。

→ 発行するとき、顔認識システムを起動するか手動でメンバーズカードを作成する必要がある。

> 更新: 2025/09/30 🆙