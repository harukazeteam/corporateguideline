const guidelines = require('./guidelines-data.js');

module.exports = async function handler(req, res) {
  // CORSヘッダーを設定
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  // CORS対応
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { message } = req.body;
    
    if (!message) {
      return res.status(400).json({ error: 'Message is required' });
    }

    // ユーザーの質問に関連するガイドラインを検索
    const relevantGuidelines = findRelevantGuidelines(message, guidelines);
    
    // 高度な簡易回答を生成
    const response = generateAdvancedResponse(message, relevantGuidelines);
    
    // 関連ページ情報
    const relatedPages = relevantGuidelines.slice(0, 3).map(g => ({
      title: g.title,
      url: g.url,
      category: g.category
    }));

    res.status(200).json({
      response,
      relatedPages,
      success: true
    });

  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({
      error: 'Internal server error',
      message: error.message
    });
  }
}

// 関連するガイドラインを検索
function findRelevantGuidelines(query, guidelines) {
  const queryLower = query.toLowerCase();
  const scores = [];

  guidelines.forEach(guideline => {
    let score = 0;
    
    // タイトルマッチング
    if (guideline.title && guideline.title.toLowerCase().includes(queryLower)) {
      score += 20;
    }
    
    // キーワードマッチング
    if (guideline.keywords && Array.isArray(guideline.keywords)) {
      guideline.keywords.forEach(keyword => {
        if (queryLower.includes(keyword.toLowerCase())) {
          score += 10;
        }
      });
    }
    
    // コンテンツマッチング
    if (guideline.content) {
      const words = queryLower.split(/\s+/);
      words.forEach(word => {
        if (word.length > 2 && guideline.content.toLowerCase().includes(word)) {
          score += 2;
        }
      });
    }
    
    if (score > 0) {
      scores.push({ guideline, score });
    }
  });

  scores.sort((a, b) => b.score - a.score);
  return scores.slice(0, 5).map(s => s.guideline);
}

// 高度な簡易回答生成
function generateAdvancedResponse(query, relevantGuidelines) {
  const queryLower = query.toLowerCase();
  
  // 関連ガイドラインがある場合
  if (relevantGuidelines.length > 0) {
    const topGuide = relevantGuidelines[0];
    
    // コンテンツから関連する部分を抽出
    const relevantContent = extractRelevantContent(topGuide.content, query);
    
    let response = `${query}についてのご質問ですね。\n\n`;
    
    // 抽出したコンテンツがある場合
    if (relevantContent) {
      response += `${relevantContent}\n\n`;
    } else {
      // 要約を使用
      response += `${topGuide.summary}\n\n`;
    }
    
    // 関連ページの案内
    response += `詳しくは以下のページをご覧ください：\n`;
    relevantGuidelines.slice(0, 3).forEach(g => {
      response += `- 「${g.title}」（${g.category}）\n`;
    });
    
    return response;
  }
  
  // マッチしない場合のデフォルト回答
  return generateDefaultResponse(query);
}

// コンテンツから関連部分を抽出
function extractRelevantContent(content, query) {
  if (!content) return null;
  
  const lines = content.split('\n');
  const queryWords = query.toLowerCase().split(/\s+/);
  let bestSection = '';
  let bestScore = 0;
  
  // セクションごとに関連度を計算
  let currentSection = [];
  let inRelevantSection = false;
  
  for (const line of lines) {
    // 見出しの場合
    if (line.match(/^#+\s/)) {
      // 前のセクションを評価
      if (currentSection.length > 0) {
        const sectionText = currentSection.join(' ');
        const score = calculateRelevance(sectionText, queryWords);
        if (score > bestScore) {
          bestScore = score;
          bestSection = currentSection.slice(0, 5).join('\n');
        }
      }
      currentSection = [line];
      inRelevantSection = queryWords.some(word => 
        line.toLowerCase().includes(word)
      );
    } else if (inRelevantSection || currentSection.length > 0) {
      currentSection.push(line);
    }
  }
  
  // 最後のセクションを評価
  if (currentSection.length > 0) {
    const sectionText = currentSection.join(' ');
    const score = calculateRelevance(sectionText, queryWords);
    if (score > bestScore) {
      bestSection = currentSection.slice(0, 5).join('\n');
    }
  }
  
  return bestSection || null;
}

// 関連度を計算
function calculateRelevance(text, queryWords) {
  const textLower = text.toLowerCase();
  let score = 0;
  
  queryWords.forEach(word => {
    if (word.length > 2) {
      const matches = (textLower.match(new RegExp(word, 'g')) || []).length;
      score += matches;
    }
  });
  
  return score;
}

// デフォルト回答生成
function generateDefaultResponse(query) {
  const responses = {
    '納期': '納期管理は、プロジェクト成功の鍵となる重要な要素です。\n\n主なポイント：\n1. 早期のリスク察知と報告\n2. バッファを含めたスケジュール設計\n3. 定期的な進捗確認\n\n詳しくは「代表的なトラブルシューティング」ページをご覧ください。',
    'フィードバック': '効果的なフィードバックは、チームの成長と品質向上に不可欠です。\n\n重要な要素：\n1. 具体的で建設的な内容\n2. タイミングの重要性\n3. 相手の立場に立った伝え方\n\n「コミュニケーションガイド」ページに詳しい方法が記載されています。',
    'デザイナー': 'デザイナーとの協働は、プロジェクトの品質を左右します。\n\nポイント：\n1. 明確な要件定義と共有\n2. 適切なスケジュール管理\n3. クリエイティビティを尊重した関係構築\n\n「ディレクターの心得」ページをご参照ください。',
    'クライアント': 'クライアントとの関係構築は、ビジネスの基盤です。\n\n成功の秘訣：\n1. 期待値の適切な管理\n2. 定期的なコミュニケーション\n3. プロフェッショナルな対応\n\n「信頼関係の構築テクニック」ページで詳しく解説しています。',
    'ヒアリング': '効果的なヒアリングは、プロジェクトの方向性を決定づけます。\n\n重要なテクニック：\n1. オープンクエスチョンの活用\n2. 傾聴と共感\n3. 本質的なニーズの把握\n\n「ヒアリングマスター講座」で具体的な手法を学べます。',
    '提案': '説得力のある提案は、案件獲得の決め手となります。\n\n成功する提案の要素：\n1. クライアントの課題への深い理解\n2. 具体的な解決策の提示\n3. 期待を超える付加価値\n\n「提案力を高める実践テクニック」をご覧ください。',
    'トラブル': 'トラブル対応は、信頼関係を深める機会でもあります。\n\n対応のポイント：\n1. 迅速な初動対応\n2. 誠実な説明と謝罪\n3. 再発防止策の提示\n\n「代表的なトラブルシューティング」で詳しく解説しています。'
  };
  
  // キーワードマッチング
  for (const [key, response] of Object.entries(responses)) {
    if (query.includes(key)) {
      return response;
    }
  }
  
  // デフォルト
  return `「${query}」についてお答えします。\n\nこの内容については、ガイドライン内の複数のページで触れられています。\n検索機能を使って関連情報をお探しいただくか、左側のナビゲーションから該当しそうなページをご覧ください。\n\nより具体的なご質問をいただければ、詳しくお答えできます。`;
}