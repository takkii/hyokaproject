### C++プロジェクトの仕様

> ファイルを読み込み、指定する単語にマッチするとき条件分岐を行う。

```markdown
# ./functions (rice関連ファイルはビルドのみ)
make distclean
ruby extconf.rb
make

# ./functions/shell
g++ -o check check.cpp
./check

> Match word contain Doe in ../../effect.txt

# ./functions/search
searchプロジェクトをVisualStudioでビルドしてください。
```

_リアルタイム顔認識システムをOSなどで、ログイン認証する場合の想定です。_

>  ※ 適宜、QtのGUIパーツ(ボタン)を組み合わせるとよいかもしれない。