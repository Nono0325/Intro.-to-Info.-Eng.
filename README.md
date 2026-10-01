# 國立虎尾科技大學 - 資訊工程導論 課程全方位精華筆記
### Introduction to Information Engineering (NFU CSIE)

[![Course](https://img.shields.io/badge/Course-Intro%20to%20Info%20Eng-0052CC.svg)](https://github.com/Nono0325/Intro.-to-Info.-Eng.)
[![Textbook](https://img.shields.io/badge/Textbook-Brookshear%20CS%2013th%20Ed.-FF5722.svg)](https://www.pearson.com)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/Notes-Academic%20Study%20Guide-green.svg)](#)

本倉儲為**國立虎尾科技大學資訊工程系「資訊工程導論」**課程之完整、系統化學習筆記與實作代碼庫。內容深度整合授課投影片精髓、教科書 (*Computer Science: An Overview*, 13th Edition) 核心理論，並包含**詳細觀念解析**、**中英對照翻譯**、**專業術語辭典**、**高解析度投影片圖解**與**可直接執行的 Python 實作程式碼**。

---

## 🗺️ 課程知識地圖 (Course Knowledge Roadmap)

```mermaid
mindmap
  root((資訊工程導論<br/>Intro to Info Eng))
    Module 0: 課程大綱與倫理規範
      學術倫理與誠信五大原則
      生成式 AI 協作指南 Tutor not Answer Generator
      布魯姆認知目標 Remember Understand Apply
      18週教學進度與評分權重
    Module 1: 計算機科學緒論
      核心詞彙鏈 Problem to Hardware
      演算法五大特性 Input Output Definiteness Effectiveness Finiteness
      計算工具六大演進史 從算盤到積體電路
      九大核心主題 演算法 抽象化 創造性 資料 程式化 網路 影響力 AI 數位永續
      Google Maps 實務貫穿分析
      程式開發典範演進 從手工寫 Code 到 Agentic Coding
      四大哲學倫理框架 德行 義務 效益 契約
    Module 2: 演算法與問題解決
      演算法正式定義 順序性 明確性 可行性 終止性
      抽象本質 故事 vs 書本
      Pólya 解題四階段 瞭解 擬定 執行 回顧
      虛擬碼原式 指定 條件 縮排 迭代 函式
      迭代結構 循序搜尋 插入排序 選擇排序
      遞迴結構 基本情況 遞迴步驟 望遠鏡展開 二元搜尋
      Big-O 漸進複雜度 多項式定理 成長率層級
      金環切割問題 二進位冪次編碼
      軟體驗證 斷言 前後置條件 迴圈不變量三要素
```

---

## 📚 模組章節導航 (Modules Navigation)

| 模組目錄 | 主題單元 | 課本章節 | 重點內容提要 | 快速傳送門 |
| :--- | :--- | :---: | :--- | :---: |
| **Module 0** | **課程大綱與學習指引**<br/>*(Course Syllabus & Guide)* | Syllabus | 評分標準、18 週進度表、布魯姆認知層級、學術倫理與生成式 AI 使用 SOP、MIT 腦波反思。 | [前往閱讀 📖](00_Course_Syllabus/README.md) |
| **Module 1** | **計算機科學緒論與核心思維**<br/>*(Introduction to CS)* | Ch 0 | 詞彙鏈、演算法五大特性、輾轉相除法推演、計算機歷史六大階段、九大核心主題、AI 時代為何學 CS、四大倫理框架。 | [前往閱讀 📖](01_Introduction_to_CS/README.md) |
| **Module 2** | **演算法與問題解決全解析**<br/>*(Algorithms & Problem Solving)* | Ch 5 | 演算法定義、摺紙原式、Pólya 解題法、小孩年齡與賽跑問題、迭代 vs 遞迴、插入排序追蹤、二元搜尋、Big-O、金環問題、迴圈不變量。 | [前往閱讀 📖](02_Algorithms_and_Problem_Solving/README.md) |

---

## 💻 課堂演算法 Python 程式碼庫 (Executable Code Examples)

本倉儲提供所有課堂探討之演算法的可執行 Python 程式碼，均附有完整繁體中文註解與測試資料：

| 檔案名稱 | 演算法 / 課題名稱 | 對應講義單元 | 時間複雜度 | 原始碼連結 |
| :--- | :--- | :---: | :---: | :---: |
| `gcd_euclidean.py` | 歐幾里得輾轉相除法 (減法版 / 取模版 / 遞迴版) | Module 1 (圖0.2) | $O(\log(\min(M, N)))$ | [檢視原始碼 ↗](code_examples/gcd_euclidean.py) |
| `largest_product_set.py` | 正整數最大乘積拆解問題 (貪婪/數學解法) | Module 2 (P.37~39) | $O(n)$ | [檢視原始碼 ↗](code_examples/largest_product_set.py) |
| `sequential_search.py` | 循序搜尋法 (線性搜尋) | Module 2 (圖5.6) | $O(n)$ | [檢視原始碼 ↗](code_examples/sequential_search.py) |
| `insertion_sort.py` | 插入排序法 (逐步撲克牌摸牌追蹤) | Module 2 (圖5.10~5.11) | $O(n^2)$ | [檢視原始碼 ↗](code_examples/insertion_sort.py) |
| `selection_sort.py` | 選擇排序法 (極值交換追蹤) | Module 2 (P.55) | $O(n^2)$ | [檢視原始碼 ↗](code_examples/selection_sort.py) |
| `binary_search_iterative.py` | 二元搜尋法 - 迭代版本 (二分折半) | Module 2 (P.60) | $O(\log n)$ | [檢視原始碼 ↗](code_examples/binary_search_iterative.py) |
| `binary_search_recursive.py` | 二元搜尋法 - 遞迴版本 (堆疊階層追蹤) | Module 2 (圖5.14~5.17) | $O(\log n)$ | [檢視原始碼 ↗](code_examples/binary_search_recursive.py) |
| `fibonacci_factorial.py` | 階乘與費氏數列 (遞迴 vs 迭代開銷比對) | Module 2 (P.43~46) | 多種 | [檢視原始碼 ↗](code_examples/fibonacci_factorial.py) |
| `loop_invariant_demo.py` | 迴圈不變量三要素驗證與 Assertion 斷言 | Module 2 (P.87~89) | $O(n)$ | [檢視原始碼 ↗](code_examples/loop_invariant_demo.py) |

### 快速執行示範：
```bash
# 執行輾轉相除法測試
python code_examples/gcd_euclidean.py

# 執行插入排序逐步追蹤
python code_examples/insertion_sort.py

# 執行迴圈不變量形式化斷言驗證
python code_examples/loop_invariant_demo.py
```

---

## 🗂️ 專案目錄結構 (Repository Structure)

```text
.
├── 00_Course_Syllabus/
│   └── README.md                  # Module 0 完整筆記 (大綱、評分、AI規範)
├── 01_Introduction_to_CS/
│   └── README.md                  # Module 1 完整筆記 (緒論、歷史、九大主題)
├── 02_Algorithms_and_Problem_Solving/
│   └── README.md                  # Module 2 完整筆記 (演算法、結構、搜尋排序、Big-O)
├── images/                        # 高解析度講義圖解與架構圖
│   ├── module0/                   # Module 0 投影片圖解 (評分、布魯姆、AI規範)
│   ├── module1/                   # Module 1 投影片圖解 (歷史、輾轉相除法、九大主題)
│   └── module2/                   # Module 2 投影片圖解 (摺紙原式、二元搜尋、Big-O)
├── code_examples/                 # 課堂演算法 Python 實作程式庫
│   ├── gcd_euclidean.py
│   ├── largest_product_set.py
│   ├── sequential_search.py
│   ├── insertion_sort.py
│   ├── selection_sort.py
│   ├── binary_search_iterative.py
│   ├── binary_search_recursive.py
│   ├── fibonacci_factorial.py
│   └── loop_invariant_demo.py
└── README.md                      # 本總覽首頁
```

---

## 📖 核心專有名詞快速總查表 (Master Vocabulary Quick Index)

| 英文專有名詞 (English Term) | 繁體中文對照 (Traditional Chinese) | 所屬模組 |
| :--- | :--- | :---: |
| **Bloom's Taxonomy** | 布魯姆認知領域教學目標 (記憶、理解、應用) | Module 0 |
| **Academic Ethics** | 學術倫理 (誠信、公平、尊重、責任) | Module 0 |
| **Algorithm** | 演算法 (順序性、無歧義、可執行、有限終止) | Module 1, 2 |
| **Definiteness / Effectiveness / Finiteness** | 確定性 / 有效性 / 有限性 | Module 1 |
| **Euclidean Algorithm (GCD)** | 歐幾里得輾轉相除法 (最大公因數) | Module 1 |
| **Abstraction & Black Box** | 抽象化與黑盒子概念 (隱藏實作、暴露介面) | Module 1 |
| **Moore's Law** | 摩爾定律 (電晶體每 18~24 個月翻倍) | Module 1 |
| **Agentic Coding / Vibe Coding** | 自主代理程式設計 / 直覺共感編程 | Module 1 |
| **Primitives** | 原式 / 語法基元 (摺紙原式與指令積木) | Module 2 |
| **Heuristics / Pólya Method** | 啟發式策略 / 波利亞解題四階段 | Module 2 |
| **Sequential Search** | 循序搜尋法 ($O(n)$) | Module 2 |
| **Insertion Sort / Selection Sort** | 插入排序法 / 選擇排序法 ($O(n^2)$) | Module 2 |
| **Recursive Structure & Base Case** | 遞迴結構與基本情況 (退化條件) | Module 2 |
| **Binary Search** | 二元搜尋法 ($O(\log n)$，分而治之折半搜尋) | Module 2 |
| **Big-O Notation** | 大 O 符號 (時間與空間漸進複雜度) | Module 2 |
| **Loop Invariant** | 迴圈不變量 (初始性、保持性、終結性) | Module 2 |

---

## 👨‍🏫 課程資訊與致謝 (Course Info & Acknowledgments)
- **學校單位**：國立虎尾科技大學 (National Formosa University) 資訊工程學系
- **授課教授**：蔡柏祥 教授
- **指定教材**：*Computer Science: An Overview*, 13th Edition, J. Glenn Brookshear and Dennis Brylow, Pearson, Addison Wesley. (滄海圖書代理)
