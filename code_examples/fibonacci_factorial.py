"""
code_examples/fibonacci_factorial.py
遞迴與迭代對比 (Recursion vs Iteration)
課程對應：Module 2 (Slide 43-46)
"""

def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def fibonacci_iterative(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    print("=== 階乘 (Factorial) 對比 ===")
    for num in [1, 5, 8]:
        print(f"{num}! -> 迭代: {factorial_iterative(num)}, 遞迴: {factorial_recursive(num)}")

    print("\n=== 費氏數列 (Fibonacci) 對比 ===")
    for idx in range(1, 11):
        print(f"Fib({idx}) -> 迭代: {fibonacci_iterative(idx)}, 遞迴: {fibonacci_recursive(idx)}")
