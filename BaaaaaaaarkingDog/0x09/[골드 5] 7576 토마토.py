import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

# BFS 기본 세팅
box = []
day = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

# box 기본 세팅
for _ in range(n):
    row = input().split()
    row = list(map(int, row))
    box.append(row)

# 모든 익은 토마토를 큐에 삽입
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))
            
least_day = 0

while queue:
    x, y = queue.popleft()

    for direc in range(4):
        nx = x + dx[direc]
        ny = y + dy[direc]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = 1
                day[nx][ny] = day[x][y] + 1
                queue.append((nx, ny))

                if least_day < day[nx][ny]:
                    least_day = day[nx][ny]

is_all_grown = True

for row in box:
    if 0 in row:
        is_all_grown = False
        
if is_all_grown:
    print(least_day)
else:
    print(-1)
