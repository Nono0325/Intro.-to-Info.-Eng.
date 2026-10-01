"""
code_examples/binary_search_iterative.py
二元搜尋法 - 迭代版本 (Binary Search - Iterative)
課程對應：Module 2 (Slide 60)
時間複雜度：O(log n)
前提條件：數列必須已排序 (Sorted)
"""

from typing import List, Any, Optional

def binary_search_iterative(target: Any, sorted_list: List[Any], verbose: bool = False) -> Optional[int]:
    left = 0
    right = len(sorted_list) - 1
    step = 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = sorted_list[mid]
        
        if verbose:
            print(f"Step {step}: 搜尋範圍 [{left}, {right}] (子數列: {sorted_list[left:right+1]}), 中間索引 mid={mid}, 值={mid_val}")
            
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
            
        step += 1
        
    return None

if __name__ == "__main__":
    names = ["Alice", "Bob", "Carol", "David", "Emma", "Fred", "Grace", "Henry", "John", "Kate"]
    print("=== 二元搜尋法 (迭代版) ===")
    print(f"已排序數列: {names}")
    
    target = "John"
    print(f"\n[搜尋目標: {target}]")
    idx = binary_search_iterative(target, names, verbose=True)
    print(f"結果: 在索引 {idx} 找到 '{target}'\n")

    target2 = "Diana"
    print(f"[搜尋目標: {target2}]")
    idx2 = binary_search_iterative(target2, names, verbose=True)
    print(f"結果: {idx2 if idx2 is not None else '未找到'}")
