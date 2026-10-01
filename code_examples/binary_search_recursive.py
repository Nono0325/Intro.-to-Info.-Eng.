"""
code_examples/binary_search_recursive.py
二元搜尋法 - 遞迴版本 (Binary Search - Recursive)
課程對應：Module 2 (Slide 61-65, 圖5.14-5.17)
時間複雜度：O(log n)
空間複雜度：O(log n) (因呼叫堆疊 Call Stack 深度)
"""

from typing import List, Any, Optional

def binary_search_recursive(target: Any, sorted_list: List[Any], left: int, right: int, depth: int = 1) -> Optional[int]:
    # 基本情況 (Base Case): 搜尋區間無效，目標不存在
    if left > right:
        print(f"{'  '*depth}[遞迴層級 {depth}] 區間無效 [{left}, {right}]，搜尋結束：未找到")
        return None

    mid = (left + right) // 2
    mid_val = sorted_list[mid]
    print(f"{'  '*depth}[遞迴層級 {depth}] 搜尋範圍 [{left}, {right}], 中間索引 {mid}, 值: '{mid_val}'")

    # 基本情況 (Base Case): 找到目標
    if mid_val == target:
        print(f"{'  '*depth}[遞迴層級 {depth}] 命中目標 '{target}'！")
        return mid

    # 遞迴步驟 (Recursive Step): 目標在右半部
    elif mid_val < target:
        return binary_search_recursive(target, sorted_list, mid + 1, right, depth + 1)

    # 遞迴步驟 (Recursive Step): 目標在左半部
    else:
        return binary_search_recursive(target, sorted_list, left, mid - 1, depth + 1)

if __name__ == "__main__":
    names = ["Alice", "Bob", "Carol", "David", "Emma", "Fred", "Grace", "Henry", "John", "Kate"]
    print("=== 二元搜尋法 (遞迴版) 呼叫堆疊展現 ===")
    print(f"已排序數列: {names}")
    
    target = "John"
    print(f"\n[開始遞迴搜尋: {target}]")
    idx = binary_search_recursive(target, names, 0, len(names) - 1)
    print(f"最終回傳索引: {idx}")
