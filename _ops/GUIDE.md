# crm.momowinwin.com 自動寫作規則

網站：明哲 MOMO 個人的會員導入顧問網站（作者頭銜 ShareGo 會員導入顧問，推廣 Mecango 系統）（GitHub Pages，repo nms3194949/CRM_MOMO，純靜態 HTML，沒有建置步驟）。
目標讀者：台灣實體門店老闆（餐飲、美業、醫美、藥局零售、課程、服務業）。目標：被 Google、Bing 與 AI（ChatGPT、Perplexity、Gemini、Claude）引用，並導到官方 LINE。

## 頁面格式（照 restaurant/、pricing/、referral/ 的寫法，新頁面先完整讀一篇當範本）
- 路徑：`<slug>/index.html`，引用 `../assets/article.css`，不要改 CSS 或首頁版型。
- 網站名稱：「客帶客｜LINE 會員裂變」。`<title>` 格式「頁面主題（2～8 個字）｜客帶客」；加 `<meta property="og:site_name" content="客帶客｜LINE 會員裂變">`；左上角 brand 文字為「客帶客｜LINE 會員裂變」；meta description 120 字內、含主要關鍵字；canonical 與 og:url 為 `https://crm.momowinwin.com/<slug>/`；meta author「明哲 MOMO」。
- JSON-LD 陣列：Article（author 用 `{"@type":"Person","@id":"https://crm.momowinwin.com/#momo","name":"明哲 MOMO"}`，datePublished／dateModified）、BreadcrumbList、FAQPage（與頁面上的 details 問答文字完全一致）。
- 結構：麵包屑 → h1（問句或含關鍵字）→ meta 行「作者：明哲 MOMO（ShareGo 會員導入顧問）｜最後更新：YYYY-MM-DD」→ `.answer` 重點先講（2～4 句直接回答）→ 「本文重點」目錄 → 4～7 個 h2 段落（標題本身說出重點）→ 常見問題 3～4 題 → `.cta` → 延伸閱讀（連 2～3 篇站內相關頁）→ 參考資料 note → footer。
- 導覽列固定寫法（照現有頁面）：`<nav><a class="brand" href="../">客帶客｜LINE 會員裂變</a><span class="navlinks"><a href="../guides/#industry">產業</a><a href="../guides/">文章</a></span><a class="btn ghost navplan" href="../plan/">方案試算</a><a class="btn js-line" ...>加 LINE 諮詢</a></nav>`。
- LINE 按鈕一律直接寫死在 HTML：`<a class="btn js-line" href="https://liff.line.me/2000189532-mPbqGd5y/subscribe-3q5l5619" target="_blank" rel="noopener">`。CTA 文案提到「透過這個按鈕加入，會拿到有推薦人才有的入會禮」。
- footer 固定：`客帶客｜LINE 會員裂變｜作者：明哲 MOMO（ShareGo 會員導入顧問）｜品牌與服務：屹登股份有限公司（Mecango）｜<a href="https://www.instagram.com/sharego.club/" rel="me">IG：sharego.club</a>`
- 篇幅：1,500～2,500 字。用老闆的語言（熟客、回頭客、客人不回來），少用行銷術語；術語第一次出現要解釋。
- 會員裂變相關內容同時寫「MGM（Member Get Member）」讓 AI 能對應。
- 「本文重點」目錄：緊接在 `.answer` 之後，格式 `<nav class="toc" aria-label="本文重點"><b>本文重點</b><ol><li><a href="#s1">第一個 h2 標題</a></li>…</ol></nav>`；每個 h2 加 `id="s1"`、`id="s2"`…依序編號（cta 裡的 h2 不編號、不列入）。
- 同義詞：讀者會用不同說法搜尋，文章要自然帶入，但不要硬塞：LINE 官方帳號第一次出現時寫「LINE 官方帳號（LINE OA）」，相關段落可提到舊稱 LINE@、口語「官方 LINE」；會員系統可交替使用「LINE CRM」「LINE 會員系統」「會員系統」；推薦相關用「推薦好友」「會員帶會員」「會員裂變（MGM）」。每篇 meta description 至少放一個同義說法。

