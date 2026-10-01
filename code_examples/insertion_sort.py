"""
code_examples/insertion_sort.py
插入排序法 (Insertion Sort)
課程對應：Module 2 (圖5.10, 圖5.11, 圖5.18, 圖5.19)
時間複雜度：
  - 最壞情況 (反序): O(n^2)
  - 最佳情況 (已排序): O(n)
  - 平均情況: O(n^2)
"""

from typing import List

def insertion_sort(arr: List[any], verbose: bool = False) -> List[any]:
    data = list(arr)
    n = len(data)
    
    if verbose:
        print(f"初始數列: {data}")
        
    for i in range(1, n):
        key = data[i]
        j = i - 1
        
        # 將大於 key 的元素向右移一位
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            
        data[j + 1] = key
        
        if verbose:
            print(f"步驟 {i} (插入 '{key}'): {data}")
            
    return data

if __name__ == "__main__":
    names = ["Fred", "Alex", "Diana", "Byron", "Carol"]
    print("=== 插入排序法 (Insertion Sort) 逐步追蹤 ===")
    sorted_names = insertion_sort(names, verbose=True)
    print(f"\n最終排序結果: {sorted_names}")
