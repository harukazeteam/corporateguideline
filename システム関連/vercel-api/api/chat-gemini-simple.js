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
    const { message } = req.body;
    
    if (!message) {
      return res.status(400).json({ error: 'Message is required' });
    }

    // Gemini APIクライアントを初期化
    const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
    const model = genAI.getGenerativeModel({ model: 'gemini-2.5-flash' });

    // シンプルなプロンプトでテスト
    const result = await model.generateContent(`ユーザーの質問: ${message}\n\n簡潔に答えてください。`);
    const response = result.response.text();

    res.status(200).json({
      response,
      success: true
    });

  } catch (error) {
    console.error('Gemini API Error:', error);
    
    res.status(500).json({
      error: 'Internal server error',
      details: error.message,
      success: false
    });
  }
}