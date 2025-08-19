# Harukazeコーポレートガイドライン

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/harukazeteam/corporateguideline)
[![License](https://img.shields.io/badge/license-Proprietary-red.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Production-success.svg)](https://harukazeteam.github.io/corporateguideline/site_output/)

## 📋 プロジェクト概要

Harukazeの法人事業向け品質管理ガイドラインの静的サイト生成システムです。ディレクター向けの業務マニュアル、コミュニケーションガイド、トラブルシューティング事例などを一元管理し、Webサイトとして公開しています。

**🌐 本番環境**: https://harukazeteam.github.io/corporateguideline/site_output/

## ✨ 主な機能

### コンテンツ管理
- 📝 **Markdownベース**: シンプルなMarkdownファイルでコンテンツ管理
- 🏷️ **フロントマター対応**: YAMLフォーマットでメタデータ管理
- 📁 **自動カテゴリ認識**: ディレクトリ構造から自動的にカテゴリを判定
- ⏱️ **動画時間表示**: 各コンテンツの動画時間を表示（v2.0.0新機能）

### ユーザーインターフェース
- 🎨 **レスポンシブデザイン**: PC、タブレット、モバイル対応
- 🔍 **全文検索**: リアルタイム検索とハイライト表示
- 💬 **AIチャット**: Gemini APIを活用した質問応答システム
- 📊 **階層ナビゲーション**: トグル可能なサイドバーメニュー

### パフォーマンス（v2.0.0改善）
- ⚡ **高速アニメーション**: 0.15秒のトランジション
- 💾 **状態保持**: LocalStorageでトグル状態を記憶
- 🎯 **即座ジャンプ**: スムーズスクロール無効化

## 🗂️ ディレクトリ構造

```
corporateguideline/
├── サイトコンテンツ/           # Markdownコンテンツ
│   ├── 01_基本情報/
│   │   ├── 01_はじめに/       # サブカテゴリ
│   │   ├── 02_ディレクターの心得/
│   │   └── ...
│   ├── 02_商談マニュアル/
│   └── 03_その他/
├── site_generator/             # サイト生成システム
│   ├── generate_auto.py       # メイン生成スクリプト
│   └── _templates/
│       └── page_light_with_ai.html
├── site_output/               # 生成されたHTMLファイル
├── CLAUDE.md                  # 開発者向け詳細ドキュメント
├── CHANGELOG.md               # 変更履歴
└── README.md                  # このファイル
```

## 🚀 クイックスタート

### 必要要件
- Python 3.7以上
- pip（Pythonパッケージマネージャー）

### セットアップ

```bash
# リポジトリのクローン
git clone https://github.com/harukazeteam/corporateguideline.git
cd corporateguideline

# 必要なパッケージのインストール
pip install -r requirements.txt
```

### サイト生成

```bash
# サイト生成ディレクトリに移動
cd site_generator

# サイトを生成
python3 generate_auto.py
```

### ローカルでの確認

```bash
# 簡易HTTPサーバーを起動
cd ../site_output
python3 -m http.server 8000

# ブラウザで開く
open http://localhost:8000
```

## 📝 コンテンツの追加・編集

### 新しいページの追加

1. `サイトコンテンツ/` ディレクトリに`.md`ファイルを作成
2. フロントマター（オプション）を追加：

```markdown
---
title: ページタイトル
category: 基本情報
subcategory: はじめに
order: 10
duration: 5分
---

# コンテンツ本文
```

3. サイトを再生成：

```bash
cd site_generator
python3 generate_auto.py
```

### 動画時間の追加

フロントマターに`duration`フィールドを追加するだけです：

```yaml
duration: 10分  # または duration: 10 でも可
```

## 🔧 開発者向け情報

詳細な技術仕様、カスタマイズ方法、トラブルシューティングについては、以下のドキュメントを参照してください：

- 📘 [CLAUDE.md](CLAUDE.md) - 開発者向け詳細ドキュメント
- 📝 [CHANGELOG.md](CHANGELOG.md) - 変更履歴
- 🔧 [TECHNICAL.md](TECHNICAL.md) - 技術仕様書（作成中）

## 🤝 コントリビューション

### バグ報告・機能要望

[Issues](https://github.com/harukazeteam/corporateguideline/issues)から報告してください。

### プルリクエスト

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/AmazingFeature`)
3. 変更をコミット (`git commit -m 'Add some AmazingFeature'`)
4. ブランチにプッシュ (`git push origin feature/AmazingFeature`)
5. プルリクエストを作成

## 📄 ライセンス

このプロジェクトはHarukaze Inc.の独占的所有物です。無断での複製、配布、改変は禁止されています。

## 📞 お問い合わせ

- **プロジェクト管理者**: Harukazeガイドラインチーム
- **GitHub**: https://github.com/harukazeteam/corporateguideline
- **本番サイト**: https://harukazeteam.github.io/corporateguideline/site_output/

---

**最終更新**: 2024年8月20日  
**バージョン**: 2.0.0  
**ステータス**: Production Ready 🚀