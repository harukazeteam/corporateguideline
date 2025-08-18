const OpenAI = require('openai');

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  const debugInfo = {
    method: req.method,
    hasApiKey: !!process.env.OPENAI_API_KEY,
    apiKeyLength: process.env.OPENAI_API_KEY ? process.env.OPENAI_API_KEY.length : 0,
    nodeVersion: process.version,
  };
  
  // OpenAIライブラリのテスト
  try {
    const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    });
    debugInfo.openaiInit = 'Success';
  } catch (error) {
    debugInfo.openaiInit = 'Failed';
    debugInfo.openaiError = error.message;
  }
  
  // ガイドラインデータの読み込みテスト
  try {
    const guidelines = require('../data/guidelines.json');
    debugInfo.guidelinesLoaded = true;
    debugInfo.guidelinesCount = guidelines.length;
  } catch (error) {
    debugInfo.guidelinesLoaded = false;
    debugInfo.guidelinesError = error.message;
  }
  
  // 簡単なOpenAI APIテスト（GETリクエストの場合のみ）
  if (req.method === 'GET' && process.env.OPENAI_API_KEY) {
    try {
      const openai = new OpenAI({
        apiKey: process.env.OPENAI_API_KEY,
      });
      
      const completion = await openai.chat.completions.create({
        model: 'gpt-3.5-turbo',
        messages: [{ role: 'user', content: 'Say "API is working"' }],
        max_tokens: 10,
      });
      
      debugInfo.apiTest = 'Success';
      debugInfo.apiResponse = completion.choices[0].message.content;
    } catch (error) {
      debugInfo.apiTest = 'Failed';
      debugInfo.apiError = error.message;
    }
  }
  
  res.status(200).json(debugInfo);
}