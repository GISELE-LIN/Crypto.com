def print_pyramid(n):
    # 迴圈處理列數
    for i in range(1, n + 1):
        # 打印空格來對齊
        print(" " * (n - i), end="")
        # 打印星號來形成金字塔
        print("*" * (2 * i - 1))

# 調用函數，打印 5 層的金字塔
print_pyramid(5)
