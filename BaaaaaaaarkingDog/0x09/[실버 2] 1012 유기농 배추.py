import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for _ in range(t):
    m, n, k = map(int, input().split())
    count = 0

    cabbage = [[0 for _ in range(m)] for _ in range(n)]

    # 배추 밭 세팅
    for _ in range(k):
        y, x = map(int, input().split())
        cabbage[x][y] = 1

    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                cabbage[i][j] = 0
                queue.append((i, j))

                count += 1

                while queue:
                    x, y = queue.popleft()
                    
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]

                        if nx >= 0 and nx < n and ny >= 0 and ny < m:
                            if cabbage[nx][ny] == 1:
                                cabbage[nx][ny] = 0
                                queue.append((nx, ny))
                                
    print(count)
