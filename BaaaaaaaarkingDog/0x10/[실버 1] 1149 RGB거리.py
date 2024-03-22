import sys

input = sys.stdin.readline

n = int(input())
rgb = [[0 for _ in range(3)] for _ in range(n + 1)]

for i in range(1, n + 1):
    rgb[i][0], rgb[i][1], rgb[i][2] = map(int, input().split())
    
# dp[i][j]: i번째 집까지 칠하는 비용의 최솟값 (단, j는 0부터 2까지 각각 빨강, 초록, 파랑)
dp = [[0 for _ in range(3)] for _ in range(n + 1)]

dp[1][0] = rgb[1][0]
dp[1][1] = rgb[1][1]
dp[1][2] = rgb[1][2]

for i in range(1, n + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2]

print(min(dp[n][0], dp[n][1], dp[n][2]))
