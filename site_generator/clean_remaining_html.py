#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
残っているHTMLタグを削除するスクリプト
"""

import os
import re
import glob

def clean_remaining_html(file_path):
    """指定されたファイルから残っているHTMLタグを削除する"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # text-align: centerのdivブロックを削除
    # <div style="text-align: center;">...</div> のパターンを削除
    content = re.sub(
        r'<div style="text-align: center[^"]*">.*?</div>\s*\n*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # text-align: leftのdivブロックを削除
    content = re.sub(
        r'<div style="text-align: left[^"]*">.*?</div>\s*\n*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # text-align: rightのdivブロックを削除
    content = re.sub(
        r'<div style="text-align: right[^"]*">.*?</div>\s*\n*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # 孤立した閉じタグを削除
    content = re.sub(r'^\s*</div>\s*$', '', content, flags=re.MULTILINE)
    
    # 連続する空行を2行に制限
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # ファイルが変更された場合のみ書き込む
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """メイン処理"""
    
    # サイトコンテンツディレクトリのパス
    content_dir = '/Users/ogatahisashi/Desktop/corporateguideline/サイトコンテンツ'
    
    # 処理対象のMarkdownファイルを取得
    md_files = glob.glob(os.path.join(content_dir, '01_最初にみる動画/**/*.md'), recursive=True)
    
    updated_files = []
    
    for file_path in md_files:
        if clean_remaining_html(file_path):
            updated_files.append(file_path)
            print(f"✅ クリーン: {os.path.basename(file_path)}")
    
    print(f"\n📊 クリーン結果:")
    print(f"  - 総ファイル数: {len(md_files)}")
    print(f"  - 更新されたファイル数: {len(updated_files)}")

if __name__ == '__main__':
    main()