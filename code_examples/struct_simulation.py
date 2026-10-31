"""
code_examples/struct_simulation.py
資料結構：結構體 (Struct) 與聚合型別 (Aggregate Type) 的 Python 模擬
課程對應：Module 3 (Slide 22-23, 圖 6.6, In-Class Exercise 3.2)

核心概念：
1. 陣列 (Array) vs 結構 (Struct / Record):
   - 陣列 (Array)：同質性資料結構 (Homogeneous)，所有元素型別皆相同，透過整數索引 (Index) 存取。
   - 結構 (Struct / Record)：異質性聚合型別 (Heterogeneous / Aggregate Type)，包含不同型別的欄位 (Fields)，
     透過欄位名稱 (Field Name) 存取。
     
2. 講義圖 6.6 C 語言結構體定義：
   struct Employee {
       string name;
       int age;
       int skill_rating;
   };
"""

from dataclasses import dataclass
from collections import namedtuple

# 方式一：傳統 Python 物件類別 (對應講義 P.23 投影片範例)
class EmployeeClass:
    def __init__(self, name: str, age: int, skill_rating: int):
        self.name = name
        self.age = age
        self.skill_rating = skill_rating
        
    def __repr__(self):
        return f"EmployeeClass(name='{self.name}', age={self.age}, skill_rating={self.skill_rating})"

# 方式二：現代 Python 3.7+ @dataclass (最推薦的 C struct 替代品)
@dataclass
class EmployeeDataClass:
    name: str
    age: int
    skill_rating: int

# 方式三：具名元組 namedtuple (輕量且具不可變性 Immutable)
EmployeeTuple = namedtuple('EmployeeTuple', ['name', 'age', 'skill_rating'])

def demonstrate_structures():
    print("=== 1. 課堂投影片標準實作 (Class 模擬 struct) ===")
    emp1 = EmployeeClass("Tony", 40, 100)
    print(f"物件表示: {emp1}")
    print(f"存取欄位: name = {emp1.name}")
    print(f"存取欄位: age = {emp1.age}")
    print(f"存取欄位: skill_rating = {emp1.skill_rating}\n")
    
    print("=== 2. 現代 Python @dataclass 實作 ===")
    emp2 = EmployeeDataClass("Alice", 28, 95)
    print(f"DataClass 物件: {emp2}")
    print(f"存取欄位: emp2.name = {emp2.name}, emp2.skill_rating = {emp2.skill_rating}\n")
    
    print("=== 3. 具名元組 NamedTuple 實作 ===")
    emp3 = EmployeeTuple("Bob", 35, 88)
    print(f"NamedTuple: {emp3}")
    print(f"欄位存取: emp3.name = {emp3.name}, emp3.age = {emp3.age}\n")
    
    print("=== 4. 陣列 (同質) 與 結構 (異質聚合) 記憶體與概念對比 ===")
    print("【陣列 Array】: [85, 90, 78] -> 全部皆為整數 (int)，連續等距存放。")
    print("【結構 Struct】: {name: 'Tony' (字串), age: 40 (整數), skill_rating: 100 (整數)} -> 多種型別混合打包。")

if __name__ == "__main__":
    demonstrate_structures()
