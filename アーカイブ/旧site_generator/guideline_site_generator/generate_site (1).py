#!/usr/bin/env python3
"""
ガイドライン静的サイト生成ツール
Markdownファイルから美しいHTMLサイトを自動生成します
"""

import os
import shutil
import markdown
from pathlib import Path
import re

# 設定
ROOT_FOLDER = "/Users/ogatahisashi/Library/CloudStorage/GoogleDrive-harukazeteam01@gmail.com/My Drive/HarukazeDatabase/Dynamic Knowledge/toB knowledge/ガイドラインプロジェクト"
OUTPUT_FOLDER = "site_output"
TEMPLATE_FILE = "_templates/page.html"

def clean_filename(filename):
    """ファイル名を読みやすい形式に変換"""
    # 拡張子を除去
    name = Path(filename).stem
    # アンダースコアとハイフンをスペースに
    name = re.sub(r'[_-]', ' ', name)
    # 各単語の先頭を大文字に
    name = ' '.join(word.capitalize() for word in name.split())
    return name

def generate_sidebar(root_path):
    """フォルダ構造からサイドバーHTMLを生成"""
    sidebar_html = ['<div class="sidebar">']
    sidebar_html.append('<h2>📚 ガイドライン</h2>')
    sidebar_html.append('<ul class="nav">')
    
    # index.mdがあれば最初に表示
    index_file = Path(root_path) / "README.md"
    if index_file.exists():
        sidebar_html.append('<li><a href="README.html" class="nav-link">🏠 トップページ</a></li>')
    
    # フォルダとファイルを走査
    def walk_directory(current_path, relative_path="", level=0):
        items = []
        
        # 現在のディレクトリのmdファイルとサブディレクトリを収集
        current_dir = Path(current_path)
        
        # まずディレクトリを処理
        for item in sorted(current_dir.iterdir()):
            if item.is_dir() and not item.name.startswith('.') and not item.name.startswith('_'):
                folder_name = clean_filename(item.name)
                items.append(f'<li class="folder-item level-{level}">')
                items.append(f'<span class="folder-title">📁 {folder_name}</span>')
                items.append('<ul class="sub-nav">')
                
                # サブディレクトリの内容を再帰的に処理
                sub_relative = f"{relative_path}/{item.name}" if relative_path else item.name
                items.extend(walk_directory(item, sub_relative, level + 1))
                
                items.append('</ul>')
                items.append('</li>')
        
        # 次にMarkdownファイルを処理
        for item in sorted(current_dir.iterdir()):
            if item.suffix == '.md' and not item.name.startswith('.'):
                file_name = clean_filename(item.name)
                html_name = item.stem + '.html'
                link_path = f"{relative_path}/{html_name}" if relative_path else html_name
                
                # アイコンを内容に応じて変更
                icon = "📋"
                if "v1" in item.name or "v2" in item.name or "v3" in item.name:
                    icon = "🔄"
                elif "README" in item.name:
                    icon = "🏠"
                elif "要件" in item.name:
                    icon = "📝"
                elif "進捗" in item.name:
                    icon = "📊"
                
                items.append(f'<li><a href="{link_path}" class="nav-link level-{level}">{icon} {file_name}</a></li>')
        
        return items
    
    sidebar_items = walk_directory(root_path)
    sidebar_html.extend(sidebar_items)
    
    sidebar_html.append('</ul>')
    sidebar_html.append('</div>')
    
    return '\n'.join(sidebar_html)

def convert_markdown_to_html(md_content):
    """MarkdownをHTMLに変換"""
    md = markdown.Markdown(extensions=[
        'extra',
        'toc',
        'codehilite',
        'tables'
    ])
    return md.convert(md_content)

def process_file(file_path, root_path, output_path, sidebar_html, template_content):
    """単一のMarkdownファイルを処理してHTMLを生成"""
    try:
        # Markdownファイルを読み込み
        with open(file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # HTMLに変換
        html_content = convert_markdown_to_html(md_content)
        
        # タイトルを抽出（最初のh1タグまたはファイル名）
        title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
        else:
            title = clean_filename(file_path.name)
        
        # テンプレートにコンテンツを挿入
        final_html = template_content.replace('{{TITLE}}', title)
        final_html = final_html.replace('{{CONTENT}}', html_content)
        final_html = final_html.replace('{{SIDEBAR}}', sidebar_html)
        
        # 出力ファイルパスを計算
        relative_path = file_path.relative_to(root_path)
        output_file = output_path / relative_path.with_suffix('.html')
        
        # 出力ディレクトリを作成
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # HTMLファイルを保存
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        print(f"✅ 生成完了: {relative_path} -> {output_file.name}")
        
    except Exception as e:
        print(f"❌ エラー: {file_path} - {str(e)}")

def main():
    """メイン処理"""
    print("🚀 ガイドライン静的サイト生成を開始します...")
    
    root_path = Path(ROOT_FOLDER)
    output_path = Path(OUTPUT_FOLDER)
    template_path = Path(TEMPLATE_FILE)
    
    # 出力ディレクトリをクリーンアップ
    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir(parents=True)
    
    # テンプレートファイルを読み込み
    if not template_path.exists():
        print(f"❌ テンプレートファイルが見つかりません: {template_path}")
        return
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # サイドバーHTMLを生成
    print("📋 サイドバーを生成中...")
    sidebar_html = generate_sidebar(root_path)
    
    # すべてのMarkdownファイルを処理
    print("📄 Markdownファイルを変換中...")
    md_files = list(root_path.rglob('*.md'))
    
    for md_file in md_files:
        # テンプレートファイルやhiddenファイルはスキップ
        if md_file.name.startswith('.') or md_file.name.startswith('_'):
            continue
            
        process_file(md_file, root_path, output_path, sidebar_html, template_content)
    
    print(f"\n🎉 サイト生成完了！")
    print(f"📁 出力フォルダ: {output_path.absolute()}")
    print(f"🌐 ブラウザで {output_path.absolute()}/README.html を開いてください")

if __name__ == "__main__":
    main()