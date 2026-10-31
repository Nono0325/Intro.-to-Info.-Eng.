"""
code_examples/oop_laser_gun.py
物件導向程式設計：雷射槍類別 (LaserClass) 與資訊隱藏/封裝實作
課程對應：Module 3 (Slide 47-54, 圖 6.19, 圖 6.21, 圖 6.22, In-Class Exercise 3.5)

核心概念：
1. 類別 (Class)：建構物件的藍圖或範本 (Template)。
2. 物件 (Object / Instance)：類別在記憶體中的具體實例。
3. 封裝 (Encapsulation) 與資訊隱藏 (Information Hiding)：
   - 將資料 (屬性/實例變數) 與處理資料的程式 (方法) 打包在一起。
   - 限制內部關鍵資料的直接存取 (visibility 能見度控制)。
   - 私有屬性 (Private): 如 `__RemainingPower`，外部無法直接竄改，保護系統完整性。
   - 公用方法 (Public): 提供良好定義的外部呼叫介面 (Interface)。
4. 生命週期管理：
   - 建構子 (Constructor): `__init__()` 初始化物件狀態。
   - 解構子 (Destructor): `__del__()` 當物件生命週期結束被回收時釋放資源。
"""

class LaserClass:
    def __init__(self, name: str, remaining_power: int = 100):
        """
        建構子 (Constructor): 初始化雷射槍實例
        - self.name: 公用屬性 (Public attribute)
        - self.__RemainingPower: 私有屬性 (Private attribute，雙底線名稱改寫 Name Mangling)
        """
        self.name = name
        self.__RemainingPower = remaining_power
        print(f"[*] 雷射槍 [{self.name}] 成功建立！初始電量: {self.__RemainingPower}")

    def turnRight(self):
        """控制雷射槍右轉"""
        print(f"[{self.name}] Turning right (向右瞄準)")

    def turnLeft(self):
        """控制雷射槍左轉"""
        print(f"[{self.name}] Turning left (向左瞄準)")

    def fire(self):
        """發射雷射 (每次發射消耗 10 點電量)"""
        if self.__RemainingPower >= 10:
            self.__RemainingPower -= 10
            print(f"[{self.name}] Firing! (發射雷射! *POW* 剩餘電量: {self.__RemainingPower})")
        else:
            print(f"[{self.name}] 電量不足，無法發射！請先充電。")

    def readEngery(self) -> int:
        """
        安全存取介面 (Getter Method): 
        外部只能透過此方法讀取私有電量，無法直接賦值篡改
        """
        print(f"[{self.name}] The remainingPower is {self.__RemainingPower}")
        return self.__RemainingPower

    def charge(self, amount: int):
        """受控的修改介面 (Setter / Action Method)"""
        if amount > 0:
            self.__RemainingPower = min(100, self.__RemainingPower + amount)
            print(f"[{self.name}] 充電完成，當前電量: {self.__RemainingPower}")

    def __del__(self):
        """解構子 (Destructor): 物件被記憶體回收時觸發"""
        print(f"[-] Laser Gun [{self.name}] is deleted (物件被解構回收)")

def main():
    print("=== 1. 建立物件實例 (Instance Creation) ===")
    laser_gun = LaserClass("Tsai", 100)
    
    print("\n=== 2. 操作公用方法 (Calling Public Methods) ===")
    laser_gun.turnRight()
    laser_gun.turnLeft()
    laser_gun.fire()
    laser_gun.fire()
    laser_gun.readEngery()
    
    print("\n=== 3. 封裝與資訊隱藏安全性驗證 (Encapsulation Test) ===")
    print("嘗試直接由外部存取私有變數 laser_gun.__RemainingPower ...")
    try:
        # Python 會引發 AttributeError，阻止非法存取
        print(laser_gun.__RemainingPower)
    except AttributeError as e:
        print(f"-> 存取受阻！AttributeError: {e}")
        print("-> 驗證成功：外部無法任意竄改內部關鍵狀態，保證資料完整性！")

    print("\n=== 4. 物件生命週期結束 ===")
    # 刪除物件引用，觸發 __del__
    del laser_gun

if __name__ == "__main__":
    main()
