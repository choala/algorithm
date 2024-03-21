n = int(input())

dp = [0 for _ in range(1000005)]

dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        dp[i] = min(1 + dp[i // 2], 1 + dp[i // 3], 1 + dp[i - 1])
    elif i % 2 == 0:
        dp[i] = min(1 + dp[i // 2], 1 + dp[i - 1])
    elif i % 3 == 0:
        dp[i] = min(1 + dp[i // 3], 1 + dp[i - 1])
    else:
        dp[i] = 1 + dp[i - 1]

print(dp[n])
