# LINE Sticker Splitter (LINE 貼圖自動切割工具)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)

這是一個專為 LINE 貼圖創作者設計的網頁版工具，能夠一鍵將 4x4 的貼圖大圖切割成符合 LINE 官方規範的獨立檔案，並自動產生必要的附屬圖片。

## 🚀 立即使用
[**點擊此處開啟工具**](https://zhangs1124.github.io/py-sticker-splitter/)

## ✨ 核心功能
- **自動切割**：將原始圖片精確切割為 4x4 網格。
- **LINE 規範強制相容**：
    - 自動調整尺寸至最大 **370x320 px**。
    - 強制轉換寬高為**偶數**（LINE 官方強烈建議）。
- **自動產生附屬圖**：
    - `main.png` (240x240 px)：主要縮圖。
    - `tab.png` (96x74 px)：聊天室分頁圖。
- **精確調整控制**：
    - **全域內距 (Padding)**：調整所有貼圖的留白。
    - **分列位移 (X/Y Offset)**：支援每一列獨立微調位置，解決不對齊問題。
- **智慧去背**：
    - **自動去除純白背景**：一鍵將背景轉為透明。
    - **容差值設定**：可調整去背強度，處理近白色的雜訊。
- **序列命名**：可自訂啟始編號（如從 01、09 或 13 開始），自動按順序命名。
- **離線可用**：基於瀏覽器 Canvas 技術，圖片不經過伺服器，保護創作隱私。

## 🛠️ 如何使用
1. 開啟[執行網址](https://zhangs1124.github.io/py-sticker-splitter/)。
2. 點擊上傳或直接拖放您的貼圖大圖。
3. 調整左側面板參數（內距、位移、編號、去背等）。
4. 在右側預覽確認無誤後。
5. 點擊 **「打包下載 (ZIP)」**。
6. 將解壓縮後的檔案上傳至 [LINE Creators Market](https://creator.line.me/)。

## 📄 授權條款
本專案採用 MIT 授權條款。
