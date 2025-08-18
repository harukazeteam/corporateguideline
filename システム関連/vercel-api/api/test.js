export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  res.status(200).json({ 
    message: 'API is working!',
    env: process.env.OPENAI_API_KEY ? 'API key is set' : 'API key is NOT set',
    method: req.method,
    timestamp: new Date().toISOString()
  });
}