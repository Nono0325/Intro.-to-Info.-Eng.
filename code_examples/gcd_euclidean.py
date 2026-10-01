"""
code_examples/gcd_euclidean.py
歐幾里得輾轉相除法 (Euclidean Algorithm for Greatest Common Divisor, GCD)
課程對應：Module 1 (圖0.2)
"""

def gcd_subtraction(m: int, n: int) -> int:
    """使用減法實作輾轉相除法 (如教材原始虛擬碼邏輯)"""
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m

def gcd_modulo(m: int, n: int) -> int:
    """使用取模運算子 (%) 實作更高效的歐幾里得演算法"""
    while n != 0:
        r = m % n
        m = n
        n = r
    return m

def gcd_recursive(m: int, n: int) -> int:
    """遞迴版本的歐幾里得演算法"""
    if n == 0:
        return m
    return gcd_recursive(n, m % n)

if __name__ == "__main__":
    test_cases = [(24, 16), (48, 18), (101, 10), (270, 192)]
    print("=== 歐幾里得輾轉相除法 (GCD) 測試 ===")
    for a, b in test_cases:
        res1 = gcd_subtraction(a, b)
        res2 = gcd_modulo(a, b)
        res3 = gcd_recursive(a, b)
        print(f"GCD({a}, {b}) => 減法版: {res1}, 取模版: {res2}, 遞迴版: {res3}")
        assert res1 == res2 == res3
    print("所有測試通過！\n")
