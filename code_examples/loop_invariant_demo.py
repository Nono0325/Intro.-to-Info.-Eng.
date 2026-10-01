"""
code_examples/loop_invariant_demo.py
迴圈不變量 (Loop Invariant) 示範與軟體驗證
課程對應：Module 2 (Slide 85-89)

示範範例：計算陣列總和
迴圈不變量宣告：
在每次迴圈迭代開始前，變數 `total` 恆等於子陣列 `arr[0 : i]` 之總和。

三步驟驗證：
1. 初始性 (Initialization): 迭代前 (i=0)，total = 0，空陣列總和為 0，成立。
2. 保持性 (Maintenance): 假設當前 total = sum(arr[0:i]) 為真，執行 total += arr[i] 且 i += 1，
   則下一次迭代前 total = sum(arr[0:i+1])，依然為真。
3. 終結性 (Termination): 當 i = n 時迴圈終止，此時 total = sum(arr[0:n])，即為整個陣列之總和。
"""

from typing import List

def sum_with_invariant_assertion(arr: List[int]) -> int:
    total = 0
    i = 0
    n = len(arr)
    
    # 1. 初始性 (Initialization)
    assert total == sum(arr[0:i]), f"初始化斷言失敗: total={total}, expected={sum(arr[0:i])}"
    
    while i < n:
        # 迴圈體執行
        total += arr[i]
        i += 1
        
        # 2. 保持性 (Maintenance)
        assert total == sum(arr[0:i]), f"保持性斷言失敗於 i={i}: total={total}, expected={sum(arr[0:i])}"
        print(f"迭代 i={i}: 當前總和 total={total}，驗證子陣列 arr[0:{i}] 總和正確！")
        
    # 3. 終結性 (Termination)
    assert i == n
    assert total == sum(arr), f"終結性斷言失敗: total={total}, expected={sum(arr)}"
    return total

if __name__ == "__main__":
    data = [5, 12, 7, 23, 9]
    print("=== 迴圈不變量 (Loop Invariant) 形式化斷言驗證 ===")
    print(f"輸入陣列: {data}")
    res = sum_with_invariant_assertion(data)
    print(f"驗證通過，陣列總和為: {res}")
