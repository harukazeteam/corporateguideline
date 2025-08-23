#!/usr/bin/env python3
"""
改良版自動検出型サイト生成ツール
- 動画時間表示対応
- サブカテゴリの正しいソート
- ナビゲーション改善
"""

import os
import shutil
import markdown
from pathlib import Path
import re
import json
import yaml
from datetime import datetime
from bs4 import BeautifulSoup

class ImprovedSiteGenerator:
    def __init__(self, content_dir="../サイトコンテンツ", 
                 output_dir="../site_output",
                 template_dir="_templates"):
        self.content_dir = Path(content_dir)
        self.output_dir = Path(output_dir)
        self.template_dir = Path(template_dir)
        self.pages = []
        self.navigation_map = {}  # ナビゲーション用のマップ
        
    def extract_frontmatter(self, content):
        """Markdownファイルからフロントマターを抽出"""
        if content.startswith('---\n'):
            try:
                parts = content.split('---\n', 2)
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    markdown_content = parts[2]
                    return frontmatter, markdown_content
            except:
                pass
        return {}, content
    
    def scan_markdown_files(self):
        """Markdownファイルを自動検出してページ情報を収集"""
        self.pages = []
        
        # アーカイブフォルダは除外
        exclude_dirs = ['アーカイブ', 'archive', 'Archive', '_archive']
        
        # ディレクトリ構造を走査
        for md_file in self.content_dir.rglob('*.md'):
            # アーカイブフォルダ内のファイルはスキップ
            if any(exclude_dir in md_file.parts for exclude_dir in exclude_dirs):
                continue
            # index.mdはスキップ
            if md_file.name == 'index.md':
                continue
                
            # 相対パスを取得
            relative_path = md_file.relative_to(self.content_dir)
            
            # ファイル内容を読み込み
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # フロントマターを抽出
            frontmatter, markdown_content = self.extract_frontmatter(content)
            
            # ページ情報を構築
            page_info = {
                'source': str(md_file),
                'content': markdown_content,
                'filename': md_file.name,
                'relative_path': str(relative_path),
            }
            
            # フロントマターから情報を取得（なければ自動生成）
            if frontmatter:
                page_info['title'] = frontmatter.get('title', self.clean_filename(md_file.stem))
                page_info['category'] = frontmatter.get('category', self.guess_category(relative_path)) or ''
                page_info['subcategory'] = frontmatter.get('subcategory', self.guess_subcategory(relative_path))
                order_value = frontmatter.get('order', self.extract_order(md_file.name))
                page_info['order'] = order_value if order_value is not None else 999
                page_info['date'] = frontmatter.get('date', None)
                page_info['tags'] = frontmatter.get('tags', [])
                # 動画時間を取得して形式を統一
                duration = frontmatter.get('duration', None)
                if duration:
                    # 数字のみの場合は「分」を追加
                    if isinstance(duration, (int, float)):
                        page_info['duration'] = f"{duration}分"
                    elif isinstance(duration, str) and duration.isdigit():
                        page_info['duration'] = f"{duration}分"
                    else:
                        page_info['duration'] = duration
                else:
                    page_info['duration'] = None
            else:
                # フロントマターがない場合は自動推測
                # 最初のH1タグからタイトルを取得
                h1_match = re.search(r'^#\s+(.+)$', markdown_content, re.MULTILINE)
                if h1_match:
                    page_info['title'] = h1_match.group(1).strip()
                else:
                    page_info['title'] = self.clean_filename(md_file.stem)
                page_info['category'] = self.guess_category(relative_path) or ''
                page_info['subcategory'] = self.guess_subcategory(relative_path)
                page_info['order'] = self.extract_order(md_file.name)
                page_info['date'] = None
                page_info['tags'] = []
                page_info['duration'] = None
            
            # 出力ファイル名を生成
            page_info['output_name'] = self.safe_filename(md_file.stem, md_file.name) + '.html'
            
            self.pages.append(page_info)
        
        # 重複するファイル名を解決
        self._resolve_duplicate_filenames()
        
        # ページをソート（カテゴリ → サブカテゴリ → 順序）
        self.pages.sort(key=lambda x: (
            self.category_sort_order(x['category']),
            self.subcategory_sort_order(x['subcategory']) if x['subcategory'] else 999,
            x['order'],
            x['filename']
        ))
        
        # ナビゲーションマップを構築
        self.build_navigation_map()
        
        print(f"検出されたMarkdownファイル: {len(self.pages)}件")
    
    def category_sort_order(self, category):
        """カテゴリのソート順序を定義"""
        order = {
            "最初にみる動画": 1,
            "商談マニュアル": 2,
            "その他": 3,
        }
        return order.get(category, 999)
    
    def subcategory_sort_order(self, subcategory):
        """サブカテゴリ名から順序を抽出"""
        if not subcategory:
            return 999
        # サブカテゴリ名の最初の数字を抽出（例: "01_はじめに" → 1）
        match = re.match(r'^(\d+)', subcategory)
        if match:
            return int(match.group(1))
        return 999
    
    def guess_category(self, relative_path):
        """相対パスからカテゴリを推測"""
        parts = relative_path.parts
        if len(parts) > 0:
            # トップレベルのディレクトリ名をカテゴリとする
            category = parts[0]
            # 数字プレフィックスを削除
            category = re.sub(r'^\d+[_-]', '', category)
            return category
        return None
    
    def guess_subcategory(self, relative_path):
        """相対パスからサブカテゴリを推測"""
        parts = relative_path.parts
        if len(parts) > 1:
            # 2階層目のディレクトリ名をサブカテゴリとする
            subcategory = parts[1] if len(parts) > 2 else None
            if subcategory:
                # 数字プレフィックスは残しておく（ソート用）
                return subcategory
            return subcategory
        return None
    
    def extract_order(self, filename):
        """ファイル名から順序を抽出（例: 01_xxx.md → 1）"""
        if not filename:
            return 999
        match = re.match(r'^(\d+)', filename)
        if match:
            return int(match.group(1))
        return 999
    
    def clean_filename(self, name):
        """ファイル名をタイトル用に整形"""
        # 01_、02_などの単純な番号プレフィックスのみ削除（1-1.などは保持）
        name = re.sub(r'^0?\d+_', '', name)
        # アンダースコアやハイフンをスペースに（ただし数字-数字.パターンは保持）
        # 1-1.パターンを保護しながら、その他の_や-をスペースに変換
        if not re.match(r'^\d+-\d+\.', name):
            name = re.sub(r'[_-]', ' ', name)
        return name
    
    def safe_filename(self, name, original_filename=''):
        """ファイル名を安全なHTML名に変換（日本語対応）"""
        # 数字プレフィックスを削除
        name = re.sub(r'^\d+[_-]', '', name)
        
        # 日本語ファイル名の変換テーブル
        replacements = {
            'guideline_why': 'guideline_why',
            'vision': 'vision',
            'はじめに': 'introduction',
            'ディレクターの心得': 'director_mindset',
            '全体の業務プロセス': 'business_process',
            'コミュニケーションガイド': 'communication_guide',
            '代表的なトラブルシューティング': 'troubleshooting',
            'ガイドライン要点まとめ': 'guideline_summary',
            '実践改善事例集': 'improvement_cases',
            '新機能の使い方': 'new_features',
            'よくある質問FAQ': 'faq',
            'プロジェクト管理のコツ': 'project_management_tips',
            'AIチャット': 'ai-assistant',
            'ガイドライン追加・改善': 'feedback'
        }
        
        # 変換テーブルで一致するものがあれば使用
        for jp, en in replacements.items():
            if jp in name:
                return en
        
        # 一致しない場合は安全な形式に変換
        # 日本語が含まれている場合は簡単な変換を試みる
        if re.search(r'[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf]', name):
            # ファイル名に番号があれば利用
            match = re.match(r'^(\d+)', original_filename)
            if match:
                # カテゴリとサブカテゴリを含めてより詳細な名前を生成
                category_match = re.search(r'/(\d+)_[^/]+/', original_filename)
                if category_match:
                    return f'page_{category_match.group(1)}_{match.group(1)}'
                return f'page_{match.group(1)}'
            else:
                # 番号がなければ連番を付与
                return f'page_{len(self.pages) + 1}'
        
        # 英数字のみの場合
        safe_name = re.sub(r'[^\w\s-]', '', name)
        safe_name = re.sub(r'\s+', '_', safe_name).lower()
        
        return safe_name if safe_name else 'untitled'
    
    def _resolve_duplicate_filenames(self):
        """重複するファイル名を解決"""
        filename_counts = {}
        
        # 重複をカウント
        for page in self.pages:
            output_name = page['output_name']
            if output_name in filename_counts:
                filename_counts[output_name] += 1
            else:
                filename_counts[output_name] = 1
        
        # 重複があるファイルに番号を付与
        filename_counters = {}
        for page in self.pages:
            output_name = page['output_name']
            if filename_counts[output_name] > 1:
                if output_name not in filename_counters:
                    filename_counters[output_name] = 1
                else:
                    filename_counters[output_name] += 1
                
                # ファイル名に番号を追加
                base_name = output_name.replace('.html', '')
                page['output_name'] = f"{base_name}_{filename_counters[output_name]}.html"
    
    def calculate_total_duration(self, pages):
        """ページリストの合計時間を計算"""
        total_minutes = 0
        for page in pages:
            if page.get('duration'):
                duration = page['duration']
                # 「分」を削除して数値を抽出
                if isinstance(duration, str):
                    match = re.search(r'(\d+)', duration)
                    if match:
                        total_minutes += int(match.group(1))
        
        if total_minutes > 0:
            if total_minutes >= 60:
                hours = total_minutes // 60
                minutes = total_minutes % 60
                if minutes > 0:
                    return f"{hours}時間{minutes}分"
                else:
                    return f"{hours}時間"
            else:
                return f"{total_minutes}分"
        return None
    
    def build_navigation_map(self):
        """ナビゲーションマップを構築（すべてのカテゴリを跨いだナビゲーション）"""
        self.navigation_map = {}
        
        # すべてのページを順番に処理（カテゴリ・サブカテゴリを跨いで）
        all_pages = self.pages  # すでにソート済み
        
        for i, page in enumerate(all_pages):
            nav = {}
            
            # 前のページ
            if i > 0:
                prev_page = all_pages[i - 1]
                nav['prev'] = {
                    'title': prev_page['title'],
                    'url': prev_page['output_name']
                }
            
            # 次のページ
            if i < len(all_pages) - 1:
                next_page = all_pages[i + 1]
                nav['next'] = {
                    'title': next_page['title'],
                    'url': next_page['output_name']
                }
            
            self.navigation_map[page['output_name']] = nav
    
    def generate_sidebar(self):
        """ページ情報からサイドバーHTMLを生成（動画時間付き）"""
        categories = {}
        
        # カテゴリごとにページを分類（サブカテゴリも考慮）
        for page in self.pages:
            category = page['category']
            if category not in categories:
                categories[category] = {'pages': [], 'subcategories': {}}
            
            # サブカテゴリがある場合
            if page.get('subcategory'):
                subcategory = page['subcategory']
                if subcategory not in categories[category]['subcategories']:
                    categories[category]['subcategories'][subcategory] = []
                categories[category]['subcategories'][subcategory].append(page)
            else:
                categories[category]['pages'].append(page)
        
        # サイドバーHTML生成
        sidebar_html = '''<!-- モバイル用サイドバーヘッダー -->
<div class="mobile-sidebar-header" style="display: none;">
    <button class="sidebar-close-btn" id="sidebarCloseBtn">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M6 18L18 6M6 6l12 12"></path>
        </svg>
    </button>
    <span style="flex: 1; font-size: 18px; font-weight: 600;">メニュー</span>
</div>
<!-- モバイル用検索 -->
<div class="mobile-sidebar-search" style="display: none;">
    <input type="text" placeholder="ページを検索..." id="mobileSidebarSearch">
</div>
<!-- 通常のサイドバーヘッダー -->
<div class="sidebar-header desktop-only">
<a href="index.html" style="text-decoration: none; color: inherit;">
<h1>Harukazeガイドライン</h1>
</a>
<p>法人事業 品質管理マニュアル</p>
</div>
<nav class="sidebar-nav">
<a href="index.html" class="nav-item"><span class="nav-item-text">ホーム</span></a>
<div class="nav-divider"></div>'''
        
        # カテゴリの表示順序を定義
        category_order = ["最初にみる動画", "商談マニュアル", "その他"]
        
        # 定義された順序でカテゴリを表示
        for category in category_order:
            if category not in categories:
                continue
            
            cat_data = categories[category]
            
            # カテゴリのdivを作成（デフォルトで閉じる）
            sidebar_html += f'<div class="category collapsed">\n'
            sidebar_html += f'  <div class="category-title">{category}</div>\n'
            sidebar_html += f'  <div class="category-content">\n'
            
            # サブカテゴリを順序付きで表示
            if cat_data['subcategories']:
                # サブカテゴリをソート（番号を考慮）
                sorted_subcategories = sorted(cat_data['subcategories'].items(), 
                                             key=lambda x: self.subcategory_sort_order(x[0]))
                
                for subcategory, pages in sorted_subcategories:
                    # サブカテゴリ名から番号プレフィックスを削除して表示
                    display_name = re.sub(r'^\d+[_-]', '', subcategory)
                    
                    # サブカテゴリ内の合計時間を計算
                    total_duration = self.calculate_total_duration(pages)
                    duration_html = ''
                    if total_duration:
                        duration_html = f'<span class="duration-badge">{total_duration}</span>'
                    
                    sidebar_html += f'    <div class="subcategory-folder collapsed">\n'
                    sidebar_html += f'      <div class="subcategory-folder-title"><span class="nav-item-text">{display_name}</span>{duration_html}</div>\n'
                    sidebar_html += f'      <div class="subcategory-folder-content">\n'
                    
                    # ページをソート（orderを考慮）
                    sorted_pages = sorted(pages, key=lambda x: (x['order'], x['filename']))
                    for page in sorted_pages:
                        # 動画時間があれば表示
                        if page.get('duration'):
                            sidebar_html += f'        <a href="{page["output_name"]}" class="nav-item"><span class="nav-item-text">{page["title"]}</span><span class="duration-badge">{page["duration"]}</span></a>\n'
                        else:
                            sidebar_html += f'        <a href="{page["output_name"]}" class="nav-item"><span class="nav-item-text">{page["title"]}</span></a>\n'
                    
                    sidebar_html += f'      </div>\n'
                    sidebar_html += f'    </div>\n'
            
            # サブカテゴリに属さないページ
            if cat_data['pages']:
                sorted_pages = sorted(cat_data['pages'], key=lambda x: (x['order'], x['filename']))
                for page in sorted_pages:
                    # 動画時間があれば表示
                    if page.get('duration'):
                        sidebar_html += f'    <a href="{page["output_name"]}" class="nav-item"><span class="nav-item-text">{page["title"]}</span><span class="duration-badge">{page["duration"]}</span></a>\n'
                    else:
                        sidebar_html += f'    <a href="{page["output_name"]}" class="nav-item"><span class="nav-item-text">{page["title"]}</span></a>\n'
            
            sidebar_html += f'  </div>\n'
            sidebar_html += f'</div>\n'
        
        # 未分類のカテゴリも表示
        for category in categories:
            if category not in category_order and category:
                cat_data = categories[category]
                
                sidebar_html += f'<div class="category collapsed">\n'
                sidebar_html += f'  <div class="category-title">{category}</div>\n'
                sidebar_html += f'  <div class="category-content">\n'
                
                # ページをソート
                sorted_pages = sorted(cat_data['pages'], key=lambda x: (x['order'], x['filename']))
                for page in sorted_pages:
                    # 動画時間があれば表示
                    if page.get('duration'):
                        sidebar_html += f'    <a href="{page["output_name"]}" class="nav-item"><span class="nav-item-text">{page["title"]}</span><span class="duration-badge">{page["duration"]}</span></a>\n'
                    else:
                        sidebar_html += f'    <a href="{page["output_name"]}" class="nav-item"><span class="nav-item-text">{page["title"]}</span></a>\n'
                
                sidebar_html += f'  </div>\n'
                sidebar_html += f'</div>\n'
        
        sidebar_html += '</nav>\n'
        
        # サイドバーフッター（よくある質問FAQは削除）
        sidebar_html += '''<div class="sidebar-footer">
    <button class="footer-link" onclick="toggleAiPanel()">AIチャット</button>
    <div class="footer-divider"></div>
    <a href="feedback.html" class="footer-link">ガイドライン追加・改善</a>
</div>'''
        
        return sidebar_html
    
    def generate_pages(self):
        """各ページのHTMLを生成"""
        # テンプレートを読み込み
        template_path = self.template_dir / "page_light_with_ai.html"
        
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        
        # サイドバーHTMLを生成
        sidebar_html = self.generate_sidebar()
        
        # 出力ディレクトリを作成
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 各ページを生成
        for page in self.pages:
            # Markdownをパース
            md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
            html_content = md.convert(page['content'])
            
            # ナビゲーションボタンのHTML作成（すべてのページに）
            nav_html = ''
            if page['output_name'] in self.navigation_map:
                nav = self.navigation_map[page['output_name']]
                nav_html = '''<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 30px; margin-bottom: 30px; gap: 20px;">
'''
                
                if 'prev' in nav:
                    nav_html += f'''  <a href="{nav["prev"]["url"]}" style="
                        display: inline-flex;
                        align-items: center;
                        padding: 10px 20px;
                        background: white;
                        color: #0066cc;
                        text-decoration: none;
                        border: 2px solid #0066cc;
                        border-radius: 6px;
                        font-weight: 500;
                        font-size: 14px;
                        transition: all 0.2s;
                    " onmouseover="this.style.backgroundColor='#0066cc'; this.style.color='white';" 
                       onmouseout="this.style.backgroundColor='white'; this.style.color='#0066cc';">
                        ← 前へ
                    </a>
'''
                else:
                    nav_html += '  <span></span>\n'
                
                if 'next' in nav:
                    nav_html += f'''  <a href="{nav["next"]["url"]}" style="
                        display: inline-flex;
                        align-items: center;
                        padding: 10px 20px;
                        background: white;
                        color: #0066cc;
                        text-decoration: none;
                        border: 2px solid #0066cc;
                        border-radius: 6px;
                        font-weight: 500;
                        font-size: 14px;
                        transition: all 0.2s;
                        margin-left: auto;
                    " onmouseover="this.style.backgroundColor='#0066cc'; this.style.color='white';" 
                       onmouseout="this.style.backgroundColor='white'; this.style.color='#0066cc';">
                        次へ →
                    </a>
'''
                else:
                    nav_html += '  <span></span>\n'
                
                nav_html += '</div>\n'
            
            # iframe タグの後にナビゲーションボタンを挿入
            # BeautifulSoupを使ってHTMLを解析
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # iframe要素を探す（Loom動画）
            iframe = soup.find('iframe')
            if iframe:
                # iframeの親要素（divタグ）を探す
                iframe_parent = iframe.parent
                if iframe_parent and iframe_parent.name == 'div':
                    # ナビゲーションボタンのHTMLを解析
                    nav_soup = BeautifulSoup(nav_html, 'html.parser')
                    # iframe親要素の直後にナビゲーションを挿入
                    iframe_parent.insert_after(nav_soup)
                    html_content = str(soup)
                else:
                    # iframeの親がdivでない場合は、コンテンツの最後に追加
                    html_content = html_content + nav_html
            else:
                # iframeがない場合は、コンテンツの最後に追加
                html_content = html_content + nav_html
            
            # テンプレートに値を挿入
            page_html = template
            page_html = page_html.replace('{{TITLE}}', page['title'])
            page_html = page_html.replace('{{CONTENT}}', html_content)
            page_html = page_html.replace('{{SIDEBAR}}', sidebar_html)
            
            # ファイルを保存
            output_path = self.output_dir / page['output_name']
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(page_html)
            
            print(f"生成: {page['output_name']} <- {page['filename']}")
    
    def generate_index(self):
        """インデックスページを生成"""
        index_content = '''
# Harukazeガイドライン

## toB事業 品質管理マニュアル

このガイドラインは、Harukazeのパートナーディレクターの方々、そしてこれから法人事業で関わってくださるパートナーの方々に向けて作成されました。

日々の活動において、どういう基準で判断し、どういう考え方を持ち、どういうスタンスで取り組んでいけばよいのか。これらを共有させていただくのが、このガイドラインの目的です。

### 🎬 最初にみる動画
Harukazeの理念、ディレクターの心得、業務プロセスなど、まず押さえておくべき基本的な内容を動画で学べます。

### 💼 商談マニュアル
法人商談における実践的なテクニックや、信頼関係構築の方法をステップバイステップで解説しています。

### 💬 AIチャット機能
わからないことがあれば、AIアシスタントにすぐに質問できます。サイドバー下部の「AIチャット」をクリックしてください。

### 📝 フィードバック
ガイドラインの改善や追加のご要望は、サイドバー下部の「ガイドライン追加・改善」からお寄せください。

---

**このガイドラインは常に進化しています。**  
より良いものにしていくために、皆様のフィードバックをお待ちしています。
'''
        
        # テンプレートを読み込み
        template_path = self.template_dir / "page_light_with_ai.html"
        
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        
        # サイドバーHTMLを生成
        sidebar_html = self.generate_sidebar()
        
        # Markdownをパース
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
        html_content = md.convert(index_content)
        
        # テンプレートに値を挿入
        page_html = template
        page_html = page_html.replace('{{TITLE}}', 'Harukazeガイドライン')
        page_html = page_html.replace('{{CONTENT}}', html_content)
        page_html = page_html.replace('{{SIDEBAR}}', sidebar_html)
        
        # ファイルを保存
        output_path = self.output_dir / 'index.html'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page_html)
        
        print(f"生成: index.html")
    
    def generate_search_index(self):
        """検索用のインデックスファイルを生成"""
        search_index = []
        
        for page in self.pages:
            # HTMLタグを除去してプレーンテキストを取得
            md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
            html_content = md.convert(page['content'])
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 全セクションを取得
            for section in soup.find_all(['h1', 'h2', 'h3']):
                section_title = section.get_text()
                section_id = section.get('id', '')
                
                # セクションの後続コンテンツを取得
                content_parts = []
                for sibling in section.find_next_siblings():
                    if sibling.name in ['h1', 'h2', 'h3']:
                        break
                    content_parts.append(sibling.get_text())
                
                content_text = ' '.join(content_parts)[:500]
                
                # 検索インデックスエントリを作成
                entry = {
                    'pageTitle': page['title'],
                    'sectionTitle': section_title,
                    'sectionId': section_id,
                    'url': page['output_name'],
                    'content': content_text,
                    'category': page['category']
                }
                search_index.append(entry)
        
        # JSONファイルとして保存
        output_path = self.output_dir / 'search-index.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(search_index, f, ensure_ascii=False, indent=2)
        
        print(f"検索インデックスを生成: search-index.json")
    
    def run(self):
        """サイト生成の実行"""
        print("=" * 50)
        print("改良版サイト生成を開始")
        print("=" * 50)
        
        # Markdownファイルをスキャン
        self.scan_markdown_files()
        
        if not self.pages:
            print("警告: Markdownファイルが見つかりませんでした")
            return
        
        # ページを生成
        self.generate_pages()
        
        # インデックスページを生成
        self.generate_index()
        
        # 検索インデックスを生成
        self.generate_search_index()
        
        print("=" * 50)
        print(f"サイト生成完了: {self.output_dir}")
        print("=" * 50)

if __name__ == "__main__":
    generator = ImprovedSiteGenerator()
    generator.run()