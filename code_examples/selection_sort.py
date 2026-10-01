"""
code_examples/selection_sort.py
選擇排序法 (Selection Sort)
課程對應：Module 2 (Slide 55 隨堂練習)
時間複雜度：O(n^2) (所有情況皆需要 n(n-1)/2 次比較)
"""

from typing import List

def selection_sort(arr: List[any], verbose: bool = False) -> List[any]:
    data = list(arr)
    n = len(data)
    
    if verbose:
        print(f"初始數列: {data}")
        
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
                
        # 交換
        data[i], data[min_idx] = data[min_idx], data[i]
        
        if verbose:
            print(f"回合 {i + 1} (選擇最小值 '{data[i]}'): {data}")
            
    return data

if __name__ == "__main__":
    names = ["Fred", "Alex", "Diana", "Byron", "Carol"]
    print("=== 選擇排序法 (Selection Sort) 逐步追蹤 ===")
    sorted_names = selection_sort(names, verbose=True)
    print(f"\n最終排序結果: {sorted_names}")
