import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

count_arr = [0 for _ in range(1000001)]
count = 0
for i in range(n):
    if (x - arr[i]) >= 0 and (x - arr[i] <= 1000000):
        if count_arr[x - arr[i]] == 1:
            count += 1
        count_arr[arr[i]] = 1

print(count)
