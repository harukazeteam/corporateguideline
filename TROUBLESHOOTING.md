# トラブルシューティングガイド

## 目次
1. [よくある問題と解決方法](#よくある問題と解決方法)
2. [サイト生成関連](#サイト生成関連)
3. [表示・UI関連](#表示ui関連)
4. [パフォーマンス関連](#パフォーマンス関連)
5. [GitHub Pages関連](#github-pages関連)
6. [開発環境関連](#開発環境関連)

## よくある問題と解決方法

### 🔴 緊急度：高

#### サイトが表示されない
```bash
# 原因1: サイトが生成されていない
cd site_generator
python3 generate_auto.py

# 原因2: GitHub Pagesが有効になっていない
# GitHub リポジトリ → Settings → Pages → Source を確認

# 原因3: URLが間違っている
# 正しいURL: https://harukazeteam.github.io/corporateguideline/site_output/
```

#### Pythonエラーで生成できない
```bash
# 必要なパッケージをインストール
pip install markdown PyYAML beautifulsoup4

# Python バージョンを確認（3.7以上必要）
python3 --version
```

### 🟡 緊急度：中

#### トグルが勝手に閉じる/開く
```javascript
// 問題: ページ遷移時にトグルがリセットされる
// 解決: LocalStorageが正しく動作しているか確認

// ブラウザのコンソールで確認
localStorage.getItem('category-基本情報')

// LocalStorageをクリア（リセット）
localStorage.clear()
```

#### 動画時間が表示されない
```yaml
# フロントマターの書き方を確認
---
title: ページタイトル
duration: 5分  # ✅ 正しい
duration: 5    # ✅ これも可（自動的に「分」が付く）
duration: "5"  # ✅ これも可
time: 5分      # ❌ フィールド名が違う
---
```

### 🟢 緊急度：低

#### アニメーションが遅い
```css
/* CSSの transition 値を確認 */
/* v2.0.0では 0.15s に統一されているはず */
transition: all 0.15s ease;  /* 正しい */
transition: all 0.3s ease;   /* 古いバージョン */
```

## サイト生成関連

### エラー: "Markdownファイルが見つかりませんでした"
```bash
# ディレクトリ構造を確認
ls -la ../サイトコンテンツ/

# Markdownファイルの拡張子を確認（.md である必要がある）
find ../サイトコンテンツ -name "*.md" | head -5
```

### エラー: UnicodeDecodeError
```python
# ファイルのエンコーディングを確認
file -I ../サイトコンテンツ/01_基本情報/*.md

# UTF-8に変換
iconv -f SHIFT_JIS -t UTF-8 input.md > output.md
```

### ファイル名の重複エラー
```bash
# 重複するファイル名を確認
find ../サイトコンテンツ -name "*.md" | xargs basename | sort | uniq -d

# 解決策: ファイル名に番号プレフィックスを追加
# 例: introduction.md → 01_introduction.md
```

## 表示・UI関連

### サイドバーが表示されない
```javascript
// コンソールでエラーを確認
console.log(document.querySelector('.sidebar'));

// CSSが正しく読み込まれているか確認
console.log(getComputedStyle(document.querySelector('.sidebar')).width);
```

### モバイルでレイアウトが崩れる
```html
<!-- viewportメタタグを確認 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- レスポンシブ対応のブレークポイントを確認 -->
<!-- 768px以下: モバイル -->
<!-- 769px-968px: タブレット -->
<!-- 969px以上: デスクトップ -->
```

### 検索が機能しない
```bash
# search-index.json が生成されているか確認
ls -la ../site_output/search-index.json

# 再生成
cd site_generator
python3 generate_auto.py
```

## パフォーマンス関連

### ページの読み込みが遅い
```bash
# 1. 画像サイズを最適化
# 大きな画像がないか確認
find ../site_output -name "*.png" -o -name "*.jpg" | xargs ls -lh

# 2. HTMLファイルのサイズを確認
ls -lh ../site_output/*.html | head -10
```

### アニメーションがカクつく
```css
/* GPU アクセラレーションを有効化 */
.category {
    will-change: transform;
    transform: translateZ(0);
}
```

## GitHub Pages関連

### デプロイされない
```bash
# 1. GitHub Actions の状態を確認
# https://github.com/harukazeteam/corporateguideline/actions

# 2. ブランチを確認（mainブランチである必要がある）
git branch
git checkout main

# 3. プッシュされているか確認
git status
git push origin main
```

### 404エラーが出る
```bash
# .nojekyll ファイルが存在するか確認
ls -la ../site_output/.nojekyll

# なければ作成
touch ../site_output/.nojekyll
git add ../site_output/.nojekyll
git commit -m "Add .nojekyll for GitHub Pages"
git push
```

## 開発環境関連

### Pythonのバージョンエラー
```bash
# Python 3.7以上が必要
python3 --version

# pyenvを使用してバージョンを管理
pyenv install 3.9.16
pyenv local 3.9.16
```

### パッケージの依存関係エラー
```bash
# 仮想環境を作成して解決
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# または
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### Gitの競合エラー
```bash
# 最新の変更を取得
git pull origin main

# 競合を解決
git status  # 競合ファイルを確認
# ファイルを編集して競合マーカーを削除

git add .
git commit -m "Resolve conflicts"
git push origin main
```

## デバッグ方法

### ブラウザコンソールでの確認
```javascript
// LocalStorage の内容を確認
Object.keys(localStorage).forEach(key => {
    if (key.includes('category') || key.includes('subcategory')) {
        console.log(key, localStorage.getItem(key));
    }
});

// 現在のトグル状態を確認
document.querySelectorAll('.category').forEach(cat => {
    console.log(cat.querySelector('.category-title').textContent, 
                cat.classList.contains('collapsed'));
});
```

### Python デバッグ
```python
# generate_auto.py にデバッグコードを追加
import pprint

# ページ情報を詳細表示
pprint.pprint(self.pages[:2])  # 最初の2ページを表示

# カテゴリ情報を確認
for page in self.pages:
    print(f"Category: {page['category']}, Subcategory: {page.get('subcategory')}")
```

## よくある質問（FAQ）

### Q: サイトを更新したのに変更が反映されない
**A:** ブラウザのキャッシュをクリアしてください。
- Chrome: `Cmd+Shift+R` (Mac) / `Ctrl+Shift+R` (Windows)
- Safari: `Cmd+Option+R`
- Firefox: `Cmd+Shift+R` (Mac) / `Ctrl+Shift+R` (Windows)

### Q: 新しいカテゴリを追加したい
**A:** `サイトコンテンツ/` に新しいフォルダを作成し、番号プレフィックスを付けてください。
```bash
mkdir "../サイトコンテンツ/04_新カテゴリ"
```

### Q: 動画時間の合計が正しくない
**A:** フロントマターの `duration` フィールドが統一されているか確認してください。
```bash
# すべての duration フィールドを確認
grep -r "duration:" ../サイトコンテンツ/
```

### Q: AIチャットが動作しない
**A:** Vercel APIのステータスを確認してください。
```javascript
// コンソールでテスト
fetch('https://guideline-ai-chat.vercel.app/api/chat-gemini', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: 'テスト' })
}).then(r => r.json()).then(console.log);
```

## サポート

問題が解決しない場合は、以下の情報を添えて報告してください：

1. **エラーメッセージ**（完全なスタックトレース）
2. **実行環境**
   - OS: Mac/Windows/Linux
   - Python バージョン
   - ブラウザとバージョン
3. **再現手順**
4. **期待される動作と実際の動作**

報告先: [GitHub Issues](https://github.com/harukazeteam/corporateguideline/issues)

---

**最終更新**: 2024年8月20日  
**バージョン**: 2.0.0  
**作成者**: Harukazeガイドライン開発チーム