# 医療カンファレンス・セミナーウェブサイト

データ駆動型のイベント管理システム

## 概要

このウェブサイトは、医療関連のカンファレンスやセミナー情報を管理・表示するためのシステムです。イベントデータはJSON形式で管理され、JavaScriptで動的に表示されます。

## ファイル構成

```
miyakohp.github.io-trial/
├── index.html              # メインHTMLファイル（データ駆動型）
├── events.json             # イベントデータ（JSON形式）
├── add_event.py            # イベント追加スクリプト
├── pdfs/                   # PDFチラシ保存ディレクトリ
├── icals/                  # iCalファイル保存ディレクトリ
└── README.md               # このファイル
```

## イベントの追加方法

### 方法1: add_event.pyスクリプトを使用

```bash
python3 add_event.py \
  --id "20251215_example" \
  --date "2025-12-15" \
  --time "18:30-19:30" \
  --title "イベント名" \
  --organizer "主催者名" \
  --format "オンライン" \
  --location "場所（オプション）" \
  --pdf "pdfs/20251215_example.pdf" \
  --ical "icals/20251215_example.ics"
```

### 方法2: events.jsonを直接編集

`events.json`ファイルを開き、以下の形式でイベントを追加します:

```json
{
  "id": "20251215_example",
  "date": "2025-12-15",
  "time": "18:30-19:30",
  "title": "イベント名",
  "organizer": "主催者名",
  "format": "オンライン",
  "location": "",
  "pdf": "pdfs/20251215_example.pdf",
  "ical": "icals/20251215_example.ics"
}
```

## デプロイ方法

```bash
# 変更をコミット
git add events.json pdfs/ icals/
git commit -m "Add new event: イベント名"

# GitHubにプッシュ
git push origin main
```

GitHub Pagesが自動的に更新されます（1-2分程度）。

## パスワード認証

ウェブサイトはパスワードで保護されています。
パスワード: `miyako69229090`

パスワードを変更する場合は、`index.html`の以下の行を編集してください:

```javascript
const correctPassword = "miyako69229090";
```

## バックアップ

### 元のバージョンに戻す方法

データ駆動型に移行する前のバージョンに戻す場合:

```bash
# タグから復元
git checkout v1.0-before-migration

# または、バックアップブランチから復元
git checkout backup-original
```

## トラブルシューティング

### イベントが表示されない

1. ブラウザのコンソールでエラーを確認
2. `events.json`のJSON形式が正しいか確認
3. ブラウザのキャッシュをクリア

### PDFやiCalファイルが見つからない

- ファイルパスが正しいか確認
- ファイルがGitHubにプッシュされているか確認

## システムの特徴

### データ駆動型アーキテクチャ

- **index.htmlは常に軽量**: イベントデータはJSONで管理
- **簡単な追加**: JSONに1エントリ追加するだけ
- **自動ソート**: 日付順に自動的にソート
- **月別グループ化**: 自動的に月ごとに表示

### 今後の拡張可能性

- イベント検索機能
- カテゴリフィルター（主催者別、形式別）
- 過去イベントの自動アーカイブ
- カレンダー表示
- RSS配信

## 更新履歴

- 2025-11-02: データ駆動型システムに移行
- 2025-10-30: 11月イベント追加
- 2025-10-XX: 初版リリース
