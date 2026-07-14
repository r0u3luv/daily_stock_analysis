# NVDA 日次分析のセットアップ

このフォークは `NVDA` の日本語レポートに設定済みです。GitHub Actions は平日 19:00（日本時間）に実行され、Actions タブからも手動実行できます。上流版の市場総評には日本語テンプレートがないため、中国語混入を防ぐ目的で市場総評は無効化しています。

## 登録が必要な Secrets

`Settings` → `Secrets and variables` → `Actions` → `Secrets` で、次の値を登録します。キーやメールのパスワードはリポジトリやこのファイルへ保存しません。

| Secret | 登録する値 |
| --- | --- |
| `LLM_GEMINI_API_KEY` | Gemini API キー |
| `LLM_OPENROUTER_API_KEY` | OpenRouter API キー |
| `EMAIL_SENDER` | 送信元メールアドレス |
| `EMAIL_PASSWORD` | SMTP のアプリパスワード／SMTP認証用パスワード |
| `EMAIL_RECEIVERS` | 配信先メールアドレス（自分宛なら `EMAIL_SENDER` と同じ値） |

Gemini を第一候補、OpenRouter を障害時の予備として順に試行します。OpenRouter のモデルは `google/gemini-2.5-flash` に設定済みです。

Gmail を使う場合、`EMAIL_PASSWORD` には通常のGoogleパスワードではなく、2段階認証を有効化したアカウントで発行したアプリパスワードを使ってください。

## 初回確認

Secrets を保存したら、`Actions` → `每日股票分析` → `Run workflow` を開き、`force_run` を有効にして `stocks-only` で実行します。メールが届けば定期実行も同じ設定で動作します。

## 公開レポート

分析が成功すると、最新の詳細レポート全文が GitHub Pages に公開されます。レポートには判断根拠、売買水準、リスク、確認項目が含まれる場合があります。Actionsログ、メールアドレス、認証情報は公開しません。レポートが生成されない、または空の場合は Pages の更新をスキップします。

これは投資助言ではありません。分析結果は投資判断の補助として扱ってください。
