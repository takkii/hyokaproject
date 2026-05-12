### search.cpp

```markdown
# ./functions (rice関連ファイルはビルドのみ)
make distclean
ruby extconf.rb
make

# ./functions/shell
g++ -o check check.cpp
./check

> Match word contain Doe in ../../effect.txt
```

_リアルタイム顔認識システムをOSなどで、ログインする場合の想定です。_

※ 既存のC++コードを修正しました。適宜、QtのGUIパーツ(ボタン)を組み合わせるとよいかもしれない。