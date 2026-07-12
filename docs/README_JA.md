<div align="center">

# 📈 AI株分析システム

[![GitHub stars](https://img.shields.io/github/stars/ZhuLinsen/daily_stock_analysis?style=social)](https://github.com/ZhuLinsen/daily_stock_analysis/stargazers)
[![CI](https://github.com/ZhuLinsen/daily_stock_analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/ZhuLinsen/daily_stock_analysis/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Ready-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://hub.docker.com/r/zhulinsen/daily_stock_analysis)

<p align="center">
  <img src="https://trendshift.io/api/badge/trendshift/repositories/18527/daily?language=Python" alt="#1 Python Repository Of The Day | Trendshift" width="250" height="55"/>&nbsp;<a href="https://hellogithub.com/repository/ZhuLinsen/daily_stock_analysis" target="_blank"><img src="https://api.hellogithub.com/v1/widgets/recommend.svg?rid=6daa16e405ce46ed97b4a57706aeb29f&claim_uid=pfiJMqhR9uvDGlT&theme=neutral" alt="Featured｜HelloGitHub" width="230" /></a>
</p>

> 🤖 AI大規模言語モデルを活用した、A株/香港株/米国株/日本株/韓国株/台湾株のウォッチリスト株（自选股）のスマート分析システム。毎日自動で分析を行い、「意思決定ダッシュボード」を企業微信（WeChat Work）/飛書（Feishu）/Telegram/Discord/Slack/メールにプッシュ通知します。

[**プロダクトプレビュー**](#-プロダクトプレビュー) · [**機能・特徴**](#-機能特徴) · [**クイックスタート**](#-クイックスタート) · [**通知サンプル**](#-通知サンプル) · [**ドキュメントセンター**](./INDEX.md) · [**完全ガイド**](./full-guide.md)

日本語 | [简体中文](../README.md) | [English](README_EN.md) | [繁體中文](README_CHT.md)

</div>

## 💖 スポンサー (Sponsors)
<div align="center">
  <p align="center">
    <a href="https://open.anspire.cn/dsa?share_code=QFBC0FYC" target="_blank"><img src="./assets/anspire.png" alt="Anspire Open ワンストップ型モデル＆検索サービス" width="300" height="141" style="width: 300px; height: 141px; object-fit: contain;"></a>
    <a href="https://serpapi.com/baidu-search-api?utm_source=github_daily_stock_analysis" target="_blank"><img src="./assets/serpapi_banner_zh.png" alt="検索エンジンから实时の金融ニュースデータを簡単に取得 - SerpApi" width="300" height="141" style="width: 300px; height: 141px; object-fit: contain;"></a>
  </p>
</div>


## 🖥️ プロダクトプレビュー

<p align="center">
  <img src="assets/readme_workspace_tour_20260510.gif" alt="DSA Web ワークスペースのデモ" width="720">
</p>

## ✨ 機能・特徴

| 機能 | 詳細・対象範囲 |
|------|------|
| AI意思決定レポート | 主要結論、スコアリング、トレンド、売買ポイント、リスク警告、材料・触媒要因、アクションチェックリスト |
| 複数市場のデータ集約 | A株、香港株、米国株、日本株、韓国株、台湾株およびETFをカバー。株価、K線（ローソク足）、テクニカル指標、ニュース、適時開示・公告、ファンダメンタルズ、レポート補助データに対応。各市場のデータソースと機能の境界については、[市場サポート範囲](./market-support.md)をご参照ください。 |
| Web / デスクトップ ワークスペース | 手動分析、タスク進捗状況、過去のレポート、詳細なMarkdown、バックテスト、ポジション、設定管理、ライト/ダークテーマ |
| Agent式 投資戦略Q&A | マルチターン対話に対応。移動平均線、ちゃん論（纏論）、エリオット波動、トレンド、テーマ・ホットセクター、イベント駆動、グロース（成長性）、業績予想など15種類の組み込み戦略をサポート。Web / Bot / APIで利用可能。 |
| スマートインポート和補完 | 画像、CSV/Excel、クリップボードからのインポート。銘柄コード、名称、ピンイン、別名の補完に対応。 |
| 自動化とプッシュ通知 | GitHub Actions、Docker、ローカルのスケジュールタスク、FastAPIサービス、および企業微信（WeChat Work）/飛书（Feishu）/Telegram/Discord/Slack/メールによるプッシュ通知。 |

> 機能の詳細、フィールド定義、ファンダメンタルズP0タイムアウト設計、取引ルール、データソースの優先順位、Web/APIの動作については、[詳細な設定およびデプロイガイド](./full-guide.md)をご覧ください。

### 技術スタックとデータソース

| タイプ | サポート対象 |
|------|------|
| AIモデル | [Anspire](https://open.anspire.cn/dsa?share_code=QFBC0FYC)、[AIHubMix](https://aihubmix.com/?aff=CfMq)、Gemini、OpenAI互換、DeepSeek、通義千問、Claude、Ollama（ローカルモデル）など |
| マーケットデータ | [TickFlow](https://tickflow.org/auth/register?ref=WDSGSPS5XC)、AkShare、Tushare、Pytdx、Baostock、YFinance、Longbridge |
| ニュース検索 | [Anspire](https://open.anspire.cn/dsa/?share_code=QFBC0FYC)、[SerpAPI](https://serpapi.com/baidu-search-api?utm_source=github_daily_stock_analysis)、[Tavily](https://tavily.com/)、[Bocha (博查) 検索](https://open.bocha.cn/)、[Brave Search](https://brave.com/search/api/)、[MiniMax](https://platform.minimaxi.com/)、SearXNG |
| ソーシャル・センチメント | [Stock Sentiment API](https://api.adanos.org/docs)（Reddit / X / Polymarket、米国株のみ、オプション） |

> プロジェクトにはデフォルトで AkShare、Baostock、YFinance などの無料データソースが組み込まれており、設定なし（ゼロ構成）ですぐに実行できます。ただし、無料ソースは上流のAPI制限や仕様変更、ネットワークの変動の影響を受けるため、動作の安定性は保証されません。長期間のスケジュール実行、バッチ分析、またはより安定した株価データの取得には、TickFlow、Tushare、Longbridge などのトークン認証が必要なデータソースの設定を推奨します。対象市場、GitHub Actionsでの設定マッピング、フォールバックのルールは [データソース設定](./full-guide.md#数据源配置) をご覧ください。

## 🚀 クイックスタート

### 方法1：[GitHub Actions（推奨）](https://www.bilibili.com/video/BV11FEb66EXG/)

> 5分でデプロイ完了。サーバー不要、完全無料。


#### 1. リポジトリをフォークする

右上の `Fork` ボタンをクリックします（ついでに Star⭐ を押して応援していただけると励みになります）。

#### 2. Secrets を設定する

`Settings` → `Secrets and variables` → `Actions` → `New repository secret`

**AIモデルの設定（少なくとも1つ必要）**

デフォルトでは、まずいずれかのモデルプロバイダーを選択し、APIキーを入力します。複数モデルの併用、画像認識、ローカルモデル、または高度なルーティングが必要な場合は、[LLM設定ガイド](./LLM_CONFIG_GUIDE.md)を参照してください。

| Secret名 | 説明 | 必須・推奨 |
|------------|------|:----:|
| `ANSPIRE_API_KEYS` | [Anspire](https://open.anspire.cn/dsa?share_code=QFBC0FYC) APIキー：1つのキーで世界中の主要な大規模言語モデルとウェブ検索を同時に有効化。本プロジェクトの新規ユーザーには35元相当の無料枠を提供（GLM5.2、GPTなどのモデルでキャンペーン実施中）。 | **推奨** |
| `AIHUBMIX_KEY` | [AIHubMix](https://aihubmix.com/?aff=CfMq) APIキー：1つのキーで主要な全モデルを切り替えて利用可能。中国国内からのアクセス制限もなし。本プロジェクト向けに10%割引を提供。 | **推奨** |
| `GEMINI_API_KEY` | Google Gemini API キー | オプション |
| `ANTHROPIC_API_KEY` | Anthropic Claude API キー | オプション |
| `OPENAI_API_KEY` | OpenAI互換 API キー（DeepSeek、通義千问なども対応） | オプション |
| `OPENAI_BASE_URL` / `OPENAI_MODEL` | OpenAI互換サービスを使用する際に入力 | オプション |

> OllamaはローカルやDockerでのデプロイに適しています。GitHub ActionsではクラウドAPIの使用を推奨します。

**通知チャネルの設定（少なくとも1つ必要）**

| Secret名 | 説明 |
|------------|------|
| `WECHAT_WEBHOOK_URL` | 企業微信（WeChat Work）ロボット |
| `FEISHU_WEBHOOK_URL` | 飛書（Feishu）ロボット |
| `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` | Telegram |
| `DISCORD_WEBHOOK_URL` | Discord Webhook |
| `SLACK_BOT_TOKEN` + `SLACK_CHANNEL_ID` | Slack Bot |
| `EMAIL_SENDER` + `EMAIL_PASSWORD` | メールプッシュ |

その他の通知チャンネル、署名検証、グループメール送信、Markdownから画像への変換などの設定は、[通知チャネル詳細設定](./full-guide.md#通知渠道详细配置)を参照してください。

**ウォッチリスト（自选股）の設定（必須）**

| Secret名 | 説明 | 必須・推奨 |
|------------|------|:----:|
| `STOCK_LIST` | ウォッチリストに入れる銘柄コード（例: `600519,hk00700,AAPL,7203.T,005930.KS,2330.TW`） | ✅ |

**ニュースソースの設定（推奨）**

ニュースソースは、市場のセンチメント、適時開示・公告、イベント、材料（触媒）分析の品質に大きく影響するため、少なくとも1つの検索サービスを設定することを強くお勧めします。

| Secret名 | 説明 | 必須・推奨 |
|------------|------|:----:|
| `ANSPIRE_API_KEYS` | [Anspire AI Search](https://open.anspire.cn/dsa?share_code=QFBC0FYC)：グローバルの世論・センチメント情報を集約。A株、米国株、香港株などのニュースや世論の検索に最適。同一キーで大容量AIモデルサービスと併用可能。本プロジェクトの新規ユーザーに35元相当の無料ポイントを提供。 | **推奨** |
| `SERPAPI_API_KEYS` | [SerpAPI](https://serpapi.com/baidu-search-api?utm_source=github_daily_stock_analysis)：検索エンジン結果の補強、リアルタイムの金融ニュースに最適。 | **推奨** |
| `TAVILY_API_KEYS` | [Tavily](https://tavily.com/)：汎用ニュース検索API。 | オプション |
| `BOCHA_API_KEYS` | [Bocha (博查) 検索](https://open.bocha.cn/)：中国語検索の最適化、AI要約をサポート。 | オプション |
| `BRAVE_API_KEYS` | [Brave Search](https://brave.com/search/api/)：プライバシー優先、米国株情報の補強。 | オプション |
| `MINIMAX_API_KEYS` | [MiniMax](https://platform.minimaxi.com/)：構造化された検索結果。 | オプション |
| `SEARXNG_BASE_URLS` | SearXNG自ビルドインスタンス：クォータ制限なし、プライベートデプロイに最適。 | オプション |

その他の検索ソース、ソーシャル・センチメント、デグレードルールについては、[検索サービス設定](./full-guide.md#搜索服务配置)をご覧ください。

**株価データソースの設定（オプション）**

> デフォルトでは AkShare、Baostock、YFinance などの無料データソースが使用されます。ログに表示される『未設定』の警告は動作に影響ありません。
> より安定した株価データを取得したい場合は、市場に応じて以下のSecretsを設定してください：

| Secret名 | 対象市場 | 説明 |
|------------|:--------:|------|
| `TUSHARE_TOKEN` | A株 | ヒストリカルデータの安定性向上 |
| `LONGBRIDGE_OAUTH_CLIENT_ID` + `LONGBRIDGE_OAUTH_TOKEN_CACHE_B64` | 香港株 / 米国株 | ボリュームレシオ（量比）、回転率（換手率）、PER（PE）などのデータを補完 |

> 詳細は [データソース設定](./full-guide.md#数据源配置) を参照してください。

#### 3. Actions を有効にする

`Actions` タブ → `I understand my workflows, go ahead and enable them` をクリックします。

#### 4. 手動テスト

`Actions` → `每日股票分析` → `Run workflow` → `Run workflow` をクリックします。

#### 完了

デフォルトでは**営業日の18:00（北京時間、日本時間19:00）**に自動的に実行されます。手動で実行することも可能です。デフォルトでは非取引日（中国/香港/米国の祝日を含む）には実行されません。強制実行、取引日チェック、レジューム機能などのルールについては [完全ガイド](./full-guide.md#定时任务配置) を参照してください。

### 方法2：[クライアント設定チュートリアル](https://www.bilibili.com/video/BV11FEb66Eyr/) / ローカル実行 / Docker デプロイ

```bash
# プロジェクトをクローン
git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis

# 依存関係のインストール
pip install -r requirements.txt

# 環境変数の設定
cp .env.example .env && vim .env

# 分析を実行
python main.py
```

よく使うコマンド：

```bash
python main.py --debug
python main.py --dry-run
python main.py --stocks 600519,hk00700,AAPL,2330.TW
python main.py --market-review
python main.py --schedule
python main.py --serve-only
```

> Dockerによるデプロイ、スケジュールタスク、クラウドサーバーからのアクセスについては [完全ガイド](./full-guide.md) を、デスクトップクライアントのビルド・パッケージングについては [デスクトップ端パッケージング説明](./desktop-package.md) を参照してください。

## 📱 通知サンプル

### 意思決定ダッシュボード
```
🎯 2026-02-08 意思決定ダッシュボード
合計3銘柄を分析 | 🟢買い:0 🟡様子見:2 🔴売り:1

📊 分析結果サマリー
⚪ 中钨高新(000657): 様子見 | スコア 65 | 強気
⚪ 永鼎股份(600105): 様子見 | スコア 48 | レンジ（横ばい）
🟡 新莱应材(300260): 売り | スコア 35 | 弱気

⚪ 中钨高新 (000657)
📰 重要情報の概要
💭 世論センチメント: 市場はAIテーマと業績の高成長に注目しており、センチメントは前向きです。ただし、短期的な利益確定売りや大口資金（主力）の流出圧力を消化する必要があります。
📊 業績予想: ニュース・世论情報によると、同社の2025年第3四半期累計業績は前年同期比で大幅に増加しており、ファンダメンタルズは堅調で、株価を支えています。

🚨 リスク警告:

リスク1：2月5日に大口資金が3億6300万元の大幅な売り越しを記録しており、短期的な売り圧力に警戒が必要です。
リスク2：株主集中度が35.15%と高く、株式が分散しているため、株価上昇時の抵抗が大きい可能性があります。
リスク3：ニュース内で過去のコンプライアンス違反や再編に関連するリスク警告が言及されており、注視する必要があります。

✨ 材料・触媒要因:

材料1：同社は市場からAIサーバー向けHDIの主要サプライヤーと位置付けられており、AI産業の発展から恩恵を受けています。
材料2：2025年第3四半期累計の非経常損益控除後純利益が前年同期比で407.52%暴騰しており、業績は非常に好調です。

📢 最新動向: 【最新ニュース】センチメント分析によると、同社はAI向けPCBマイクロドリルのリーディングカンパニーであり、世界のトップPCB/キャリアボードメーカーと深く提携しています。2月5日の大口資金の売り越しは3億6300万元で、今後の資金動向に注目する必要があります。

---
生成時刻: 18:00
```

### 相場全体の振り返り（大盤復盤）
```
🎯 2026-01-10 相場全体の振り返り

📊 主要指数
- 上海総合指数: 3250.12 (🟢+0.85%)
- 深圳成分指数: 10521.36 (🟢+1.02%)
- 創業板指数: 2156.78 (🟢+1.35%)

📈 市場概況
値上がり: 3920 | 値下がり: 1349 | ストップ高: 155 | ストップ安: 3

🔥 セクター動向
値上がり上位: インターネットサービス、文化メディア、小金属（マイナーメタル）
値下がり上位: 保険、航空・空港、太陽光発電設備
```

## ⚙️ 設定について

すべての環境変数、モデルプロバイダーの設定、通知チャネルの設定、データソースの優先順位、取引ルール、ファンダメンタルズP0設計、およびデプロイ手順の詳細については、[詳細な設定およびデプロイガイド](./full-guide.md)を参照してください。

## 🖥️ Web UI 画面

Webワークスペースでは、設定管理、タスク監視、手動分析、履歴レポート、詳細Markdownレポート、Agentによる銘柄相談、バックテスト、ポジション管理、スマートインポート、およびライト/ダークテーマを提供します。起動方法：

```bash
python main.py --webui
python main.py --webui-only
```

ブラウザで `http://127.0.0.1:8000` にアクセスして利用します。認証、スマートインポート、検索予測補完、過去レポートのコピー、クラウドサーバーからのアクセスなど詳細については、[ローカルWebUI管理画面](./full-guide.md#本地-webui-管理界面) を参照してください。

## 🤖 Agent式 投資戦略Q&A

有効なAI APIキーをどれか設定すると、Webの `/chat` ページで投資戦略Q&A（銘柄相談）が利用できるようになります。無効にしたい場合は `AGENT_MODE=false` に設定します。

- 移動平均線ゴールデンクロス、ちゃん論（纏論）、エリオット波動、上昇トレンド、テーマ・ホットセクター、イベント駆動、グロース（成長性）、業績予想などの組み込み戦略をサポート
- リアルタイム株価、K線、テクニカル指標、ニュース、リスク情報の参照に対応
- マルチターン対話、チャット履歴のエクスポート、通知チャネルへの送信、バックグラウンド実行に対応
- カスタム戦略ファイルとマルチエージェントオーケストレーション（実験的機能）に対応

> Agentの具体的なパラメータ、`skill`命名の互換性、マルチエージェントモード、予算保護（ガードレール）については、[完全ガイド](./full-guide.md#本地-webui-管理界面) および [LLM設定ガイド](./LLM_CONFIG_GUIDE.md) を参照してください。

## 🧩 関連プロジェクト (Related Projects)

> DSAは日常の分析レポート生成にフォーカスしています。下記の同シリーズの2つのプロジェクトは、それぞれ銘柄の選定、戦略検証、戦略進化をカバーしており、必要に応じて併用するのに適しています。現在は独立してメンテナンスされていますが、将来的にはDSAとの候補銘柄のインポート連携、バックテスト検証、レポートの連携などを検討していく予定です。

| プロジェクト | 位置付け・役割 |
|------|------|
| [AlphaSift](https://github.com/ZhuLinsen/alphasift) | マルチファクター銘柄選定と全市場スキャン。株式プールから候補銘柄を抽出するのに使用 |
| [AlphaEvo](https://github.com/ZhuLinsen/alphaevo) | 戦略のバックテストと自己進化。戦略ルールの検証、およびイテレーションによる戦略パラメータとポートフォリオの探索に使用 |

## 📬 お問い合わせとコラボレーション

<table>
  <tr>
    <td width="92" valign="top"><strong>コラボレーション用メール</strong></td>
    <td valign="top">
      <a href="mailto:zhuls345@gmail.com">zhuls345@gmail.com</a><br>
      プロジェクト相談、導入サポート、機能拡張
    </td>
    <td align="center" rowspan="3" valign="middle" width="148">
      <a href="http://xhslink.com/m/tU520DWCKT" target="_blank"><img src="./assets/xiaohongshu_tick.jpg" width="112" alt="小紅書QRコード"></a><br>
      <sub>小紅書（RED）でQRコードをスキャンしてフォロー</sub>
    </td>
  </tr>
  <tr>
    <td width="92" valign="top"><strong>小紅书 (RED)</strong></td>
    <td valign="top"><a href="http://xhslink.com/m/tU520DWCKT">小紅書でお待ちしております</a></td>
  </tr>
  <tr>
    <td width="92" valign="top"><strong>不具合・要望のフィードバック</strong></td>
    <td valign="top"><a href="https://github.com/ZhuLinsen/daily_stock_analysis/issues">Issueを送信</a></td>
  </tr>
</table>

## 📄 ライセンス

[MIT License](LICENSE) © 2026 ZhuLinsen

二次開発や引用を行う際は、本リポジトリをソースとして明記していただけますと幸いです。プロジェクトの継続的なメンテナンスへのご支援に感謝いたします。

## ⚠️ 免責事項

本プロジェクトは学習および研究目的のみで提供されており、いかなる投資アドバイスも構成しません。株式投資にはリスクが伴います。投資は慎重に行ってください。本プロジェクトの利用によって生じた一切の損失について、作者は責任を负いません。

---
