n = int(input())

for i in range(n):
    print(" " * i, end="")
    print("*" * ((n - i) * 2 - 1))

for j in range(n - 1):
    print(" " * (n - j - 2), end="")
    print("*" * ((j + 1) * 2 + 1))
