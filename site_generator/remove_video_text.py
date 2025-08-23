#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdownファイルから「動画で理解する」の文言と古いナビゲーションボタンを削除するスクリプト
"""

import os
import re
import glob

def remove_unwanted_content(file_path):
    """指定されたファイルから不要なコンテンツを削除する"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 「動画で理解する（〇分）」の見出しを削除
    # ## 動画で理解する（3分） のようなパターンを削除
    content = re.sub(r'^##\s*動画で理解する[（(][^)）]*[)）]\s*\n+', '', content, flags=re.MULTILINE)
    
    # 古いナビゲーションボタンを削除
    # <div style="display: flex; ... </div> のような複数行にわたるナビゲーションを削除
    content = re.sub(
        r'<div style="display: flex;[^>]*>.*?</div>\s*\n*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # .mdへのリンクを削除（古いナビゲーションリンク）
    # 例: <a href="02_品質問題：基本的なミスの連発.md">次のページ →</a>
    content = re.sub(
        r'<a href="[^"]+\.md">[^<]*</a>',
        '',
        content
    )
    
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
    md_files = glob.glob(os.path.join(content_dir, '**/*.md'), recursive=True)
    
    # アーカイブフォルダ内のファイルは除外
    md_files = [f for f in md_files if 'アーカイブ' not in f]
    
    updated_files = []
    
    for file_path in md_files:
        if remove_unwanted_content(file_path):
            updated_files.append(file_path)
            print(f"✅ 更新: {os.path.basename(file_path)}")
    
    print(f"\n📊 更新結果:")
    print(f"  - 総ファイル数: {len(md_files)}")
    print(f"  - 更新されたファイル数: {len(updated_files)}")

if __name__ == '__main__':
    main()