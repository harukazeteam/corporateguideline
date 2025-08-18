module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  const debugInfo = {
    method: req.method,
    hasGeminiKey: !!process.env.GEMINI_API_KEY,
    geminiKeyLength: process.env.GEMINI_API_KEY ? process.env.GEMINI_API_KEY.length : 0,
    nodeVersion: process.version,
  };
  
  // ライブラリのインポートテスト
  try {
    const { GoogleGenerativeAI } = require('@google/generative-ai');
    debugInfo.libraryImport = 'Success';
    
    if (process.env.GEMINI_API_KEY) {
      const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
      const model = genAI.getGenerativeModel({ model: 'gemini-2.5-flash' });
      debugInfo.modelInit = 'Success';
      
      // 簡単なテスト
      if (req.method === 'GET') {
        try {
          const result = await model.generateContent('Say "Gemini is working"');
          debugInfo.testResponse = result.response.text();
        } catch (error) {
          debugInfo.testError = error.message;
        }
      }
    }
  } catch (error) {
    debugInfo.libraryImport = 'Failed';
    debugInfo.importError = error.message;
  }
  
  res.status(200).json(debugInfo);
}