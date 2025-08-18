# Harukaze Guideline AI Chat API

HarukazeガイドラインのAIチャット機能を提供するVercel APIです。

## 機能

- ガイドラインの内容を学習したAIがユーザーの質問に回答
- 関連するガイドラインページの提案
- Markdownファイルの内容をベクトル検索

## セットアップ

### 1. 依存関係のインストール

```bash
npm install
```

### 2. 環境変数の設定

`.env.example`を`.env`にコピーして、OpenAI APIキーを設定：

```bash
cp .env.example .env
```

`.env`ファイルを編集：
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. ガイドラインデータの準備

```bash
npm run prepare-data
```

これにより、`data/guidelines.json`が生成されます。

### 4. ローカル開発

```bash
npm run dev
```

http://localhost:3000/api/chat でAPIが利用可能になります。

## デプロイ

### Vercelへのデプロイ

1. Vercelアカウントを作成（https://vercel.com）

2. Vercel CLIをインストール：
```bash
npm i -g vercel
```

3. プロジェクトをデプロイ：
```bash
vercel
```

4. 環境変数を設定：
```bash
vercel env add OPENAI_API_KEY
```

5. 本番環境にデプロイ：
```bash
vercel --prod
```

## API仕様

### POST /api/chat

リクエスト：
```json
{
  "message": "納期が遅れそうな時はどうすればいい？"
}
```

レスポンス：
```json
{
  "response": "納期遅延への対応について説明します...",
  "relatedPages": [
    {
      "title": "トラブルシューティング",
      "url": "troubleshooting.html",
      "category": "基本情報"
    }
  ],
  "success": true
}
```

## フロントエンドとの連携

HTMLファイルのJavaScriptで以下のように設定：

```javascript
const apiUrl = 'https://your-project.vercel.app/api/chat';
```

## 注意事項

- OpenAI APIの利用料金が発生します
- 月間の無料枠を超えると課金されます
- APIキーは絶対に公開しないでください

## トラブルシューティング

### CORSエラーが発生する場合

`vercel.json`でCORS設定を確認してください。

### データが更新されない場合

```bash
npm run prepare-data
vercel --prod
```

を実行してデータを再生成し、再デプロイしてください。