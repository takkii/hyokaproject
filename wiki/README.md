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

※ hyokaproject.log、顔認識対象者(名前: 英文字)を探索する関数で操作を想定しています。

> 更新: 2026/04/20 🆙
