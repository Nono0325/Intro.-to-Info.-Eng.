"""
code_examples/sequential_search.py
循序搜尋法 (Sequential / Linear Search)
課程對應：Module 2 (圖5.6)
時間複雜度：O(n)
"""

from typing import List, Any, Optional

def sequential_search(target: Any, array: List[Any]) -> Optional[int]:
    """
    循序走訪陣列，找到第一個與 target 相同的元素索引。
    若找不到則回傳 None。
    """
    for index, item in enumerate(array):
        if item == target:
            return index
    return None

if __name__ == "__main__":
    names = ["Fred", "Alex", "Diana", "Byron", "Carol", "John"]
    print("=== 循序搜尋法 (Sequential Search) 測試 ===")
    print(f"陣列清單: {names}")
    
    for query in ["Diana", "John", "Alice"]:
        idx = sequential_search(query, names)
        if idx is not None:
            print(f"查詢 '{query}': 找到於索引 {idx}")
        else:
            print(f"查詢 '{query}': 未找到")
