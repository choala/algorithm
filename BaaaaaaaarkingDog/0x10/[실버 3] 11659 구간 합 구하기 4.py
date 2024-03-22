import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

# dp[i]: i번째까지의 모든 수의 합
dp = [0 for _ in range(100005)]

dp[1] = num[0]
dp[2] = num[0] + num[1]

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + num[i - 1]

for _ in range(m):
    s, e = map(int, input().split())
    
    print(dp[e] - dp[s - 1])
