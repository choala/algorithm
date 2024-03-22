import sys

input = sys.stdin.readline

n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]
money.sort(reverse=True)

counts = 0
for i in range(n):
    if money[i] <= k:
        count, change = divmod(k, money[i])

        counts += count
        k = change

print(counts)
