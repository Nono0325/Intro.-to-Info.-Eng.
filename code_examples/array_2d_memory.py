"""
code_examples/array_2d_memory.py
二維陣列記憶體定址模擬與以列為主 (Row-Major) 定址公式
課程對應：Module 3 (Slide 18-21, 圖 6.5)

數學原理：
記憶體本質上是一維線性連續空間 (1D Linear Space)。
高階語言中的二維陣列 A[rows][cols] 在實體記憶體中通常採用「以列為主 (Row-major)」或「以行為主 (Column-major)」方式平坦化存放。

Row-major 定址公式 (若以 1-based index 為例，如同講義投影片 P.19):
Loc(A[i][j]) = alpha + [n * (i - 1) + (j - 1)] * d
其中：
- alpha: 陣列起始實體記憶體位址 (Base Address)
- n: 每列所包含的元素個數 (Number of columns)
- i: 目標列索引 (1-based row index)
- j: 目標行索引 (1-based column index)
- d: 每個元素佔用的位元組大小 (Element size in bytes)

若轉換為現代 C / Python 的 0-based index:
Loc(A[r][c]) = alpha + [cols * r + c] * d
"""

def calculate_address_1_based(base_addr: int, cols_per_row: int, row_1: int, col_1: int, elem_size: int = 1) -> int:
    """依照講義 P.19 的 1-based Row-major 公式計算記憶體位址"""
    offset = cols_per_row * (row_1 - 1) + (col_1 - 1)
    addr = base_addr + offset * elem_size
    return addr

def calculate_address_0_based(base_addr: int, cols_per_row: int, row_0: int, col_0: int, elem_size: int = 1) -> int:
    """依照現代 C/Python 的 0-based Row-major 公式計算記憶體位址"""
    offset = cols_per_row * row_0 + col_0
    addr = base_addr + offset * elem_size
    return addr

def demonstrate_2d_array():
    print("=== 1. 講義圖 6.5：2 列 9 行 (2x9) 二維陣列定址模擬 ===")
    base_address = 1000
    rows = 2
    cols = 9
    element_size = 1 # 1 byte
    
    print(f"基底位址 (Base Address alpha): {base_address}")
    print(f"陣列維度: {rows} 列 (Rows) x {cols} 行 (Columns)")
    print(f"元素大小 (d): {element_size} byte\n")
    
    # 建立一個邏輯上的 2x9 矩陣資料
    scores = [
        [85, 90, 78, 92, 88, 76, 95, 89, 84], # 第 1 列 (Row 1)
        [70, 82, 91, 65, 87, 93, 79, 81, 88]  # 第 2 列 (Row 2)
    ]
    
    # 模擬 1D 平坦化記憶體 (Row-major flattening)
    flat_memory = []
    for r in range(rows):
        for c in range(cols):
            flat_memory.append(scores[r][c])
            
    print(f"記憶體中連續存放的平坦序列 (18 個元素):")
    print(flat_memory)
    print("-" * 60)
    
    # 測試計算特定元素的位址
    test_cases = [(1, 1), (1, 9), (2, 1), (2, 5), (2, 9)]
    print(f"{'目標元素 (1-based)':<18}{'計算位址':<12}{'值':<6}{'公式推導過程'}")
    print("-" * 60)
    for r1, c1 in test_cases:
        addr = calculate_address_1_based(base_address, cols, r1, c1, element_size)
        val = scores[r1 - 1][c1 - 1]
        formula_str = f"{base_address} + [9*({r1}-1) + ({c1}-1)] * {element_size} = {addr}"
        print(f"Scores[{r1}][{c1}]        {addr:<12}{val:<6}{formula_str}")
        
    print("\n=== 2. Python 2D 陣列初始化示範 (對應講義 P.20-21) ===")
    # 講義寫法：巢狀迴圈建構
    out = []
    for m in range(1, 2 + 1):
        row = []
        for n in range(1, 9 + 1):
            row.append(0)
        out.append(row)
    print("巢狀迴圈產生的 2x9 陣列:")
    print(out)
    
    # 推薦的 Pythonic 列表推導式 (List Comprehension)
    pythonic_2d = [[0 for _ in range(9)] for _ in range(2)]
    print("\nPythonic 列表推導式生成的 2x9 陣列:")
    print(pythonic_2d)

if __name__ == "__main__":
    demonstrate_2d_array()
