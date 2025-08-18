#!/usr/bin/env python3
"""
ガイドライン静的サイト生成ツール（site_config.json対応版）
"""

import os
import json
import shutil
import markdown
from pathlib import Path
import re

# 設定ファイルを読み込む
with open('site_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# 設定
ROOT_FOLDER = os.getcwd()
SOURCE_FOLDER = config['source_folder']
OUTPUT_FOLDER = config['output_folder']
TEMPLATE_FILE = config['template_file']

def generate_site():
    """サイトを生成"""
    print("🚀 ガイドライン静的サイト生成を開始します...")
    
    # 出力フォルダをクリーンアップ
    if os.path.exists(OUTPUT_FOLDER):
        shutil.rmtree(OUTPUT_FOLDER)
    os.makedirs(OUTPUT_FOLDER)
    
    # テンプレートを読み込む
    template_path = os.path.join(ROOT_FOLDER, TEMPLATE_FILE)
    if not os.path.exists(template_path):
        print(f"❌ テンプレートファイルが見つかりません: {TEMPLATE_FILE}")
        return
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 各ファイルを処理
    nav_items = []
    
    for filename in config['include_files']:
        file_path = os.path.join(ROOT_FOLDER, SOURCE_FOLDER, filename)
        
        if not os.path.exists(file_path):
            print(f"⚠️  ファイルが見つかりません: {file_path}")
            continue
        
        # マークダウンを読み込んで変換
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # マークダウンをHTMLに変換
        html_content = markdown.markdown(content, extensions=['fenced_code', 'tables', 'toc'])
        
        # ファイル情報を取得
        file_info = config['files'].get(filename, {})
        title = file_info.get('title', Path(filename).stem)
        category = file_info.get('category', '未分類')
        
        # 出力ファイル名を決定
        safe_name = config['filename_replacements'].get(Path(filename).stem, Path(filename).stem)
        output_filename = f"{safe_name}.html"
        
        # HTMLを生成
        page_html = template
        page_html = page_html.replace('{{TITLE}}', title)
        page_html = page_html.replace('{{CONTENT}}', html_content)
        page_html = page_html.replace('{{SIDEBAR}}', '')  # 旧テンプレート用
        page_html = page_html.replace('{{NAV_LINKS}}', '')  # 後で更新
        # {{SIDEBAR_CONTENT}} は後で置換するので、ここでは置換しない
        
        # ファイルを保存
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page_html)
        
        print(f"✅ 生成完了: {output_filename}")
        
        # ナビゲーション項目を追加
        nav_items.append({
            'title': title,
            'url': output_filename,
            'category': category
        })
    
    # 全ページのナビゲーションを更新
    nav_links_html = generate_nav_links(nav_items)
    sidebar_html = generate_sidebar_content(nav_items)
    
    for filename in os.listdir(OUTPUT_FOLDER):
        if filename.endswith('.html'):
            file_path = os.path.join(OUTPUT_FOLDER, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 現在のページをアクティブにする
            current_file = filename
            updated_nav = nav_links_html
            for item in nav_items:
                if item['url'] == current_file:
                    updated_nav = updated_nav.replace(f'href="{current_file}"', f'href="{current_file}" class="active"')
                    break
            
            content = content.replace('{{NAV_LINKS}}', updated_nav)
            content = content.replace('{{SIDEBAR}}', '')  # 旧テンプレート対応
            content = content.replace('{{SIDEBAR_CONTENT}}', sidebar_html)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
    
    print(f"\n✅ サイト生成が完了しました！")
    print(f"📁 出力先: {os.path.join(ROOT_FOLDER, OUTPUT_FOLDER)}")

def generate_nav_links(nav_items):
    """ナビゲーションリンクHTMLを生成"""
    links = []
    for item in nav_items:
        # 絵文字を除去してシンプルなタイトルに
        simple_title = item['title'].split(' ')[1] if ' ' in item['title'] else item['title']
        links.append(f'<a href="{item["url"]}">{simple_title}</a>')
    
    return '\n                '.join(links)

def generate_sidebar_content(nav_items):
    """サイドバーコンテンツHTMLを生成"""
    # カテゴリごとにグループ化
    categories = {}
    for item in nav_items:
        category = item['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(item)
    
    # HTMLを生成
    html = []
    
    # カテゴリの順序を定義（基本情報を先に、必須項目を後に）
    category_order = ['基本情報', '必須項目', 'その他要素']
    
    for category in category_order:
        if category in categories:
            html.append(f'<div class="sidebar-category">')
            html.append(f'    <h2>{category}</h2>')
            html.append(f'    <ul class="sidebar-nav">')
            
            for item in categories[category]:
                # 絵文字を除去してシンプルなタイトルに
                simple_title = item['title'].split(' ')[1] if ' ' in item['title'] else item['title']
                html.append(f'        <li><a href="{item["url"]}">{simple_title}</a></li>')
            
            html.append(f'    </ul>')
            html.append(f'</div>')
    
    return '\n'.join(html)

if __name__ == "__main__":
    generate_site()