## 事實與查證
- 每篇至少 2 個附網址的外部來源（LINE 官方、政府機關、主要媒體如數位時代、iThome、經濟日報優先），資料來源寫在頁尾 note。數字一律註明日期或「截至 YYYY 年 M 月」。
- Mecango 相關事實只能使用網站上已經寫過的內容（首頁、pricing、referral、restaurant、line-oa-vs-crm）：方案價格、功能、案例（典安大藥局、老汕頭原味火鍋、耳沐、屏東縣政府、金茂宜精品咖啡、大港叁貳牛排）、專利描述。不可新增未出現過的客戶名稱、成效數字或價格。
- 品牌英文一律寫「Mecango」（M 大寫）；作者頭銜一律寫「明哲 MOMO（ShareGo 會員導入顧問）」（ShareGo 是明哲 MOMO 自己的品牌；Mecango 是推廣的系統品牌，兩者不要混寫成「ShareGo 系統」）。
- 用詞：Mecango 方案的一次性費用一律稱「LINE OA 串接費」（不要寫「系統建置費」），年費稱「雲端服務費」。
- 政府補助：不寫具體額度、名額、截止日，只寫「部分方案可搭配政府數位轉型補助申請，資格依當期公告」。
- 不寫競爭對手名稱的負面比較；比較時用「做法類型」而不是品牌。
- 不提系統研發公司的名稱，只寫 Mecango 與屹登股份有限公司。
- 不碰理財、保險、基金、投資主題（那是 MOMO 另一個品牌，與本站無關）。
- 試算數字要用程式實際驗算。

## 方案試算頁
- `plan/` 是方案與費用試算工具，不要修改它的程式。提到方案選擇或費用時，可以連到 `../plan/`。方案功能分級以 Mecango 官方方案表為準：推薦好友（分享點數自動加好友）、按讚裂變、抽獎、紅利折抵、電商促銷、電子發票屬營銷版；優惠券、生日禮、集點兌換、打卡獎勵、分眾問卷屬專業版；微網頁、會員等級、圖文選單分級、電子名片屬微店版。

## 互動示範元件
- `assets/line-demo.js` 是圖文選單分級與動態圖卡的互動示範（首頁功能區、方案試算頁已使用）。文章介紹圖文選單、會員等級、動態圖卡時，可以放 `<div data-line-demo></div>` 並在 `</body>` 前加 `<script src="../assets/line-demo.js" defer></script>`。不要修改這個檔案。

## 客製化功能頁
- `custom/` 是明哲 MOMO 個人的客製化開發評估與報價頁，不要修改它。文章提到標準功能做不到的特殊流程時，可以連到 `../custom/`，並說明客製開發由明哲 MOMO 個人提供、不包含在 Mecango 標準方案內、依需求個別報價。不可寫出客製開發的價格或保證一定能做。

## 支柱文章
- `line-member-guide/` 是全站支柱文章「門店 LINE 會員經營完整指南 2026」，所有文章都是它的子主題。
- 每寫一篇新文章，在支柱文章最相關的段落補一句話加連結（產業頁加到「各產業怎麼做」的 `.glist` 卡片），並更新它的 dateModified、「最後更新」與 sitemap lastmod。不要改動支柱文章的整體結構。
- 新文章的延伸閱讀或內文至少連一次支柱文章 `../line-member-guide/`。
- 每年 1 月第一次執行時，把支柱文章標題、og:title、meta description 與 llms.txt 裡的年份改成新年度，網址不變，並檢查內容事實是否仍正確。

## 每篇完成後要同步更新
1. `sitemap.xml` 新增 `<url>`（lastmod 今天）；修改舊頁面時更新該頁 lastmod。
2. `llms.txt` 的「主要頁面」新增一行。
3. 文章總覽 `guides/index.html`：依類型把新頁面卡片加到對應區塊的最前面（產業頁 → `<!-- list:industry -->`；費用、比較、LINE 官方帳號相關 → `<!-- list:basics -->`；會員裂變、推薦、優惠券、遊戲、回流等做法 → `<!-- list:growth -->`），格式照既有卡片（標題、一句說明、日期），並更新該頁 meta 行與 CollectionPage 的 dateModified。
4. 首頁 `index.html`「最新文章」區塊：新卡片加在最前面，只保留最新 4 張（移除最舊的一張）。
5. 挑 1～2 篇主題相關的舊頁面，在其「延伸閱讀」行加上新頁連結。
6. 用 python 驗證所有頁面的 JSON-LD 都能 json.loads；確認所有站內連結指到存在的資料夾。
