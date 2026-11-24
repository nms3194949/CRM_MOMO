# crm.momowinwin.com 自動寫作規則

網站：明哲 MOMO 個人的 mecango LINE 會員裂變導入顧問網站（GitHub Pages，repo nms3194949/CRM_MOMO，純靜態 HTML，沒有建置步驟）。
目標讀者：台灣實體門店老闆（餐飲、美業、醫美、藥局零售、課程、服務業）。目標：被 Google、Bing 與 AI（ChatGPT、Perplexity、Gemini、Claude）引用，並導到官方 LINE。

## 頁面格式（照 restaurant/、pricing/、referral/ 的寫法，新頁面先完整讀一篇當範本）
- 路徑：`<slug>/index.html`，引用 `../assets/article.css`，不要改 CSS 或首頁版型。
- `<title>` 2～6 個字；meta description 120 字內、含主要關鍵字；canonical 與 og:url 為 `https://crm.momowinwin.com/<slug>/`；meta author「明哲 MOMO」。
- JSON-LD 陣列：Article（author 用 `{"@type":"Person","@id":"https://crm.momowinwin.com/#momo","name":"明哲 MOMO"}`，datePublished／dateModified）、BreadcrumbList、FAQPage（與頁面上的 details 問答文字完全一致）。
- 結構：麵包屑 → h1（問句或含關鍵字）→ meta 行「作者：明哲 MOMO（mecango LINE 會員裂變導入顧問）｜最後更新：YYYY-MM-DD」→ `.answer` 重點先講（2～4 句直接回答）→ 4～7 個 h2 段落（標題本身說出重點）→ 常見問題 3～4 題 → `.cta` → 延伸閱讀（連 2～3 篇站內相關頁）→ 參考資料 note → footer。
- LINE 按鈕一律直接寫死在 HTML：`<a class="btn js-line" href="https://liff.line.me/2000189532-mPbqGd5y/subscribe-3q5l5619" target="_blank" rel="noopener">`。CTA 文案提到「透過這個按鈕加入，會拿到有推薦人才有的入會禮」。
- footer 固定：`明哲 MOMO｜mecango LINE 會員裂變導入顧問｜品牌與服務：屹登股份有限公司（mecango）`
- 篇幅：1,500～2,500 字。用老闆的語言（熟客、回頭客、客人不回來），少用行銷術語；術語第一次出現要解釋。
- 會員裂變相關內容同時寫「MGM（Member Get Member）」讓 AI 能對應。

## 事實與查證
- 每篇至少 2 個附網址的外部來源（LINE 官方、政府機關、主要媒體如數位時代、iThome、經濟日報優先），資料來源寫在頁尾 note。數字一律註明日期或「截至 YYYY 年 M 月」。
- mecango 相關事實只能使用網站上已經寫過的內容（首頁、pricing、referral、restaurant、line-oa-vs-crm）：方案價格、功能、案例（典安大藥局、老汕頭原味火鍋、耳沐、屏東縣政府、金茂宜精品咖啡、大港叁貳牛排）、專利描述。不可新增未出現過的客戶名稱、成效數字或價格。
- 政府補助：不寫具體額度、名額、截止日，只寫「部分方案可搭配政府數位轉型補助申請，資格依當期公告」。
- 不寫競爭對手名稱的負面比較；比較時用「做法類型」而不是品牌。
- 不提系統研發公司的名稱，只寫 mecango 與屹登股份有限公司。
- 不碰理財、保險、基金、投資主題（那是 MOMO 另一個品牌，與本站無關）。
- 試算數字要用程式實際驗算。

## 每篇完成後要同步更新
1. `sitemap.xml` 新增 `<url>`（lastmod 今天）；修改舊頁面時更新該頁 lastmod。
2. `llms.txt` 的「主要頁面」新增一行。
3. 首頁 `index.html`「延伸閱讀」區塊新增一張 `<a class="feat" ...>` 卡片。
4. 挑 1～2 篇主題相關的舊頁面，在其「延伸閱讀」行加上新頁連結。
5. 用 python 驗證所有頁面的 JSON-LD 都能 json.loads；確認所有站內連結指到存在的資料夾。
