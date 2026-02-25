# ソラトビコミックス - プロジェクトルール

## セッションログ（必須）
- 会話の終了時、または重要な作業を行った後は **`.claude/session_log.md`** に記録を追記すること
- 記録フォーマット: `## YYYY-MM-DD（Windows / Mac）` + 箇条書きで作業内容
- これにより Windows / Mac どちらのマシンで作業しても経緯を引き継げる
- セッション開始時は必ず `session_log.md` を読んで過去の作業内容を把握すること

## プロジェクト概要
- **ソラトビコミックス**: コミックPR事業のランディングページ
- GitHub Pages で公開: https://nodusun.github.io/soratobi-comics/
- X（旧Twitter）: @soratobicomics

## 技術構成
- 静的サイト（HTML + CSS）、フレームワークなし
- フォント: Noto Sans JP（Google Fonts）
- ホスティング: GitHub Pages

## ファイル構成
- `index.html` — メインページ
- `style.css` — スタイルシート
- `images/` — 画像素材（hero.png, service_*.png）
- `.claude/session_log.md` — セッションログ
- `.claude/settings.json` — Claude Code 許可設定
