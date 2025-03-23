def print_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))

# 5 layer
print_pyramid(5)