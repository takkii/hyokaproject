### 更新履歴

- [x] バックエンド実装から、顔写真の比較と精度評価をする。
- [x] 精度評価、結果の検証と動作確認をする。
- [x] bootstrapをレイアウトに適用する。
- [x] style.css、テキストの中央揃えをcssで実行する。
- [x] 精度評価、index.htmlに統一しメッセージをpython処理で表示する。
- [x] ⭕と❎の絵文字で表現、⭕は百人一首をランダムで表示する。
- [x] ⭕と❎の絵文字で表現、❎は精度評価数値が既定値より少ないことを表示する。
- [x] python-dotenv、通常の精度評価の浮動小数点数やPATHをdotenvで設定できるようにした。
- [x] golden-eagle、同様に精度評価の浮動小数点数を.envから呼び出す仕様にする。
- [x] bakachon、接続完了。2度呼び出されます。2度めは撮り直しが必要かどうかです。
- [x] 画像変換処理、JPEG→GIF。意図しない例外を発生しないように変更しました。
- [x] 全体のリファクタリング、nyasocom_sun_pg_winに寄せる方向性で書きました。
- [x] Python3の仕様かな...、値の定義を2回読もうとすると何も表示しないため、再度値を定義し直した。
- [x] .env初期値、顔認識システム精度評価の数値を0.24未満で例外発生にします。
- [x] 顔写真を撮影するときは、照明を点けて明るいところで撮影してください。

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

# 起動 http://localhost:8000/hyokapp/
python manage.py runserver

# インストール sheltered-girl
gem install sheltered-girl

# pass.txt内探索
aqua -z pass.txt TRUE
# 1 : TRUE
```

_※ 顔認識システムはにゃそこん参ぴーじーうぃんと併用することを想定しています。_

> 更新: 2025/10/07 🆙