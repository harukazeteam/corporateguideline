const OpenAI = require('openai');

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

  // ガイドラインデータを直接読み込み
  const guidelines = require('./guidelines-data.js');

  try {
    const { message } = req.body;
    
    if (!message) {
      return res.status(400).json({ error: 'Message is required' });
    }

    // OpenAI クライアントを初期化
    const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    });

    // ユーザーの質問に関連するガイドラインを検索
    const relevantGuidelines = findRelevantGuidelines(message, guidelines);
    
    // コンテキストを構築
    const context = buildContext(relevantGuidelines);
    
    // OpenAI APIを呼び出し
    const completion = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: [
        {
          role: 'system',
          content: `あなたはHarukazeガイドラインのAIアシスタントです。
以下のガイドライン情報を基に、ユーザーの質問に的確に答えてください。
回答は具体的で実践的なアドバイスを心がけ、関連するページがあれば必ず紹介してください。

利用可能なガイドライン情報:
${context}

回答形式:
1. 質問に対する直接的な回答
2. 具体的な実践方法やポイント
3. 「詳しくは〇〇ページをご覧ください」という形で関連ページを紹介`
        },
        {
          role: 'user',
          content: message
        }
      ],
      temperature: 0.7,
      max_tokens: 800,
    });

    const response = completion.choices[0].message.content;
    
    // 関連ページ情報を追加
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
    console.error('Detailed error:', error.message);
    console.error('Error stack:', error.stack);
    
    // エラー時は簡易回答にフォールバック
    const fallbackResponse = generateSimpleResponse(message || '');
    
    res.status(200).json({
      response: fallbackResponse + '\n\n（注: AIによる詳細な回答機能に一時的な問題が発生しています）',
      relatedPages: [],
      success: true,
      debug: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
}

// 関連するガイドラインを検索
function findRelevantGuidelines(query, guidelines) {
  if (!guidelines || guidelines.length === 0) {
    return [];
  }
  
  const queryLower = query.toLowerCase();
  const scores = [];

  guidelines.forEach(guideline => {
    let score = 0;
    
    // タイトルに含まれる場合は高スコア
    if (guideline.title && guideline.title.toLowerCase().includes(queryLower)) {
      score += 10;
    }
    
    // キーワードマッチング
    if (guideline.keywords && Array.isArray(guideline.keywords)) {
      guideline.keywords.forEach(keyword => {
        if (queryLower.includes(keyword) || keyword.includes(queryLower)) {
          score += 5;
        }
      });
    }
    
    // コンテンツに含まれる場合
    if (guideline.content) {
      const contentMatches = (guideline.content.toLowerCase().match(new RegExp(queryLower, 'g')) || []).length;
      score += contentMatches * 0.5;
    }
    
    // カテゴリマッチング
    if (guideline.category && queryLower.includes(guideline.category.toLowerCase())) {
      score += 3;
    }
    
    if (score > 0) {
      scores.push({ guideline, score });
    }
  });

  // スコアの高い順にソート
  scores.sort((a, b) => b.score - a.score);
  
  return scores.slice(0, 5).map(s => s.guideline);
}

// コンテキストを構築
function buildContext(guidelines) {
  if (!guidelines || guidelines.length === 0) {
    return 'ガイドラインに関連する情報が見つかりませんでした。';
  }

  return guidelines.map(g => {
    const excerpt = (g.summary || '').substring(0, 200) + '...';
    return `
【${g.title}】（${g.category || '未分類'}）
${excerpt}
URL: ${g.url || 'N/A'}
`;
  }).join('\n---\n');
}

// 簡易的な回答生成（フォールバック用）
function generateSimpleResponse(query) {
  const responses = {
    '納期': '納期に関するご質問ですね。納期が遅れそうな場合は、まず早めにクライアントに連絡することが重要です。具体的な対応方法については「代表的なトラブルシューティング」ページをご覧ください。',
    'フィードバック': 'フィードバックについてのご質問ですね。効果的なフィードバックは具体的で建設的であることが大切です。詳しくは「コミュニケーションガイド」ページをご覧ください。',
    'デザイナー': 'デザイナーとの協働についてのご質問ですね。デザイナーとの円滑なコミュニケーションは、プロジェクト成功の鍵です。「ディレクターの心得」ページに詳しい情報があります。',
    '品質': '品質管理についてのご質問ですね。品質チェックは段階的に行うことが重要です。「全体の業務プロセス」ページをご覧ください。',
    'クライアント': 'クライアントとの関係性についてのご質問ですね。信頼関係の構築は、ビジネス成功の基盤です。「信頼関係の構築テクニック」ページをご覧ください。',
    'ヒアリング': 'ヒアリングについてのご質問ですね。効果的なヒアリングは、クライアントのニーズを正確に把握する鍵です。「ヒアリングマスター講座」ページをご覧ください。',
    '提案': '提案についてのご質問ですね。説得力のある提案は、案件獲得の決め手となります。「提案力を高める実践テクニック」ページをご覧ください。',
    'クロージング': 'クロージングについてのご質問ですね。適切なタイミングでのクロージングが成約率を高めます。「クロージング成功の秘訣」ページをご覧ください。'
  };
  
  for (const [key, response] of Object.entries(responses)) {
    if (query.includes(key)) {
      return response;
    }
  }
  
  return `ご質問ありがとうございます。「${query}」についてガイドラインを確認しています。該当する情報が見つからない場合は、検索機能をご利用いただくか、より具体的な質問をお願いします。`;
}