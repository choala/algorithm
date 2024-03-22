import sys

input = sys.stdin.readline

n = int(input())
steps = [int(input()) for _ in range(n)]

if n == 1:
    print(steps[0])
elif n == 2:
    print(steps[0] + steps[1])
elif n == 3:
    print(dp[2] = max(steps[0] + steps[2], steps[1] + steps[2]))
else:
    # DP 기본 세팅
    dp = [0 for _ in range(305)]
    
    dp[0] = steps[0]
    dp[1] = steps[0] + steps[1]
    dp[2] = max(steps[0] + steps[2], steps[1] + steps[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i - 3] + steps[i] + steps[i - 1], dp[i - 2] + steps[i])
    
    print(dp[n - 1])
