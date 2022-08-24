<div align="center">

![Last commit](https://img.shields.io/github/last-commit/Comamoca/stampy?style=flat-square)
![Repository Stars](https://img.shields.io/github/stars/Comamoca/stampy?style=flat-square)
![Issues](https://img.shields.io/github/issues/Comamoca/stampy?style=flat-square)
![Open Issues](https://img.shields.io/github/issues-raw/Comamoca/stampy?style=flat-square)
![Bug Issues](https://img.shields.io/github/issues/Comamoca/stampy/bug?style=flat-square)

#  stampy 🍣

４文字の文字列をスタンプ風の画像に変換します。

![生成出来る画像の例](./out.png "生成出来る画像の例")

</div>

<table>
  <thead>
    <tr>
      <th style="text-align:center">🍡日本語</th>
      <th style="text-align:center">🍔Sorry, Japanease Only</th>
    </tr>
  </thead>
</table>

<div align="center">

</div>

> **Note**
> バージョン0.1.3からデフォルトでランダムな色を生成する仕様になりました。
> デフォルト値の黒色を利用していた方は`--color`オプションで`0,0,0`を指定してください。

## 🚀 使い方

```
# 文字列を与えるとスタンプ風の画像を生成します。デフォルトでランダムな文字色になります。
stampy にんにん

# オプションで色(RGB)を指定する事ができます。
stampy にんにん --color 100,180,123

# ４文字以外の文字列はエラーになります。
stampy にゃんにゃん

# カレントディレクトリにoutput.pngという画像が出力されます。
```

## ⬇️  Install

```sh
# PyPIからでもインストール出来ます。
pipx install stampy

# インストールにはpipxを推奨します。
pipx install git+https://github.com/Comamoca/stampy
```

## ⛏️   開発

```sh
git clone https://github.com/Comamoca/stampy
cd stampy
poetry install
poetry run python src/main.py
```
## 📝 Todo

Not yet...💤

## 📜 ライセンス

MIT
[SIL Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL_web)

### 🧩 Modules

[💕 スペシャルサンクス](#💕スペシャルサンクス)

## 👏 影響を受けたプロジェクト

Not yet...💤

## 💕 スペシャルサンクス

- [M+フォント](https://mplusfonts.github.io/)

- [pillow](https://github.com/python-pillow/Pillow)

- [click](https://github.com/pallets/click)
