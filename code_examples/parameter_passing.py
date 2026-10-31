"""
code_examples/parameter_passing.py
參數傳遞機制剖析：傳值 (Call by Value) vs 傳址 (Call by Reference)
課程對應：Module 3 (Slide 38-43, 圖 6.10, 圖 6.11, In-Class Exercise 3.3)

理論分析：
1. 傳值呼叫 (Call by Value, 圖 6.10):
   - 呼叫端將「實質引數的值 (Value)」複製一份至副程式的「形式參數 (Formal Parameter)」。
   - 形式參數在副程式的堆疊訊框 (Stack Frame) 中配置獨立空間。
   - 副程式內對形式參數的任何更改，僅影響其內部副本，對呼叫端的原始變數毫無影響。

2. 傳址呼叫 (Call by Reference, 圖 6.11):
   - 呼叫端將「實質引數的記憶體位址 (Memory Address)」傳遞給形式參數。
   - 形式參數成為呼叫端原始變數的別名 (Alias)。
   - 副程式內對形式參數的任何讀寫，直接作用於呼叫端的實體記憶體位置。

3. Python 的傳遞機制 (Pass-by-Object-Reference / Call-by-Assignment):
   - 不可變物件 (Immutable: int, float, str, tuple) -> 行為等同傳值。
   - 可變物件 (Mutable: list, dict, 自訂類別實例) -> 透過內部修改 (In-place mutation) 行為等同傳址。
"""

from typing import List

# 模擬 C 語言傳值示範 (Call by Value)
def demo_call_by_value(x: int):
    print(f"  [副程式進入] 形式參數 x = {x} (記憶體位址 id = {id(x)})")
    x = x + 10  # 重新賦值，產生新物件
    print(f"  [副程式修改後] 形式參數 x = {x} (新記憶體位址 id = {id(x)})")

# 模擬 C++ 傳址示範 (使用可變列表或包裝物件模擬 Reference / Pointer)
class IntReference:
    def __init__(self, value: int):
        self.value = value
    def __repr__(self):
        return str(self.value)

def demo_call_by_reference(ref: IntReference):
    print(f"  [副程式進入] 接收指標位址 ref = {id(ref)}, 其值為 = {ref.value}")
    ref.value += 10 # 直接更改原位址內容
    print(f"  [副程式修改後] 直接修改指標目標內容: ref.value = {ref.value}")

def demo_python_mutable_passing(data_list: List[int]):
    print(f"  [副程式進入] 接收列表位址 id = {id(data_list)}, 內容 = {data_list}")
    data_list.append(999) # 內部修改 (In-place mutation)
    print(f"  [副程式修改後] 列表內容更新為 = {data_list}")

def main():
    print("=" * 65)
    print("一、傳值呼叫 (Call by Value) 追蹤 (對應講義圖 6.10)")
    print("=" * 65)
    orig_a = 5
    print(f"[呼叫前] 主程式變數 a = {orig_a} (記憶體 id = {id(orig_a)})")
    demo_call_by_value(orig_a)
    print(f"[呼叫後] 主程式變數 a = {orig_a} (數值不受影響！完全安全隔離)\n")

    print("=" * 65)
    print("二、傳址呼叫 (Call by Reference) 追蹤 (對應講義圖 6.11)")
    print("=" * 65)
    orig_ref = IntReference(5)
    print(f"[呼叫前] 主程式包裝變數 ref = {orig_ref} (記憶體 id = {id(orig_ref)})")
    demo_call_by_reference(orig_ref)
    print(f"[呼叫後] 主程式包裝變數 ref = {orig_ref} (數值已被副程式直接更動！)\n")

    print("=" * 65)
    print("三、Python 可變物件之參考傳遞特性")
    print("=" * 65)
    my_list = [1, 2, 3]
    print(f"[呼叫前] my_list = {my_list}")
    demo_python_mutable_passing(my_list)
    print(f"[呼叫後] my_list = {my_list} (原始列表已直接被擴增！)")

if __name__ == "__main__":
    main()
