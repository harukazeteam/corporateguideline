# Vercelデプロイ詳細ガイド

## 事前準備

1. **Vercelアカウント作成**
   - https://vercel.com にアクセス
   - 「Sign Up」をクリック
   - GitHubアカウントでサインアップ（推奨）

2. **OpenAI APIキー取得**
   - https://platform.openai.com にアクセス
   - アカウント作成またはログイン
   - 「API Keys」から新しいキーを作成
   - キーをコピー（一度しか表示されません！）

## デプロイ手順

### 1. Vercel CLIをインストール

```bash
npm i -g vercel
```

### 2. vercel-apiディレクトリに移動

```bash
cd /Users/ogatahisashi/Library/CloudStorage/GoogleDrive-harukazeteam01@gmail.com/My Drive/HarukazeDatabase/Dynamic Knowledge/toB knowledge/ガイドラインプロジェクト/vercel-api
```

### 3. 初回デプロイ

```bash
vercel
```

以下の質問に答えます：

```
? Set up and deploy "~/vercel-api"? [Y/n] → Y
? Which scope do you want to deploy to? → 自分のアカウントを選択
? Link to existing project? [y/N] → N
? What's your project's name? → harukaze-guideline-api
? In which directory is your code located? → ./ （そのままEnter）
? Want to override the settings? [y/N] → N
```

### 4. 環境変数の設定

デプロイ完了後、環境変数を設定：

```bash
vercel env add OPENAI_API_KEY
```

以下のように入力：
```
? What's the value of OPENAI_API_KEY? → [OpenAIのAPIキーを貼り付け]
? Add OPENAI_API_KEY to which Environments? → Production, Preview, Development（全て選択）
```

### 5. 本番環境へ再デプロイ

環境変数を反映させるため：

```bash
vercel --prod
```

### 6. デプロイ完了確認

デプロイが完了すると、URLが表示されます：
```
🎉  Production: https://harukaze-guideline-api.vercel.app [コピー済み]
```

## フロントエンドの更新

### 1. テンプレートファイルを編集

`site_generator/_templates/page_light_with_ai.html`の1077行目付近を更新：

```javascript
// 変更前
const apiUrl = window.location.hostname === 'localhost' 
    ? 'http://localhost:3000/api/chat' 
    : 'https://harukaze-guideline-api.vercel.app/api/chat';

// 変更後（実際のURLに置き換え）
const apiUrl = window.location.hostname === 'localhost' 
    ? 'http://localhost:3000/api/chat' 
    : 'https://[あなたのプロジェクト名].vercel.app/api/chat';
```

### 2. サイトを再生成

```bash
cd ../site_generator
python3 generate_auto.py
```

### 3. GitHubにプッシュ

```bash
git add -A
git commit -m "Update API URL for production"
git push
```

## 動作確認

1. GitHub Pagesでサイトを開く
2. AIチャットボタンをクリック
3. 質問を入力して送信
4. OpenAI APIからの回答が表示されることを確認

## トラブルシューティング

### CORSエラーが出る場合

`vercel.json`のCORS設定を確認。必要に応じて特定のドメインのみ許可：

```json
{
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        { "key": "Access-Control-Allow-Origin", "value": "https://hisashi0001.github.io" }
      ]
    }
  ]
}
```

### APIキーエラーが出る場合

```bash
vercel env ls  # 環境変数を確認
vercel env rm OPENAI_API_KEY  # 一旦削除
vercel env add OPENAI_API_KEY  # 再設定
vercel --prod  # 再デプロイ
```

### 料金について

- Vercel: 無料枠で十分（月100GBの帯域幅）
- OpenAI: 使用量に応じて課金（gpt-3.5-turboは安価）
  - 目安: 1000リクエストで約$1-2程度

## セキュリティ注意事項

- OpenAI APIキーは絶対に公開しない
- フロントエンドのコードにAPIキーを含めない
- 必要に応じてレート制限を実装