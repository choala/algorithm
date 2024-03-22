import sys

input = sys.stdin.readline

n = int(input())

# dp[i]: i를 1로 만드는 데 필요한 연산 횟수의 최솟값
dp = [0 for _ in range(1000005)]
to = [0 for _ in range(1000005)]

dp[2] = 1
to[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + 1
    to[i] = i - 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

        if dp[i] == dp[i // 2] + 1:
            to[i] = i // 2
            
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

        if dp[i] == dp[i // 3] + 1:
            to[i] = i // 3

print(dp[n])

next = n
while next != 0:
    print(next, end=' ')
    next = to[next]
