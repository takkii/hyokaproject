### 仕様: 実装済み

- [x] バックエンド実装から、顔写真の比較と精度評価しました。
- [x] 精度評価、結果の検証と動作確認をしました。
- [x] ⭕ 百人一首をランダムで表示しました。
- [x] python-dotenv、通常の精度評価の浮動小数点数やPATHをdotenvで設定できるようにしました。
- [x] bakachon、接続完了。起動時、2度呼び出されるが2度目は撮り直しが必要かどうかを確認しました。
- [x] 画像変換処理、JPEG→GIF。意図しない例外を発生しないように変更しました。
- [x] 値の定義を2回読もうとすると何も表示しないため、再度値を定義し直しました。
- [x] golden-eagle、requirements.txtを移植しました。
- [x] hyokaproject.log、データ分析の対象にしました。
- [x] hyokaproject.log、システム停止時などのログも出力されるため気になる人は手動で消して下さい。
- [x] リアルタイム顔認識に対応しました。
- [x] リアルタイム顔認識のため、bootstrap/style.css/index.htmlを廃止しました。
- [x] wiki/README.md内.env設定をhyokaproject直下に貼り付けてお使い下さい。

_顔写真を撮影するときは、照明を点けて明るいところで撮影してください。_

#### 環境構築

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

※ 今回、DBは使わないので起動のために必要です。

# before_param, after_paramに比較する顔写真のPATHを追加
# 初期値を設定済、必要であればgolden-eagleと通常の精度評価を調整
# hyokaproject/settings.py
# 79-80行目付近のユーザ名とパスワードなどを.envに設定する
.env

# 起動 http://localhost/hyokapp/
python manage.py runserver localhost:80
```

#### .env

```markdown
# Equal Face Photo origin folder.
before_param = "./Images/face.gif"
# Don't change.
lo_num = 0.289
# DB Name.
NAME = "hyokaproject_develop"
# DB User or admin
USER = "root"
# DB password
PASSWORD = "20070920"
# Startup, face photo.
picture_images = "./Images/face.jpg"
bakachon_folder = "bakachon"
# First Name, Takayuki.
one_name = "Takayuki"
# face-recognition
fl_num = 0.4
# Default settings, 100KB hyokaproject.log
int_num = 100
# Webcam Built-in camera (0 or 1) | view.py
int_conn = 0
```

_更新履歴: 2026/04/21🔄_
