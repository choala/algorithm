n = int(input())

for i in range(n):
    print("*" * (i + 1), end="")

    for _ in range((n - i - 1) * 2):
        print(" ", end="")

    print("*" * (i + 1))

for j in range(n - 1):
    print("*" * (n - j - 1), end="")

    for _ in range((j + 1) * 2):
        print(" ", end="")

    print("*" * (n - j - 1))
    
