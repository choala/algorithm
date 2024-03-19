import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    # BFS 기본 세팅
    cabbage = [[0 for _ in range(m)] for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()

    # cabbage 기본 세팅
    for _ in range(k):
        x, y = map(int, input().split())

        cabbage[y][x] = 1
        
    white = 0
    
    for i in range(n):
        for j in range(m):
            # 시작점 찾기
            if cabbage[i][j] == 1 and visit[i][j] == 0:
                visit[i][j] = 1
                queue.append((i, j))
                white += 1
    
            while queue:
                x, y = queue.popleft()
    
                for direc in range(4):
                    nx = x + dx[direc]
                    ny = y + dy[direc]
    
                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if cabbage[nx][ny] == 1 and visit[nx][ny] == 0:
                            visit[nx][ny] = 1
                            queue.append((nx, ny))
    
    print(white)
