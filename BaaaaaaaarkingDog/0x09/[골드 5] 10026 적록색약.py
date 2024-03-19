import sys
from collections import deque

input = sys.stdin.readline

n = int(input())


# paint 기본 세팅
paint = []
for _ in range(n):
    row = list(input().strip())
    paint.append(row)
    
# BFS 기본 세팅
visit = [[0 for _ in range(len(paint[0]))] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

rgb_count = 0
rb_count = 0

# 적록색약이 아닌 경우의 BFS
rgb = ['R', 'G', 'B']
for index in range(3):
    for i in range(n):
        for j in range(len(paint[0])):
            if paint[i][j] == rgb[index] and visit[i][j] == 0:
                visit[i][j] = 1
                queue.append((i, j))
                
                rgb_count += 1
    
                while queue:
                    x, y = queue.popleft()
                    
                    for direc in range(4):
                        nx = x + dx[direc]
                        ny = y + dy[direc]
    
                        if nx >= 0 and nx < n and ny >= 0 and ny < len(paint[0]):
                            if paint[nx][ny] == rgb[index] and visit[nx][ny] == 0:
                                visit[nx][ny] = 1
                                queue.append((nx, ny))

# 적록색약인 경우의 BFS
visit = [[0 for _ in range(len(paint[0]))] for _ in range(n)]

rgb = ['RG', 'B']
for index in range(2):
    for i in range(n):
        for j in range(len(paint[0])):
            if paint[i][j] in rgb[index] and visit[i][j] == 0:
                visit[i][j] = 1
                queue.append((i, j))

                rb_count += 1

                while queue:
                    x, y = queue.popleft()

                    for direc in range(4):
                        nx = x + dx[direc]
                        ny = y + dy[direc]

                        if nx >= 0 and nx < n and ny >= 0 and ny < len(paint[0]):
                            if paint[nx][ny] in rgb[index] and visit[nx][ny] == 0:
                                visit[nx][ny] = 1
                                queue.append((nx, ny))

print(rgb_count, rb_count)
