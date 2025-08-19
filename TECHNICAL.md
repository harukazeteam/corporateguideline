# 技術仕様書 - Harukazeコーポレートガイドライン

## 目次
1. [アーキテクチャ概要](#アーキテクチャ概要)
2. [システム要件](#システム要件)
3. [コア機能の実装詳細](#コア機能の実装詳細)
4. [データフロー](#データフロー)
5. [パフォーマンス最適化](#パフォーマンス最適化)
6. [セキュリティ](#セキュリティ)
7. [API仕様](#api仕様)

## アーキテクチャ概要

### システム構成
```
┌─────────────────┐     ┌──────────────┐     ┌─────────────┐
│  Markdownファイル │ --> │ Python生成器  │ --> │ 静的HTML    │
└─────────────────┘     └──────────────┘     └─────────────┘
                               │                      │
                               ▼                      ▼
                        ┌──────────────┐     ┌─────────────┐
                        │ YAMLメタデータ│     │ GitHub Pages│
                        └──────────────┘     └─────────────┘
```

### 技術スタック
- **バックエンド**: Python 3.7+
- **静的サイト生成**: カスタムPythonスクリプト
- **フロントエンド**: HTML5, CSS3, Vanilla JavaScript
- **ホスティング**: GitHub Pages
- **CI/CD**: GitHub Actions
- **外部API**: Vercel AI API (Gemini)

## システム要件

### 開発環境
```yaml
Python: 3.7以上
pip: 最新版推奨
必須パッケージ:
  - markdown: 3.4+
  - PyYAML: 6.0+
  - beautifulsoup4: 4.11+
  - pathlib: (標準ライブラリ)
```

### ブラウザサポート
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- モバイルブラウザ（iOS Safari, Chrome Mobile）

## コア機能の実装詳細

### 1. サイト生成エンジン（generate_auto.py）

#### クラス構造
```python
class ImprovedSiteGenerator:
    def __init__(self, content_dir, output_dir, template_dir)
    def extract_frontmatter(self, content)
    def scan_markdown_files(self)
    def category_sort_order(self, category)
    def subcategory_sort_order(self, subcategory)
    def guess_category(self, relative_path)
    def guess_subcategory(self, relative_path)
    def extract_order(self, filename)
    def clean_filename(self, name)
    def safe_filename(self, name, original_filename)
    def _resolve_duplicate_filenames(self)
    def calculate_total_duration(self, pages)  # v2.0.0新機能
    def build_navigation_map(self)
    def generate_sidebar(self)
    def generate_pages(self)
    def generate_index(self)
    def generate_search_index(self)
    def run(self)
```

#### フロントマター処理
```python
def extract_frontmatter(self, content):
    if content.startswith('---\n'):
        parts = content.split('---\n', 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])
            markdown_content = parts[2]
            return frontmatter, markdown_content
    return {}, content
```

### 2. トグル状態管理（v2.0.0改善）

#### LocalStorage構造
```javascript
localStorage: {
    'category-基本情報': 'false',      // 開いている
    'category-商談マニュアル': 'true',  // 閉じている
    'subcategory-はじめに': 'false',   // 開いている
    'subcategory-ディレクターの心得': 'true'  // 閉じている
}
```

#### 状態管理ロジック
```javascript
function initializeToggleCategories() {
    document.querySelectorAll('.category').forEach(category => {
        const categoryName = title.textContent.trim();
        const savedState = localStorage.getItem(`category-${categoryName}`);
        
        if (savedState === 'false') {
            category.classList.remove('collapsed');
        } else {
            category.classList.add('collapsed');
        }
        
        title.addEventListener('click', (e) => {
            category.classList.toggle('collapsed');
            const isCollapsed = category.classList.contains('collapsed');
            localStorage.setItem(`category-${categoryName}`, isCollapsed);
        });
    });
}
```

### 3. 動画時間計算（v2.0.0新機能）

#### 時間フォーマット処理
```python
def calculate_total_duration(self, pages):
    total_minutes = 0
    for page in pages:
        if page.get('duration'):
            duration = page['duration']
            if isinstance(duration, str):
                match = re.search(r'(\d+)', duration)
                if match:
                    total_minutes += int(match.group(1))
    
    if total_minutes >= 60:
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"{hours}時間{minutes}分" if minutes > 0 else f"{hours}時間"
    return f"{total_minutes}分" if total_minutes > 0 else None
```

### 4. レスポンシブレイアウト

#### ブレークポイント
```css
/* デスクトップ */
@media (min-width: 969px) {
    .sidebar { width: 280px; }
    .main-content { margin-left: 280px; }
}

/* タブレット */
@media (max-width: 968px) and (min-width: 769px) {
    .sidebar { width: 240px; }
    .main-content { margin-left: 240px; }
}

/* モバイル */
@media (max-width: 768px) {
    .sidebar { 
        position: fixed;
        width: 100%;
        transform: translateX(-100%);
    }
    .sidebar.active { transform: translateX(0); }
}
```

## データフロー

### コンテンツ処理フロー
```
1. Markdownファイル読み込み
   ├── フロントマター抽出
   ├── カテゴリ/サブカテゴリ判定
   └── 順序番号抽出

2. メタデータ処理
   ├── タイトル生成
   ├── 動画時間フォーマット
   └── ファイル名正規化

3. HTML生成
   ├── Markdown→HTML変換
   ├── テンプレート適用
   └── サイドバー生成

4. 検索インデックス生成
   ├── HTMLタグ除去
   ├── セクション分割
   └── JSON出力
```

## パフォーマンス最適化

### v2.0.0での改善点

#### 1. アニメーション高速化
```css
/* 変更前 */
transition: all 0.3s ease;

/* 変更後 */
transition: all 0.15s ease;
```

#### 2. レイアウト最適化
```css
.nav-item {
    display: flex;  /* Flexbox採用 */
    align-items: center;
}

.nav-item-text {
    flex: 1;  /* 可変幅 */
    overflow: hidden;
    text-overflow: ellipsis;
}

.duration-badge {
    margin-left: auto;  /* 右端固定 */
    flex-shrink: 0;  /* 幅固定 */
}
```

#### 3. スクロール最適化
```javascript
// スムーズスクロール無効化
targetElement.scrollIntoView({
    behavior: 'auto',  // 'smooth' → 'auto'
    block: 'start'
});
```

### パフォーマンス指標
- **初回読み込み**: < 2秒（3G環境）
- **インタラクション応答**: < 100ms
- **アニメーション**: 60fps維持

## セキュリティ

### XSS対策
```python
# HTMLエスケープ処理
from html import escape
safe_title = escape(page['title'])
```

### CSP（Content Security Policy）
```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               script-src 'self' 'unsafe-inline' https://vercel.app; 
               style-src 'self' 'unsafe-inline';">
```

### 機密情報の管理
- APIキーは環境変数で管理
- フロントエンドには機密情報を含めない
- GitHubリポジトリはプライベート設定

## API仕様

### Vercel AI API

#### エンドポイント
```
POST https://guideline-ai-chat.vercel.app/api/chat-gemini
```

#### リクエスト
```json
{
    "message": "ユーザーの質問"
}
```

#### レスポンス
```json
{
    "response": "AIの回答",
    "relatedPages": [
        {
            "title": "関連ページタイトル",
            "url": "page.html",
            "category": "カテゴリ名"
        }
    ]
}
```

### 検索インデックスAPI

#### ファイル形式
```json
[
    {
        "pageTitle": "ページタイトル",
        "sectionTitle": "セクションタイトル",
        "sectionId": "section-id",
        "url": "page.html",
        "content": "コンテンツの抜粋...",
        "category": "カテゴリ名"
    }
]
```

## トラブルシューティング

### よくある問題と解決方法

#### 1. サイト生成エラー
```bash
# エラー: ModuleNotFoundError
pip install -r requirements.txt

# エラー: UnicodeDecodeError
# ファイルエンコーディングをUTF-8に統一
```

#### 2. トグル状態が保存されない
```javascript
// LocalStorageが無効化されていないか確認
console.log(localStorage.getItem('category-基本情報'));
```

#### 3. 動画時間が表示されない
```yaml
# フロントマターの形式を確認
duration: 5分  # 正しい
duration: "5分"  # これも正しい
duration: 5  # 自動的に「5分」に変換
```

## 今後の技術的課題

### 短期（〜2024年Q3）
- [ ] Service Worker実装（オフライン対応）
- [ ] WebP画像形式対応
- [ ] Lighthouse スコア100点達成

### 中期（〜2024年Q4）
- [ ] TypeScript移行
- [ ] React/Vue.js導入検討
- [ ] GraphQL API実装

### 長期（2025年〜）
- [ ] WebAssembly活用
- [ ] PWA完全対応
- [ ] リアルタイム同期機能

---

**最終更新**: 2024年8月20日  
**バージョン**: 2.0.0  
**作成者**: Harukazeガイドライン開発チーム