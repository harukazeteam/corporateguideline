import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Markdownファイルを読み込んでJSONデータベースを作成
function prepareGuidelineData() {
  const contentDir = path.join(__dirname, '../../../サイトコンテンツ');
  const outputFile = path.join(__dirname, '../data/guidelines.json');
  
  const guidelines = [];
  
  function processDirectory(dir, category = '') {
    const files = fs.readdirSync(dir);
    
    files.forEach(file => {
      const filePath = path.join(dir, file);
      const stat = fs.statSync(filePath);
      
      if (stat.isDirectory() && !file.includes('アーカイブ')) {
        // カテゴリ名を抽出
        const categoryName = file.replace(/^\d+_/, '');
        processDirectory(filePath, categoryName);
      } else if (file.endsWith('.md')) {
        const content = fs.readFileSync(filePath, 'utf8');
        
        // タイトルを抽出
        const titleMatch = content.match(/^#\s+(.+)$/m);
        const title = titleMatch ? titleMatch[1] : file.replace('.md', '');
        
        // URLを生成（site_generatorのロジックに合わせる）
        const fileName = file.replace(/^\d+_/, '').replace('.md', '');
        let url = '';
        
        // ファイル名マッピング
        const fileNameMapping = {
          'はじめに': 'index.html',
          'ディレクターの心得': 'director_mindset.html',
          '全体の業務プロセス': 'business_process.html',
          'コミュニケーションガイド': 'communication_guide.html',
          '代表的なトラブルシューティング': 'troubleshooting.html',
          '実践改善事例集': 'improvement_cases.html',
          'よくある質問FAQ': 'faq.html',
          'AIチャット': 'ai-assistant.html',
          'ガイドライン改善提案': 'feedback.html'
        };
        
        url = fileNameMapping[fileName] || `page_${file.match(/^(\d+)/)?.[1] || '99'}.html`;
        
        // コンテンツを要約（最初の500文字）
        const summary = content
          .replace(/#.*$/gm, '') // 見出しを削除
          .replace(/\n{2,}/g, ' ') // 改行を空白に
          .replace(/[*_`]/g, '') // Markdown記法を削除
          .trim()
          .substring(0, 500);
        
        guidelines.push({
          title,
          category,
          url,
          content: content,
          summary,
          keywords: extractKeywords(content),
          filePath: path.relative(contentDir, filePath)
        });
      }
    });
  }
  
  processDirectory(contentDir);
  
  // データを保存
  fs.mkdirSync(path.dirname(outputFile), { recursive: true });
  fs.writeFileSync(outputFile, JSON.stringify(guidelines, null, 2));
  
  console.log(`Generated guidelines.json with ${guidelines.length} documents`);
}

// キーワードを抽出
function extractKeywords(content) {
  const keywords = [];
  
  // 見出しからキーワードを抽出
  const headings = content.match(/^#{1,3}\s+(.+)$/gm) || [];
  headings.forEach(heading => {
    keywords.push(heading.replace(/^#+\s+/, '').toLowerCase());
  });
  
  // 重要なキーワードを抽出
  const importantWords = [
    '納期', 'デザイナー', 'クライアント', 'フィードバック',
    '品質', 'コミュニケーション', 'トラブル', '商談',
    'ヒアリング', '提案', 'クロージング', '信頼関係'
  ];
  
  importantWords.forEach(word => {
    if (content.includes(word)) {
      keywords.push(word);
    }
  });
  
  return [...new Set(keywords)]; // 重複を削除
}

// 実行
prepareGuidelineData();