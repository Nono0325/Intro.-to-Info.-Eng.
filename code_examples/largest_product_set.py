"""
code_examples/largest_product_set.py
課堂挑戰題：給定正整數 n，找出一組總和為 n 的正整數數列，使其乘積最大
課程對應：Module 2 (Slide 37-39)

解題思維 (Polya 階段論應用)：
1. 觀察數列：
   - 任何大於 4 的整數 k，拆成 2 和 (k-2) 或 3 和 (k-3)，其乘積都比 k 本身更大。
   - 拆解因子 3 比 2 更優 (因為 3^(n/3) > 2^(n/2))。
   - 特例：如果最後剩下 1，應該與前面的 3 合併變成 4 (即 2*2)。
"""

from typing import List, Tuple

def largest_product_set(n: int) -> Tuple[int, List[int]]:
    if n <= 1:
        return n, [n]
    if n == 2:
        return 1, [1, 1]
    if n == 3:
        return 2, [1, 2]

    factors = []
    current = n
    
    # 盡可能拆出 3
    while current > 4:
        factors.append(3)
        current -= 3
        
    # 剩下的數字只會是 2, 3 或 4
    if current == 4:
        factors.extend([2, 2])
    else:
        factors.append(current)

    # 計算總乘積
    product = 1
    for f in factors:
        product *= f

    return product, factors

if __name__ == "__main__":
    print("=== 正整數最大乘積拆解測試 ===")
    for n in range(2, 16):
        prod, parts = largest_product_set(n)
        print(f"n = {n:2d} -> 拆解: {' + '.join(map(str, parts))} = {n}, 最大乘積 = {prod}")
