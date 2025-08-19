#!/usr/bin/env python3
"""
自動検出型サイト生成ツール
Markdownファイルを追加するだけで自動的にサイトに反映される
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

class AutoSiteGenerator:
    def __init__(self, content_dir="../サイトコンテンツ", 
                 output_dir="../site_output",
                 template_dir="_templates"):
        self.content_dir = Path(content_dir)
        self.output_dir = Path(output_dir)
        self.template_dir = Path(template_dir)
        self.pages = []
        
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
            
            # 出力ファイル名を生成
            page_info['output_name'] = self.safe_filename(md_file.stem, md_file.name) + '.html'
            
            self.pages.append(page_info)
        
        # 重複するファイル名を解決
        self._resolve_duplicate_filenames()
        
        # None値をデフォルト値に置き換え
        for page in self.pages:
            if page.get('category') is None:
                page['category'] = ''
            if page.get('subcategory') is None:
                page['subcategory'] = ''
            if page.get('order') is None:
                page['order'] = 999
            if page.get('filename') is None:
                page['filename'] = ''
        
        # ソート（カテゴリ → サブカテゴリ → order → ファイル名）
        self.pages.sort(key=lambda x: (
            x.get('category', ''),
            x.get('subcategory', ''),
            x.get('order', 999),
            x.get('filename', '')
        ))
    
    def guess_category(self, relative_path):
        """ディレクトリ構造からカテゴリを推測"""
        parts = relative_path.parts
        if len(parts) > 1:
            # サブディレクトリ名をカテゴリとして使用
            category = parts[0]
            # カテゴリ名の正規化（番号プレフィックスを除去）
            category = re.sub(r'^\d+[_-]', '', category)
            
            if category == "基本情報":
                return "基本情報"
            elif category == "商談マニュアル":
                return "商談マニュアル"
            elif category == "その他":
                return "その他"
            elif category == "loomの動画":
                return "Loom動画"
            else:
                return category
        # ルートディレクトリのファイルは「基本情報」に分類
        return "基本情報"
    
    def guess_subcategory(self, relative_path):
        """ディレクトリ構造からサブカテゴリを推測"""
        parts = relative_path.parts
        if len(parts) > 2:
            # 2階層目がサブカテゴリ
            subcategory = parts[1]
            # 番号プレフィックスを除去
            subcategory = re.sub(r'^\d+[_-]', '', subcategory)
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
        # 数字プレフィックスを削除
        name = re.sub(r'^\d+[_-]', '', name)
        # アンダースコアやハイフンをスペースに
        name = re.sub(r'[_-]', ' ', name)
        # 単語の先頭を大文字に
        return name.title()
    
    def safe_filename(self, name, original_filename=''):
        """ファイル名を安全なHTML名に変換（日本語対応）"""
        # 数字プレフィックスを削除
        name = re.sub(r'^\d+[_-]', '', name)
        
        # 日本語ファイル名の変換テーブル
        replacements = {
            'はじめに': 'introduction',
            'ディレクターの心得': 'director_mindset',
            '全体の業務プロセス': 'business_process',
            'コミュニケーションガイド': 'communication_guide',
            '代表的なトラブルシューティング': 'troubleshooting',
            'ガイドライン要点まとめ': 'guideline_summary',
            '実践改善事例集': 'improvement_cases',
            '新機能の使い方': 'new_features',
            '新規コンテンツの追加方法': 'new_features',
            'よくある質問FAQ': 'faq',
            'よくある質問（FAQ）': 'faq',
            'プロジェクト管理のコツ': 'project_management_tips',
            'loomリンク集': 'loom_links',
            '文字起こし': 'transcript',
            'AIチャット': 'ai-assistant',
            'AIアシスタント': 'ai-assistant',
            'AIアシスタント': 'ai-assistant',
            'ガイドライン改善提案': 'feedback',
            'ガイドライン追加・改善': 'feedback',
            'コンテンツ追加・修正ガイド': 'content-guide'
        }
        
        # 変換テーブルで一致するものがあれば使用
        for jp, en in replacements.items():
            if jp in name:
                # 「はじめに」はintroductionに変更（indexではなく）
                if jp == 'はじめに':
                    return 'introduction'
                return en
        
        # 一致しない場合は安全な形式に変換
        # 日本語が含まれている場合は簡単な変換を試みる
        if re.search(r'[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf]', name):
            # ファイル名に番号があれば利用
            match = re.match(r'^(\d+)', original_filename)
            if match:
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
    
    def generate_sidebar(self):
        """ページ情報からサイドバーHTMLを生成"""
        categories = {}
        
        # カテゴリごとにページを分類（サブカテゴリも考慮）
        for page in self.pages:
            category = page['category']
            if category not in categories:
                categories[category] = {'pages': [], 'subcategories': {}}
            
            # サブカテゴリがある場合（例：01_はじめに/以下のファイル）
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
<a href="index.html" class="nav-item">ホーム</a>
<div class="nav-divider"></div>'''
        
        # カテゴリの表示順序を定義
        category_order = ["基本情報", "商談マニュアル", "その他", "Loom動画"]
        
        # 定義された順序でカテゴリを表示
        for category in category_order:
            if category in categories:
                cat_data = categories[category]
                sidebar_html += f'''
<div class="category collapsed">
<div class="category-title">{category}</div>
<div class="category-content">'''
                
                # まずサブカテゴリを表示（「はじめに」など）
                for subcategory, subpages in cat_data['subcategories'].items():
                    # サブカテゴリ名を整形（番号プレフィックスを除去）
                    clean_subcat = re.sub(r'^\d+[_-]', '', subcategory)
                    
                    # サブカテゴリのタイトルを決定
                    subcat_title = clean_subcat
                    
                    # サブカテゴリのセクション（独立したサブカテゴリフォルダとして）
                    sidebar_html += f'''
<div class="subcategory-folder collapsed">
<div class="subcategory-folder-title">{subcat_title}</div>
<div class="subcategory-folder-content">'''
                    
                    # サブページを表示
                    for page in sorted(subpages, key=lambda x: x.get('order', 999)):
                        # indexページはスキップ
                        if 'index' in page.get('filename', '').lower():
                            continue
                        page_title = page['title']
                        # 短縮版のタイトルを作成（長すぎる場合）
                        if len(page_title) > 25:
                            page_title = page_title.split('：')[0] if '：' in page_title else page_title[:25] + '...'
                        sidebar_html += f'''
<a href="{page['output_name']}" class="nav-item">{page_title}</a>'''
                    
                    sidebar_html += '\n</div>\n</div>'
                
                # 通常のページを表示（サブカテゴリに属さないもの）
                for page in cat_data['pages']:
                    # サイドバー用のタイトル（AIチャットの場合は「（テスト版）」を除去）
                    sidebar_title = page['title']
                    if sidebar_title == 'AIチャット（テスト版）':
                        sidebar_title = 'AIチャット'
                    
                    # このページがサブカテゴリと同名でないかチェック
                    is_subcategory_parent = False
                    for subcategory in cat_data['subcategories'].keys():
                        clean_subcat = re.sub(r'^\d+[_-]', '', subcategory)
                        if clean_subcat == sidebar_title or clean_subcat == page['title']:
                            is_subcategory_parent = True
                            break
                    
                    # サブカテゴリの親ページでない場合のみ表示
                    if not is_subcategory_parent:
                        sidebar_html += f'''
<a href="{page['output_name']}" class="nav-item">{sidebar_title}</a>'''
                
                sidebar_html += '\n</div>\n</div>'
        
        # 定義されていないカテゴリも追加
        for category, cat_data in categories.items():
            if category not in category_order:
                sidebar_html += f'''
<div class="category collapsed">
<div class="category-title">{category}</div>
<div class="category-content">'''
                
                # 通常のページ
                for page in cat_data['pages']:
                    # サイドバー用のタイトル（AIチャットの場合は「（テスト版）」を除去）
                    sidebar_title = page['title']
                    if sidebar_title == 'AIチャット（テスト版）':
                        sidebar_title = 'AIチャット'
                    sidebar_html += f'''
<a href="{page['output_name']}" class="nav-item">{sidebar_title}</a>'''
                
                sidebar_html += '\n</div>\n</div>'
        
        sidebar_html += '\n</nav>'
        
        # サイドバーフッターを追加
        sidebar_html += '''
<div class="sidebar-footer">
    <button class="footer-link" onclick="toggleAiPanel(); event.stopPropagation();">AIチャット</button>
    <div class="footer-divider"></div>
    <a href="feedback.html" class="footer-link">ガイドライン改善提案</a>
</div>'''
        
        return sidebar_html
    
    def generate_search_index(self):
        """検索用のインデックスを生成"""
        search_index = []
        
        for page in self.pages:
            # Markdownをパース
            md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc', 'nl2br'])
            html_content = md.convert(page['content'])
            
            # HTMLタグを除去してテキストのみ抽出
            soup = BeautifulSoup(html_content, 'html.parser')
            text_content = soup.get_text()
            
            # セクションごとに分割してインデックスを作成
            sections = []
            lines = text_content.split('\n')
            current_section = {
                'title': page['title'],
                'content': '',
                'level': 0
            }
            
            # コンテンツを見出しごとに分割
            for line in page['content'].split('\n'):
                line = line.strip()
                
                # 見出しを検出
                heading_match = re.match(r'^(#{1,3})\s+(.+)$', line)
                if heading_match:
                    # 前のセクションを保存
                    if current_section['content']:
                        sections.append(current_section.copy())
                    
                    level = len(heading_match.group(1))
                    title = heading_match.group(2)
                    
                    # 新しいセクションを開始
                    current_section = {
                        'title': title,
                        'content': '',
                        'level': level
                    }
                else:
                    # 見出し以外のコンテンツを追加
                    if line:
                        current_section['content'] += line + ' '
            
            # 最後のセクションを保存
            if current_section['content']:
                sections.append(current_section)
            
            # 各セクションをインデックスに追加
            for section in sections:
                # セクションIDを生成（アンカーリンク用）
                section_id = re.sub(r'[^\w\s-]', '', section['title'])
                section_id = re.sub(r'\s+', '-', section_id).lower()
                
                search_index.append({
                    'pageTitle': page['title'],
                    'sectionTitle': section['title'],
                    'content': section['content'][:300],  # 最初の300文字
                    'url': page['output_name'],
                    'sectionId': section_id,
                    'category': page['category']
                })
        
        return search_index
    
    def generate_site(self):
        """サイト全体を生成"""
        print("🔍 Markdownファイルを検索中...")
        self.scan_markdown_files()
        print(f"📄 {len(self.pages)}個のページを検出しました")
        
        # 出力ディレクトリを準備
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # テンプレートを読み込み（AIチャット機能付きテンプレートを使用）
        template_path = self.template_dir / "page_light_with_ai.html"
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        
        # サイドバーを生成
        sidebar_html = self.generate_sidebar()
        
        # 各ページを生成
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc', 'nl2br'])
        
        for i, page in enumerate(self.pages):
            print(f"⚡ {page['title']} を生成中...")
            
            # Markdownをレンダリング
            html_content = md.convert(page['content'])
            md.reset()
            
            # h1タグがコンテンツに含まれている場合は削除（タイトルの重複を防ぐ）
            # BeautifulSoupを使ってHTMLを解析
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            first_h1 = soup.find('h1')
            if first_h1 and first_h1.text.strip() == page['title']:
                first_h1.decompose()  # 最初のh1タグを削除
                html_content = str(soup)
            
            # テンプレートに埋め込み
            output = template.replace('{{TITLE}}', page['title'])
            output = output.replace('{{SIDEBAR}}', sidebar_html)
            output = output.replace('{{CONTENT}}', f'<h1 class="page-title">{page["title"]}</h1>\n{html_content}')
            
            # ファイルを保存
            output_path = self.output_dir / page['output_name']
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(output)
        
        # ホームページを生成
        self.generate_index_page(template, sidebar_html)
        
        # 検索インデックスを生成
        search_index = self.generate_search_index()
        search_index_path = self.output_dir / 'search-index.json'
        with open(search_index_path, 'w', encoding='utf-8') as f:
            json.dump(search_index, f, ensure_ascii=False, indent=2)
        
        print(f"✅ サイト生成完了！ {self.output_dir} を確認してください")
        
        # ページ一覧を表示
        print("\n📚 生成されたページ:")
        for category, pages in self.get_pages_by_category().items():
            print(f"\n【{category}】")
            for page in pages:
                print(f"  - {page['title']} ({page['output_name']})")
    
    def generate_index_page(self, template, sidebar_html):
        """ホームページを生成"""
        content = '''
# Harukazeガイドライン

このサイトはHarukazeのディレクター向けガイドラインです。

## 初めての方へ

このガイドラインを初めてご覧になる方は、まず「基本情報」カテゴリのコンテンツから順番にお読みください。基本情報には、ディレクターとして押さえておくべき重要な5つのコンテンツがまとめられています。

## コンテンツ一覧
'''
        
        # カテゴリの表示順序
        category_order = ["基本情報", "商談マニュアル", "その他"]
        
        # カテゴリごとにリンクを生成
        for category in category_order:
            pages = [p for p in self.pages if p['category'] == category]
            if pages:
                content += f"\n### {category}\n\n"
                for page in pages:
                    content += f"- [{page['title']}]({page['output_name']})\n"
        
        # 定義されていないカテゴリも追加
        other_categories = [cat for cat in set(p['category'] for p in self.pages) if cat not in category_order]
        for category in other_categories:
            pages = [p for p in self.pages if p['category'] == category]
            if pages:
                content += f"\n### {category}\n\n"
                for page in pages:
                    content += f"- [{page['title']}]({page['output_name']})\n"
        
        content += '''
## フィードバック

ガイドラインをより良くするため、ぜひご意見をお聞かせください。

→ [改善提案フォームはこちら](feedback.html)
'''
        
        # Markdownをレンダリング
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc', 'nl2br'])
        html_content = md.convert(content)
        
        # テンプレートに埋め込み
        output = template.replace('{{TITLE}}', 'Harukazeガイドライン')
        output = output.replace('{{SIDEBAR}}', sidebar_html)
        output = output.replace('{{CONTENT}}', html_content)
        
        # index.htmlとして保存
        output_path = self.output_dir / 'index.html'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)
        
        print("⚡ ホームページ を生成中...")
    
    def get_pages_by_category(self):
        """カテゴリごとにページを整理"""
        categories = {}
        for page in self.pages:
            category = page['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(page)
        return categories

def main():
    """メイン処理"""
    generator = AutoSiteGenerator()
    generator.generate_site()

if __name__ == "__main__":
    main()