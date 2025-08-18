#!/usr/bin/env python3
"""
ガイドライン静的サイト生成ツール（クリーン版）
既存マニュアルを除外し、パス問題を解決
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

# 除外するフォルダ
EXCLUDE_FOLDERS = ["05_既存マニュアル（統合対象）", ".git", ".obsidian", "_templates"]

def clean_filename(filename):
    """ファイル名を読みやすい形式に変換"""
    name = Path(filename).stem
    name = re.sub(r'[_-]', ' ', name)
    name = ' '.join(word.capitalize() for word in name.split())
    return name

def safe_filename(filename):
    """ファイル名を安全な形式に変換（ASCII文字のみ）"""
    name = Path(filename).stem
    # 日本語や特殊文字を英数字に変換
    replacements = {
        'プロジェクト管理': 'project_management',
        '開発中ドキュメント': 'development_docs',
        '現行版ガイドライン': 'current_guidelines',
        '参考資料': 'reference_materials',
        'コミュニケーションガイドライン': 'communication_guide',
        'AI生成版': 'ai_generated',
        '実践事例集': 'case_studies',
        '文字起こし資料': 'transcripts',
        '分析データ': 'analysis_data',
        'ドラフト版': 'drafts',
        '骨子・構成案': 'structure_plans',
        '要件定義': 'requirements',
        'プロジェクト進捗': 'project_progress',
        'README': 'readme'
    }
    
    # 日本語を英語に置換
    for jp, en in replacements.items():
        if jp in name:
            name = name.replace(jp, en)
    
    # 残りの日本語文字をローマ字に変換（簡易版）
    name = re.sub(r'[^\w\s-]', '', name)  # 英数字とハイフン、スペースのみ残す
    name = re.sub(r'\s+', '_', name)      # スペースをアンダースコアに
    name = name.lower()                   # 小文字に統一
    
    return name if name else 'untitled'

def should_exclude_folder(folder_name):
    """フォルダを除外するかどうかを判定"""
    return any(exclude in folder_name for exclude in EXCLUDE_FOLDERS)

def generate_sidebar(root_path):
    """フォルダ構造からサイドバーHTMLを生成"""
    sidebar_html = ['<div class="sidebar">']
    sidebar_html.append('<h2>📚 ガイドライン</h2>')
    sidebar_html.append('<ul class="nav">')
    
    # README.mdがあれば最初に表示
    index_file = Path(root_path) / "README.md"
    if index_file.exists():
        sidebar_html.append('<li><a href="readme.html" class="nav-link">🏠 トップページ</a></li>')
    
    def walk_directory(current_path, level=0):
        items = []
        current_dir = Path(current_path)
        
        # ディレクトリを処理
        for item in sorted(current_dir.iterdir()):
            if (item.is_dir() and 
                not item.name.startswith('.') and 
                not item.name.startswith('_') and
                not should_exclude_folder(item.name)):
                
                folder_name = clean_filename(item.name)
                items.append(f'<li class="folder-item level-{level}">')
                items.append(f'<span class="folder-title">📁 {folder_name}</span>')
                items.append('<ul class="sub-nav">')
                
                # サブディレクトリの内容を再帰的に処理
                items.extend(walk_directory(item, level + 1))
                
                items.append('</ul>')
                items.append('</li>')
        
        # Markdownファイルを処理
        for item in sorted(current_dir.iterdir()):
            if item.suffix == '.md' and not item.name.startswith('.'):
                file_name = clean_filename(item.name)
                safe_name = safe_filename(item.name)
                html_name = safe_name + '.html'
                
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
                elif "draft" in item.name.lower() or "ドラフト" in item.name:
                    icon = "✏️"
                elif "骨子" in item.name or "構成" in item.name:
                    icon = "🏗️"
                
                items.append(f'<li><a href="{html_name}" class="nav-link level-{level}">{icon} {file_name}</a></li>')
        
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
        
        # タイトルを抽出
        title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
        else:
            title = clean_filename(file_path.name)
        
        # テンプレートにコンテンツを挿入
        final_html = template_content.replace('{{TITLE}}', title)
        final_html = final_html.replace('{{CONTENT}}', html_content)
        final_html = final_html.replace('{{SIDEBAR}}', sidebar_html)
        
        # 出力ファイル名（全てルートに配置してパス問題を回避）
        safe_name = safe_filename(file_path.name)
        output_file = output_path / (safe_name + '.html')
        
        # HTMLファイルを保存
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        relative_path = file_path.relative_to(root_path)
        print(f"✅ 生成完了: {relative_path} -> {output_file.name}")
        
    except Exception as e:
        print(f"❌ エラー: {file_path} - {str(e)}")

def main():
    """メイン処理"""
    print("🚀 ガイドライン静的サイト生成を開始します（クリーン版）...")
    
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
    
    # 除外フォルダを表示
    print(f"🚫 除外フォルダ: {', '.join(EXCLUDE_FOLDERS)}")
    
    # すべてのMarkdownファイルを処理
    print("📄 Markdownファイルを変換中...")
    md_files = []
    
    for md_file in root_path.rglob('*.md'):
        # 除外条件をチェック
        if (md_file.name.startswith('.') or 
            md_file.name.startswith('_') or
            any(exclude in str(md_file) for exclude in EXCLUDE_FOLDERS)):
            continue
        md_files.append(md_file)
    
    print(f"📊 処理対象ファイル数: {len(md_files)}")
    
    for md_file in md_files:
        process_file(md_file, root_path, output_path, sidebar_html, template_content)
    
    print(f"\n🎉 サイト生成完了！")
    print(f"📁 出力フォルダ: {output_path.absolute()}")
    print(f"🌐 ブラウザで {output_path.absolute()}/readme.html を開いてください")

if __name__ == "__main__":
    main()