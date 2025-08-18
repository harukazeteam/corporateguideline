const { GoogleGenerativeAI } = require('@google/generative-ai');

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
    // ガイドラインデータを安全に読み込む
    let guidelines = [];
    try {
      guidelines = require('./guidelines-data.js');
    } catch (loadError) {
      console.error('Failed to load guidelines data:', loadError);
      // ガイドラインが読み込めなくても続行
    }
    
    const { message } = req.body;
    
    if (!message) {
      return res.status(400).json({ error: 'Message is required' });
    }

    // Gemini APIクライアントを初期化
    const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
    const model = genAI.getGenerativeModel({ model: 'gemini-2.5-flash' });

    // ユーザーの質問に関連するガイドラインを検索
    const relevantGuidelines = findRelevantGuidelines(message, guidelines);
    
    // 関連が薄くても全体的な情報を含める
    if (relevantGuidelines.length < 5 && guidelines.length > 0) {
      // ランダムに追加のガイドラインを含める
      const additionalGuidelines = guidelines
        .filter(g => !relevantGuidelines.includes(g))
        .slice(0, 5 - relevantGuidelines.length);
      relevantGuidelines.push(...additionalGuidelines);
    }
    
    // コンテキストを構築（関連度の高い上位3つのみ使用）
    const topRelevant = relevantGuidelines.slice(0, 3);
    const context = buildContext(topRelevant, message);
    
    // プロンプトを構築
    const prompt = `あなたはHarukazeガイドラインのAIアシスタントです。HarukazeはtoB事業としてデザイン制作を行っているクリエイティブチームです。

以下のガイドライン情報を参考に、ユーザーの質問に答えてください：
${context}

ユーザーの質問: ${message}

回答方法：
1. ガイドラインに記載されている具体的な対処法や推奨事項を3-5項目で箇条書きにしてください
2. 実践的で具体的なアドバイスを心がけてください
3. 最後に「詳しくは『〇〇』ページをご覧ください」と関連ページへ案内してください
4. ガイドラインに明確な記載がない場合は、一般的な知識で補完してください`;

    // Gemini APIを呼び出し
    const result = await model.generateContent(prompt);
    const response = result.response.text();
    
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
    console.error('Gemini API Error:', error);
    
    // エラー時は簡易回答にフォールバック
    const fallbackResponse = generateSimpleResponse(message || '');
    
    res.status(200).json({
      response: fallbackResponse + '\n\n（注: AIによる詳細な回答機能に一時的な問題が発生しています）',
      relatedPages: [],
      success: true
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
    
    // コンテンツに含まれる場合（より重要度を上げる）
    if (guideline.content) {
      const contentLower = guideline.content.toLowerCase();
      // 完全一致は高スコア
      if (contentLower.includes(queryLower)) {
        score += 8;
      }
      // 部分一致も評価
      const queryWords = queryLower.split(/\s+/);
      queryWords.forEach(word => {
        if (word.length > 2 && contentLower.includes(word)) {
          score += 2;
        }
      });
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
  
  return scores.slice(0, 10).map(s => s.guideline);
}

// コンテキストを構築（重要なセクションを優先的に抽出）
function buildContext(guidelines, query) {
  if (!guidelines || guidelines.length === 0) {
    return 'ガイドラインに関連する情報が見つかりませんでした。';
  }

  return guidelines.map(g => {
    const content = g.content || g.summary || '';
    
    // 重要なセクションを抽出
    const sections = extractImportantSections(content, query);
    
    return `
【${g.title}】（${g.category || '未分類'}）
URL: ${g.url}

${sections}
`;
  }).join('\n\n---\n\n');
}

// 重要なセクションを抽出する関数
function extractImportantSections(content, query) {
  const queryLower = query.toLowerCase();
  const lines = content.split('\n');
  const importantSections = [];
  let currentSection = [];
  let inRelevantSection = false;
  
  // 優先的に抽出するセクション名
  const prioritySections = [
    '実践的なTips', '実践的な活用', 'よくある失敗例', 'よくある落とし穴',
    '対処法', '解決策', '具体的な', 'ポイント', '押さえるべき',
    'コツ', '方法', '手順', 'チェックリスト'
  ];
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const lineLower = line.toLowerCase();
    
    // 見出しを検出
    if (line.match(/^#{1,3}\s+/)) {
      // 前のセクションを保存
      if (inRelevantSection && currentSection.length > 0) {
        importantSections.push(currentSection.join('\n'));
      }
      
      currentSection = [line];
      
      // 優先セクションかチェック
      inRelevantSection = prioritySections.some(section => 
        lineLower.includes(section.toLowerCase())
      ) || lineLower.includes(queryLower);
    } else if (inRelevantSection) {
      currentSection.push(line);
    }
    
    // クエリに関連する内容は必ず含める
    if (lineLower.includes(queryLower) && !inRelevantSection) {
      // 前後の文脈も含める
      const contextStart = Math.max(0, i - 2);
      const contextEnd = Math.min(lines.length - 1, i + 2);
      const context = lines.slice(contextStart, contextEnd + 1).join('\n');
      importantSections.push(context);
    }
  }
  
  // 最後のセクションを保存
  if (inRelevantSection && currentSection.length > 0) {
    importantSections.push(currentSection.join('\n'));
  }
  
  // 重要なセクションがない場合は、コンテンツの最初の部分を返す
  if (importantSections.length === 0) {
    return content.substring(0, 1500) + (content.length > 1500 ? '\n\n...' : '');
  }
  
  return importantSections.join('\n\n');
}

// 簡易的な回答生成（フォールバック用）
function generateSimpleResponse(query) {
  const responses = {
    '納期': '納期が遅れそうな場合は、早めにクライアントに連絡し、代替案を提示することが大切です。',
    'フィードバック': '効果的なフィードバックは具体的で建設的に行い、改善点を明確に伝えることが重要です。',
    'デザイナー': 'デザイナーの強みを理解し、適材適所のアサインと成長機会の提供が大切です。',
    '品質': '品質チェックはラフ段階、完成段階、納品前の3段階で行うことが重要です。',
    '商談': '商談では相手のニーズを深く理解し、Win-Winの関係を構築することが大切です。'
  };
  
  for (const [key, response] of Object.entries(responses)) {
    if (query.includes(key)) {
      return response;
    }
  }
  
  return `${query}についてお答えします。一般的には、相手の立場を理解し、明確なコミュニケーションを心がけることが重要です。`;
}