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

> 更新: 2025/10/11 🆙
