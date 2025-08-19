#!/usr/bin/env python3
"""
古いナビゲーションリンクをMarkdownファイルから削除するスクリプト
"""

import os
import re
from pathlib import Path

def remove_old_navigation(file_path):
    """Markdownファイルから古いナビゲーションを削除"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # パターン1: 前へ/次へナビゲーションバー全体を削除（両方のフォーマットに対応）
    pattern1 = r'<div style="display: flex;[^>]*?>.*?← 前へ.*?次へ.*?</div>\n*'
    content = re.sub(pattern1, '', content, flags=re.DOTALL)
    
    # パターン2: 「次の動画へ」ボタンを削除
    pattern2 = r'<div style="text-align: center;[^>]*?>.*?次の動画へ.*?</div>\n*'
    content = re.sub(pattern2, '', content, flags=re.DOTALL)
    
    # パターン3: 単独の次へボタンリンク
    pattern3 = r'<a href="[^"]*\.html"[^>]*>次の動画へ[^<]*</a>\n*'
    content = re.sub(pattern3, '', content, flags=re.DOTALL)
    
    # 変更があった場合のみファイルを更新
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    content_dir = Path('../サイトコンテンツ')
    
    # 対象ファイルのリスト
    target_files = [
        '01_基本情報/03_全体の業務プロセス/02_ヒアリング、提案、見積もりフェーズ.md',
        '01_基本情報/02_ディレクターの心得/02_主要な当事者領域責任範囲.md',
        '01_基本情報/03_全体の業務プロセス/08_振り返りフェーズ.md',
        '01_基本情報/03_全体の業務プロセス/07_請求支払いフェーズ.md',
        '01_基本情報/03_全体の業務プロセス/06_納品フェーズ.md',
        '01_基本情報/03_全体の業務プロセス/05_プロジェクト始動、制作フェーズ.md',
        '01_基本情報/03_全体の業務プロセス/04_チーム結成フェーズ.md',
        '01_基本情報/03_全体の業務プロセス/03_受注、契約フェーズ.md',
        '01_基本情報/03_全体の業務プロセス/01_前提問い合わせフェーズ.md',
        '01_基本情報/01_はじめに/05_マニュアル活用法.md',
        '01_基本情報/01_はじめに/04_Harukazeから提供てきること.md',
        '01_基本情報/01_はじめに/03_Harukazeの理念.md',
        '01_基本情報/01_はじめに/02_vision.md',
    ]
    
    updated_count = 0
    for file_path in target_files:
        full_path = content_dir / file_path
        if full_path.exists():
            if remove_old_navigation(full_path):
                print(f"✅ 更新: {file_path}")
                updated_count += 1
            else:
                print(f"⏭️  変更なし: {file_path}")
        else:
            print(f"❌ ファイルが見つかりません: {file_path}")
    
    print(f"\n合計 {updated_count} ファイルを更新しました。")

if __name__ == "__main__":
    main()