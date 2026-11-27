# ShareGo IG 經營規則（sharego.club）

帳號：Instagram **sharego.club**（Windsor connector `instagram`，account id `17841414094147682`）
顯示名稱：ShareGo客帶客－讓熟客幫你帶新客｜經營者：明哲 MOMO（ShareGo 會員導入顧問）
定位：門店老闆的 LINE 會員經營筆記。受眾＝餐飲、美業、醫美、藥局零售、服務業老闆與店長。

## 發文節奏（台北時間，每週二、四、六晚上）
| 星期 | 欄位 | 形式 |
|---|---|---|
| 二 | 做法／觀念 | 輪播 5～7 張（含 cover 與 cta） |
| 四 | 產業 or 節慶檔期 | 輪播 5～7 張 |
| 六 | 互動 | 選選看（quiz→answer）、找錯誤、勾勾看自我檢查；或單張金句／觀念圖（1 張，用 create_image_post） |
- 節慶題要在節日前 7～14 天發，讓老闆有時間準備。

## 品牌與用詞（硬規則）
- IG 上**不提 Mecango、屹登、黑快馬**，也不寫「ShareGo 系統」。功能一律說「會員系統」「LINE 會員系統」「系統」。
- 作者自稱「明哲 MOMO，ShareGo 會員導入顧問」。
- 同義詞：LINE 官方帳號（可帶 LINE OA、官方 LINE）；會員裂變／推薦好友（MGM）。
- 不寫補助金額、不點名或貶低競品、不談金融保險理財、不寫無法驗證的成效數字。數字只能用網站已有、且有來源的事實（例如網站 pricing、line-member-guide 頁）。
- **還沒有自己的 LINE 官方帳號**：CTA 一律導「個人檔案連結」（網站完整文章、方案試算），或「留言／私訊告訴我」。不要寫「加 LINE 拿入會禮」。等 MOMO 有自己的官方帳號後再改此條。
- 語氣：像跟老闆聊天，具體、短句、給可以照做的做法。每張字少，一張一個重點。

## 圖卡製作
1. 寫 `_ops/ig/posts/<YYYY-MM-DD>-<topic-id>.json`（格式見下方或範例 2026-12-01-referral-reward.json、2026-11-28-quiz-birthday.json）。
2. `python3 _ops/ig/build.py <slug>` → 輸出 `ig/<slug>/01.jpg…` 和 `preview.jpg`；若 `overflow_slides` 非空（exit 2）代表文字超出，刪字後重做。
3. 用 Read 打開 preview.jpg 親眼檢查：字有沒有重疊、斷行是否奇怪、有沒有錯字。
4. commit + push 到 main，等 GitHub Pages 上線（約 1～3 分鐘）再發文。

slide type：
- `cover` {title(可用 <em> <br>), sub, tag, coupon:[大字,小字]}（第一張）
- `points` {h, items:[[標題,說明]…] 最多 4 個, icon(選填，例如 "✓"), note}
- `wrong` {h, items:[[錯誤,說明]…] 最多 3 個}
- `steps` {h, items:[[2字圖示,標題,說明]…] 最多 4 個, note}
- `table` {h, head:[a,b], rows:[[a,b,是否強調]…] 最多 5 列, note}
- `check` {h, items:[…] 最多 5 個, note}（勾勾看）
- `big` {kicker, title, sub, text, tag}（單一重點大字）
- `quiz` {h, q, options:[A,B,C], note}；下一張 `answer` {answer, text}
- `cta` {h, text, items(同 steps，選填), url, note}（最後一張）
- 任一張可加 `"mint": true` 換淺綠底；`foot` 覆寫左下文字。

caption：開頭一句鉤子 → 3～5 行重點 → 一個互動問題（請留言）→「完整做法在個人檔案連結」→ 5 個 hashtag（中文為主，固定含 #LINE官方帳號）。≤ 2200 字元，不放網址（IG 不能點）。

## 發文（Windsor）
- 輪播：`execute_action` connector=`instagram` action=`create_carousel_post` account=`17841414094147682` params={image_urls:[…], caption}
- 單張：action=`create_image_post` params={image_url, caption}
- 發完把 media id 記到 `_ops/ig/log.md`，主題庫該題 status 改 `posted`。
- 已發貼文若有錯，**不要自己刪除**，通知 MOMO 決定。

## 成效追蹤（每週二那次順便做）
- `get_data` connector=`instagram` fields=[date, media_id, media_caption, media_type, media_reach, media_saved, media_shares, media_engagement, media_comments_count, media_follows, media_profile_visits]，date_preset=`last_30d`；以及 [date, followers_count, reach, profile_links_taps]。
- 算每則：觸及、收藏率（saved/reach）、分享、留言、帶來追蹤。寫到 `_ops/ig/report/YYYY-MM-DD.md`。
- 看哪個欄位／形式表現最好，調整接下來兩週的主題排序（把表現好的類型往前排），並在週報中說明調整。
- 留言：讀新留言（fields comment_id, comment_text, comment_username, comment_timestamp, media_id）。一般問題（行業、做法）可用 reply_to_comment 簡短友善回覆並邀請看個人檔案連結；問價格、要報價、抱怨、或不確定的，不回，列在通知裡給 MOMO。
