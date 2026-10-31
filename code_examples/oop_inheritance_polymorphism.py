"""
code_examples/oop_inheritance_polymorphism.py
物件導向進階：繼承 (Inheritance) 與多型 (Polymorphism: Overloading vs Overriding)
課程對應：Module 3 (Slide 55-58)

核心概念解析：
1. 繼承 (Inheritance):
   - 基礎類別 (Base / Parent Class): 提供通用的屬性與行為，如 `Bird`。
   - 衍生類別 (Derived / Child Class): 繼承父類別的所有功能，並可擴充或特化，如 `Sparrow`。
   - `super()`: 呼叫父類別之建構子或方法。

2. 多型 (Polymorphism):
   - Overloading (多載): 在「相同類別/範疇」中，定義名稱相同但「參數個數或型別不同」的函數。
     (C++/Java 原生支援靜態多載；Python 透過預設引數、*args 或 @singledispatch 達成)。
   - Overriding (改寫/覆寫): 在「子類別」中重新定義與父類別「名稱相同」的方法，
     以覆蓋父類別預設行為，展現專屬多型動作。
"""

from functools import singledispatch

# ==============================================================================
# 一、繼承與方法覆寫 (Overriding) 示範 (對應講義 P.56, P.58)
# ==============================================================================

class Bird:
    def __init__(self, name: str):
        self.name = name

    def move(self) -> str:
        """父類別預設的移動行為"""
        return "Flying normally (拍翅飛行)"

class Sparrow(Bird):
    def __init__(self, name: str):
        # 呼叫父類別建構子，擴充名稱
        super().__init__("little birdie " + name)

    def move(self) -> str:
        """方法改寫 (Method Overriding): 覆寫父類別的 move() 方法"""
        return "Hovering (盤旋飛行)"

class Penguin(Bird):
    def move(self) -> str:
        """企鵝也是鳥，但改寫為游泳"""
        return "Swimming in cold water (游泳跳躍)"


# ==============================================================================
# 二、方法多載 (Overloading) 示範 (對應講義 P.57)
# ==============================================================================

# 方式 A：講義投影片概念 (依參數型態計算平方)
# 在 Python 中使用 functools.singledispatch 實現基於型別的函數多載
@singledispatch
def square(x):
    raise NotImplementedError(f"不支援的型別: {type(x)}")

@square.register(int)
def _(x: int) -> int:
    print("  -> 呼叫整數版 square(int)")
    return x * x

@square.register(float)
def _(x: float) -> float:
    print("  -> 呼叫浮點數版 square(float)")
    return round(x * x, 4)

# 方式 B：傳統類別內部使用預設參數的多載模擬
class Calculator:
    def add(self, a, b, c=None):
        """根據參數個數多載"""
        if c is not None:
            return a + b + c
        return a + b


def main():
    print("=" * 65)
    print("一、繼承 (Inheritance) 與 方法改寫 (Overriding) 追蹤")
    print("=" * 65)
    bird = Bird("Bird")
    sparrow = Sparrow("Mikey")
    penguin = Penguin("Pingu")

    print(f"父類別物件名稱: {bird.name}")
    print(f"父類別動作: {bird.move()}\n")

    print(f"子類別物件名稱: {sparrow.name}")
    print(f"子類別覆寫動作: {sparrow.move()}\n")

    print(f"另一子類別物件名稱: {penguin.name}")
    print(f"另一子類別覆寫動作: {penguin.move()}\n")

    # 多型呼叫演示：同一個介面 move()，不同物件展現不同專屬行為
    print("【多型威力展示】：統一遍歷鳥群")
    flock = [bird, sparrow, penguin]
    for b in flock:
        print(f" - {b.name:<25}: {b.move()}")

    print("\n" + "=" * 65)
    print("二、方法多載 (Overloading) 追蹤 (依據引數型態分派)")
    print("=" * 65)
    val_int = square(7)
    print(f"square(7) 結果 = {val_int}\n")

    val_float = square(7.5)
    print(f"square(7.5) 結果 = {val_float}\n")

    calc = Calculator()
    print(f"兩數相加: calc.add(10, 20) = {calc.add(10, 20)}")
    print(f"三數相加: calc.add(10, 20, 30) = {calc.add(10, 20, 30)}")

if __name__ == "__main__":
    main()
