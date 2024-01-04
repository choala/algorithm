n = int(input())

for i in range(n - 1):
    for j in range(n - i - 1):
        print(" ", end="")
    print("*" * (2 * i + 1))

for i in range(n):
    for j in range(i):
        print(" ", end="")
    print("*" * (2 * (n - i) - 1))
