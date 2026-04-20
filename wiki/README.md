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
# 百人一首
issus = '/hyokapp/txt/hyakunin.txt'
```

※ hyokaproject.log、顔認識対象者(名前: 英文字)を探索する関数で操作を想定しています。

> 更新: 2026/04/20 🆙
