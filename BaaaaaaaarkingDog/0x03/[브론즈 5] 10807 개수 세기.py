import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
v = int(input())

arr.sort()
count = 0
for i in range(n):
    if arr[i] == v:
        count += 1
    elif arr[i] > v:
        break

print(count)
