#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Loomリンクを/share/から/embed/に修正するスクリプト
"""

import os
import re
import glob

def fix_loom_links(file_path):
    """Loomのリンクを修正する"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # loom.com/share/ を loom.com/embed/ に変更
    content = re.sub(
        r'https://www\.loom\.com/share/',
        'https://www.loom.com/embed/',
        content
    )
    
    # ファイルが変更された場合のみ書き込む
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """メイン処理"""
    
    # サイトコンテンツディレクトリのパス
    content_dir = '/Users/ogatahisashi/Desktop/corporateguideline/サイトコンテンツ/01_最初にみる動画'
    
    # 処理対象のMarkdownファイルを取得
    md_files = glob.glob(os.path.join(content_dir, '**/*.md'), recursive=True)
    
    updated_files = []
    
    for file_path in md_files:
        if fix_loom_links(file_path):
            updated_files.append(file_path)
            print(f"✅ 修正: {os.path.basename(file_path)}")
    
    print(f"\n📊 修正結果:")
    print(f"  - 総ファイル数: {len(md_files)}")
    print(f"  - 修正されたファイル数: {len(updated_files)}")

if __name__ == '__main__':
    main()