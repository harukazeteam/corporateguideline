# 🚀 汎用静的サイト生成ツール - 使用マニュアル

## 📋 概要

どんなプロジェクトでも美しいHTMLサイトを自動生成できる汎用ツールです。設定ファイルを変更するだけで、新しいプロジェクトに対応できます。

## 🛠️ 新プロジェクトでの使用手順

### ステップ1: プロジェクトフォルダの準備

```bash
# 新しいプロジェクト用フォルダを作成
mkdir my_new_project_site
cd my_new_project_site

# 必要ファイルをコピー
cp /path/to/guideline_site_generator/generate_universal.py .
cp /path/to/guideline_site_generator/_templates .
cp /path/to/guideline_site_generator/requirements.txt .
```

### ステップ2: 設定ファイルの作成

`site_config.json` を作成：

```json
{
  "site_title": "あなたのプロジェクト名",
  "site_subtitle": "サブタイトル",
  "source_folder": "/path/to/your/markdown/files",
  "output_folder": "site_output",
  "template_file": "_templates/page_light.html",
  
  "include_files": [
    "README.md",
    "docs/guide.md",
    "docs/manual.md"
  ],
  
  "files": {
    "README.md": {
      "title": "📋 プロジェクト概要",
      "category": "基本情報"
    },
    "guide.md": {
      "title": "📖 ガイド",
      "category": "ドキュメント"
    },
    "manual.md": {
      "title": "📚 マニュアル",
      "category": "ドキュメント"
    }
  },
  
  "filename_replacements": {
    "README": "index",
    "guide": "guide",
    "manual": "manual"
  }
}
```

### ステップ3: サイト生成

```bash
# ライブラリインストール（初回のみ）
pip3 install -r requirements.txt

# サイト生成
python3 generate_universal.py
```

### ステップ4: GitHub Pagesで公開

```bash
# GitHubリポジトリを作成後
git clone https://github.com/username/repository-name.git
cd repository-name

# 生成されたファイルをコピー
cp -r site_output/* .

# コミット&プッシュ
git add .
git commit -m "Add generated site files"
git push

# GitHub → Settings → Pages で公開設定
```

## ⚙️ 設定ファイル詳細

### 基本設定

- `site_title`: サイトのタイトル
- `site_subtitle`: サブタイトル
- `source_folder`: Markdownファイルがあるフォルダパス
- `output_folder`: HTML出力先フォルダ
- `template_file`: 使用するHTMLテンプレート

### ファイル設定

- `include_files`: 表示したいMarkdownファイルのリスト
- `files`: 各ファイルの表示名とカテゴリ設定
- `filename_replacements`: ファイル名の置換ルール

### カテゴリについて

サイドバーは `category` で自動グループ化されます：

```json
"files": {
  "intro.md": {
    "title": "📖 はじめに",
    "category": "基本情報"
  },
  "advanced.md": {
    "title": "🚀 応用編",
    "category": "ガイド"
  }
}
```

## 🎨 テンプレートのカスタマイズ

### 色を変える

`_templates/page_light.html` の以下の部分を編集：

```css
:root {
  --bg-primary: #ffffff;     /* 背景色 */
  --text-primary: #212529;   /* 文字色 */
  --accent: #0066cc;         /* アクセント色 */
  --sidebar-bg: #f5f7f9;     /* サイドバー背景 */
}
```

### ロゴを追加

```html
<div class="sidebar-header">
  <img src="logo.png" alt="Logo" style="height: 40px; margin-bottom: 8px;">
  <h1>{{SITE_TITLE}}</h1>
  <p>{{SITE_SUBTITLE}}</p>
</div>
```

## 📋 プロジェクトパターン例

### パターン1: 企業ガイドライン

```json
{
  "site_title": "企業名",
  "site_subtitle": "社内ガイドライン",
  "include_files": [
    "README.md",
    "communication/guide.md",
    "design/styleguide.md",
    "workflow/process.md"
  ]
}
```

### パターン2: プロダクトドキュメント

```json
{
  "site_title": "プロダクト名",
  "site_subtitle": "Documentation",
  "include_files": [
    "README.md",
    "getting-started.md",
    "api/reference.md",
    "tutorials/basic.md"
  ]
}
```

### パターン3: 学習教材

```json
{
  "site_title": "コース名",
  "site_subtitle": "学習教材",
  "include_files": [
    "introduction.md",
    "lesson1.md",
    "lesson2.md",
    "exercises.md"
  ]
}
```

## 🔧 トラブルシューティング

### ファイルが見つからない

```
⚠️ ファイルが見つかりません: docs/guide.md
```

→ `source_folder` と `include_files` のパスを確認

### 文字化け

→ Markdownファイルが UTF-8 で保存されているか確認

### GitHub Pagesで表示されない

→ ファイルがリポジトリのルートにあるか確認
→ `index.html` ファイルが存在するか確認

## 🚀 自動化のヒント

### 定期実行（macOS）

```bash
# crontabで毎日自動生成
0 9 * * * cd /path/to/project && python3 generate_universal.py
```

### GitHub Actions（自動デプロイ）

`.github/workflows/deploy.yml` で自動化可能

## 📞 サポート

問題があれば、Harukazeチームまでお気軽にご連絡ください！

---

**このツールで、どんなプロジェクトでも美しいドキュメントサイトが作れます** 🎉