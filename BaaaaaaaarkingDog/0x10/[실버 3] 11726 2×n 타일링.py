n = int(input())

# dp[i]: 2 x i 크기의 직사각형을 채우는 방법의 수
dp = [0 for _ in range(1005)]

dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])
