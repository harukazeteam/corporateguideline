#!/usr/bin/env python3
"""
汎用静的サイト生成ツール
どんなプロジェクトでも使える設定ファイル対応版
"""

import os
import shutil
import markdown
from pathlib import Path
import re
import json

def load_config(config_file="site_config.json"):
    """設定ファイルを読み込み"""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ 設定ファイルが見つかりません: {config_file}")
        print("site_config.json を作成してください")
        return None

def clean_filename(filename):
    """ファイル名を読みやすい形式に変換"""
    name = Path(filename).stem
    name = re.sub(r'[_-]', ' ', name)
    name = ' '.join(word.capitalize() for word in name.split())
    return name

def safe_filename(filename, replacements={}):
    """ファイル名を安全な形式に変換"""
    name = Path(filename).stem
    
    # カスタム置換
    for jp, en in replacements.items():
        if jp in name:
            name = en
            break
    
    # 基本的な置換
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'\s+', '_', name).lower()
    
    return name if name else 'untitled'

def get_file_info(filepath, file_config):
    """ファイルパスから表示用の情報を取得"""
    filename = Path(filepath).name
    
    # 設定ファイルから情報を取得
    for file_pattern, info in file_config.items():
        if file_pattern in filename:
            return info
    
    # デフォルト設定
    return {
        "title": f"📋 {clean_filename(filename)}", 
        "category": "その他"
    }

def generate_sidebar(file_list, config):
    """選択されたファイルからサイドバーを生成"""
    sidebar_html = ['<div class="sidebar">']
    sidebar_html.append('<div class="sidebar-header">')
    sidebar_html.append(f'<h1>{config["site_title"]}</h1>')
    sidebar_html.append(f'<p>{config["site_subtitle"]}</p>')
    sidebar_html.append('</div>')
    
    sidebar_html.append('<nav class="sidebar-nav">')
    
    # カテゴリ別にグループ化
    categories = {}
    for filepath in file_list:
        info = get_file_info(filepath, config["files"])
        category = info["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append((filepath, info))
    
    # カテゴリごとに表示
    for category, files in categories.items():
        sidebar_html.append(f'<div class="category">')
        sidebar_html.append(f'<div class="category-title">{category}</div>')
        
        for filepath, info in files:
            safe_name = safe_filename(Path(filepath).name, config.get("filename_replacements", {}))
            html_name = safe_name + '.html'
            sidebar_html.append(f'<a href="{html_name}" class="nav-item">{info["title"]}</a>')
        
        sidebar_html.append('</div>')
    
    sidebar_html.append('</nav>')
    sidebar_html.append('</div>')
    
    return '\n'.join(sidebar_html)

def enhance_content_with_media(content):
    """YouTubeやLoomリンクを埋め込みに変換"""
    # YouTube埋め込み
    youtube_pattern = r'https://(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)|https://youtu\.be/([a-zA-Z0-9_-]+)'
    
    def youtube_replace(match):
        video_id = match.group(1) or match.group(2)
        return f'''
        <div class="video-embed">
            <iframe width="720" height="405" 
                src="https://www.youtube.com/embed/{video_id}" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
            </iframe>
        </div>
        '''
    
    content = re.sub(youtube_pattern, youtube_replace, content)
    
    # Loomリンクのプレビュー
    loom_pattern = r'https://www\.loom\.com/share/([a-zA-Z0-9]+)'
    
    def loom_replace(match):
        video_id = match.group(1)
        return f'''
        <div class="loom-embed">
            <a href="https://www.loom.com/share/{video_id}" target="_blank" class="loom-link">
                🎥 Loom動画を開く
            </a>
        </div>
        '''
    
    content = re.sub(loom_pattern, loom_replace, content)
    
    return content

def convert_markdown_to_html(md_content):
    """MarkdownをHTMLに変換"""
    md = markdown.Markdown(extensions=[
        'extra',
        'toc',
        'codehilite',
        'tables'
    ])
    html_content = md.convert(md_content)
    
    # メディアリンクを埋め込みに変換
    html_content = enhance_content_with_media(html_content)
    
    return html_content

def process_file(file_path, root_path, output_path, sidebar_html, template_content, config):
    """単一のMarkdownファイルを処理してHTMLを生成"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        html_content = convert_markdown_to_html(md_content)
        
        # タイトルを取得
        info = get_file_info(file_path.name, config["files"])
        title = info["title"]
        
        # テンプレートにコンテンツを挿入
        final_html = template_content.replace('{{TITLE}}', title)
        final_html = final_html.replace('{{CONTENT}}', html_content)
        final_html = final_html.replace('{{SIDEBAR}}', sidebar_html)
        
        # 出力ファイル名
        safe_name = safe_filename(file_path.name, config.get("filename_replacements", {}))
        output_file = output_path / (safe_name + '.html')
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        print(f"✅ 生成完了: {info['title']} -> {output_file.name}")
        
    except Exception as e:
        print(f"❌ エラー: {file_path} - {str(e)}")

def main():
    """メイン処理"""
    print("🚀 汎用静的サイト生成ツールを開始...")
    
    # 設定ファイルを読み込み
    config = load_config()
    if not config:
        return
    
    root_path = Path(config["source_folder"])
    output_path = Path(config["output_folder"])
    template_path = Path(config["template_file"])
    
    print(f"📁 ソースフォルダ: {root_path}")
    print(f"📁 出力フォルダ: {output_path}")
    
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
    
    # 対象ファイルを確認
    existing_files = []
    for file_path in config["include_files"]:
        full_path = root_path / file_path
        if full_path.exists():
            existing_files.append(full_path)
            print(f"📄 対象ファイル: {file_path}")
        else:
            print(f"⚠️  ファイルが見つかりません: {file_path}")
    
    if not existing_files:
        print("❌ 対象ファイルが見つかりませんでした")
        return
    
    # サイドバーHTMLを生成
    print("📋 サイドバーを生成中...")
    sidebar_html = generate_sidebar(existing_files, config)
    
    # ファイルを処理
    print("📄 Markdownファイルを変換中...")
    for file_path in existing_files:
        process_file(file_path, root_path, output_path, sidebar_html, template_content, config)
    
    print(f"\n🎉 サイト生成完了！")
    print(f"📁 出力フォルダ: {output_path.absolute()}")
    
    # index.htmlの確認
    index_files = list(output_path.glob("index.html"))
    if index_files:
        print(f"🌐 ブラウザで {index_files[0].absolute()} を開いてください")
    else:
        html_files = list(output_path.glob("*.html"))
        if html_files:
            print(f"🌐 ブラウザで {html_files[0].absolute()} を開いてください")

if __name__ == "__main__":
    main()