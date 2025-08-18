# 🚀 Harukazeガイドライン静的サイト生成ツール

MarkdownファイルからプロフェッショナルなHTMLサイトを自動生成するツールです。

## ✨ 特徴

- 📁 **フォルダ構造自動認識**: ガイドラインプロジェクトの構造をそのまま反映
- 🎨 **美しいデザイン**: プロフェッショナルなUI/UXを自動適用
- 📱 **レスポンシブ対応**: PC・タブレット・スマートフォンで最適表示
- ⚡ **高速生成**: 数百ファイルでも数秒で完了
- 🔄 **バージョン管理**: ガイドラインのバージョンを自動認識

## 📋 必要な環境

- Python 3.7以上
- macOS, Windows, Linux対応

## 🛠️ セットアップ

### 1. 必要なライブラリをインストール

```bash
pip install -r requirements.txt
```

### 2. スクリプト実行

```bash
python generate_site.py
```

## 📁 生成されるファイル

```
site_output/
├── README.html (トップページ)
├── 01_プロジェクト管理/
│   ├── 要件定義.html
│   └── プロジェクト進捗.html
├── 02_開発中ドキュメント/
│   └── ...
└── 03_現行版ガイドライン/
    └── ...
```

## 🎯 使用方法

### ステップ1: ライブラリをインストール
```bash
cd "/Users/ogatahisashi/Library/CloudStorage/GoogleDrive-harukazeteam01@gmail.com/My Drive/HarukazeDatabase/guideline_site_generator"
pip install -r requirements.txt
```

### ステップ2: サイトを生成
```bash
python generate_site.py
```

### ステップ3: ブラウザで確認
生成された `site_output/README.html` をブラウザで開いてください。

## ⚙️ カスタマイズ

### 入力フォルダの変更
`generate_site.py` の以下の行を編集：

```python
ROOT_FOLDER = "あなたのフォルダパス"
```

### デザインの変更
`_templates/page.html` のCSSを編集してデザインをカスタマイズできます。

## 🔧 高度な使い方

### 自動更新の設定
macOSの場合、以下でcronジョブを設定できます：

```bash
# 毎日午前9時に自動生成
0 9 * * * cd "/path/to/guideline_site_generator" && python generate_site.py
```

### Webサーバーでの公開
生成されたファイルをWebサーバーにアップロードして公開：

```bash
# 簡易Webサーバーで確認
cd site_output
python -m http.server 8000
# http://localhost:8000 でアクセス
```

## 📊 サポートするMarkdown機能

- ✅ 見出し (H1-H6)
- ✅ リスト（順序なし・順序あり）
- ✅ コードブロック・インラインコード
- ✅ テーブル
- ✅ 引用
- ✅ リンク・画像
- ✅ 太字・斜体
- ✅ 目次自動生成

## 🎨 自動適用される機能

- 📋 **自動アイコン**: ファイル内容に応じて適切なアイコンを自動選択
- 🏷️ **バージョン認識**: v1.0, v2.0などのバージョンを自動検出
- 📱 **レスポンシブメニュー**: モバイルでも使いやすいナビゲーション
- 🎯 **アクティブページ表示**: 現在のページをハイライト

## 🆘 トラブルシューティング

### エラー: "No module named 'markdown'"
```bash
pip install markdown
```

### エラー: "Permission denied"
フォルダの書き込み権限を確認してください。

### 日本語が文字化けする
ファイルがUTF-8で保存されているか確認してください。

## 🔄 更新履歴

- **v1.0**: 初回リリース
- 自動サイドバー生成
- レスポンシブデザイン対応
- 日本語完全対応

## 📞 サポート

問題や要望があれば、Harukazeチームまでお気軽にご連絡ください。

---

**Harukazeチーム専用ツール** | 継続的改善を目指して 🚀