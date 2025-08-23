#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
番号付きタイトルを正しく更新するスクリプト
1-1.などは残し、01_などは削除する
"""

import os
import re
import glob

def extract_title_from_filename(filename):
    """ファイル名からタイトルを抽出（01_などは削除、1-1.などは保持）"""
    # ファイル名から.mdを除去
    name = filename.replace('.md', '')
    
    # 01_、02_、03_、04_、05_などの単純なプレフィックスを削除
    name = re.sub(r'^0?\d+_', '', name)
    
    # ただし、1-1.、2-2.などのハイフン付き番号は残す
    # （すでに処理済みなので何もしない）
    
    return name

def update_title(file_path):
    """指定されたファイルのタイトルを更新する"""
    
    filename = os.path.basename(file_path)
    new_title = extract_title_from_filename(filename)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # フロントマターのtitleを更新
    in_frontmatter = False
    title_updated = False
    h1_updated = False
    
    for i, line in enumerate(lines):
        # フロントマターの開始/終了を検出
        if line.strip() == '---':
            if i == 0:
                in_frontmatter = True
            elif in_frontmatter:
                in_frontmatter = False
        
        # フロントマター内のtitleを更新
        elif in_frontmatter and line.startswith('title:'):
            lines[i] = f'title: {new_title}\n'
            title_updated = True
        
        # H1タグを更新（フロントマター外）
        elif not in_frontmatter and line.startswith('# ') and not h1_updated:
            lines[i] = f'# {new_title}\n'
            h1_updated = True
    
    # ファイルに書き戻す
    if title_updated or h1_updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return True, new_title
    
    return False, new_title

def main():
    """メイン処理"""
    
    # サイトコンテンツディレクトリのパス
    content_dir = '/Users/ogatahisashi/Desktop/corporateguideline/サイトコンテンツ/01_最初にみる動画'
    
    # 処理対象のMarkdownファイルを取得
    md_files = glob.glob(os.path.join(content_dir, '**/*.md'), recursive=True)
    
    # indexファイルは除外
    md_files = [f for f in md_files if not f.endswith('index.md')]
    
    updated_files = []
    
    for file_path in md_files:
        updated, new_title = update_title(file_path)
        if updated:
            updated_files.append(file_path)
            print(f"✅ 更新: {os.path.basename(file_path)} → {new_title}")
    
    print(f"\n📊 更新結果:")
    print(f"  - 総ファイル数: {len(md_files)}")
    print(f"  - 更新されたファイル数: {len(updated_files)}")

if __name__ == '__main__':
    main()