# 行きたい店リスト（ittemitai-mise）

オーナーの「行ってみたい飲食店」をスマホで見るためのページ。GitHub Pages で公開している。
公開URL：https://m8tksgk-pixel.github.io/ittemitai-mise/

- `data.json` … 店のデータ（正本）。アプリはこれを読むだけ
- `index.html` … 画面。`sw.js` … 電波がないときの控え。`make_icon.py` … アイコン作成

**このリポジトリは公開されている。** 自宅の場所が分かる言葉（「自宅」「家から」「同じ町内」など）や個人情報は data.json に書かない。

## 店を追加してと頼まれたとき（食べログ・公式サイト・SNSのURLなど）

- 「追加して」と言われていれば確認なしで追加。リンクだけ貼られた場合は「行きたい店リストに追加しますか？」と先に聞く

1. 貼られたページ（食べログ・公式サイト・Instagram など）を読み、次を埋める。**空欄を残さないよう、貼られたページに無い項目は自分で調べて補う**（食べログならInstagram・X・公式サイト、Instagramなら食べログなど）。調べても見つからない項目だけ空文字にする（推測で埋めない）
   - `name` 店名 / `genre` ジャンル / `area`（例「橿原・久米町」「大和高田」「奈良市・ならまち」）/ `address` / `phone`
   - `tabelogUrl` / `websiteUrl` / `instagramUrl` / `xUrl`
   - `businessHours` / `closedDays` / `needsReservation`（予約必須なら true）/ `reservationNote`
   - `parkingInfo`（例「駐車場あり（10台）」「専用なし」）/ `carSuitability`（「車向き」「車可」「車不向き」のどれか）
   - `byCar` / `byTrain` / `byWalk`（true/false。徒歩はオーナーが言った時だけ true）/ `accessNote`（最寄り駅から徒歩○分など）
   - `photoUrl` … **必ず探して入れる**（空だとアプリに写真が出ない）。食べログのページの `og:image`（例 `https://tblg.k-img.com/resize/640x640c/restaurant/images/Rvw/390082/7e38….jpg`）を見つけ、`https://tblg.k-img.com/restaurant/images/Rvw/{番号}/640x640_rect_{ファイル名}.jpg` の形に直して入れる。`?` 以降の付いた URL と `http:` で始まる URL（スマホで表示されない）は使わない。どうしても取れない時だけ空にして、そのことをオーナーに伝える
   - `comment` … オーナーが感想を書いた時だけ。`visited` … 普通は false
   - 専用駐車場がなく近くのパーキングが分かる場合だけ `parkingMapsQuery`（例「タイムズ○○ 住所」）
   - `list` … どのタブに出すか。「行きたい店」タブは省略（または `"want"`）。朝に行ける店・歩いて行けるふだん使いの店として頼まれたら `"daily"`（アプリの「朝・徒歩圏」タブに出る）
2. `id` は今ある最大の id + 1
3. 同じ店（tabelogUrl か店名＋住所が一致）が既にあれば、追加せずにそのことを伝える
4. data.json の末尾に1行1店の形で足し、JSON として壊れていないか確かめる
5. main ブランチにそのまま commit して push する（Pages に1〜2分で反映される）。コミットメッセージは「店を追加：店名」
6. オーナーへは「追加した店名・ジャンル・エリア・営業時間・定休日」を短く返し、埋められなかった項目があれば書く

## そのほかの依頼
- 「行った」「コメント変更」「削除」なども data.json を直して push する
- アプリの「変更を書き出す」で貼られた JSON を受け取ったら、id ごとに data.json へ反映する（スマホ側にしかない変更を取り込む）
- 名前やファイル名に「ikitai」は使わない（「生きたい」と読めるのをオーナーが嫌う）
