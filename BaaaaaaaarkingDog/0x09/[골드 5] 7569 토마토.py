import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

# BFS 기본 세팅
boxes = []
day = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()

# box 기본 세팅
for _ in range(h):
    box = []
    
    for _ in range(n):
        row = input().strip().split()
        row = list(map(int, row))
        box.append(row)

    boxes.append(box)

# 모든 익은 토마토를 큐에 삽입
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                queue.append((i, j, k))

least_day = 0

while queue:
    x, y, z = queue.popleft()

    for direc in range(6):
        nx = x + dx[direc]
        ny = y + dy[direc]
        nz = z + dz[direc]

        if nx >= 0 and nx < h and ny >= 0 and ny < n and nz >= 0 and nz < m:
            if boxes[nx][ny][nz] == 0:
                boxes[nx][ny][nz] = 1
                day[nx][ny][nz] = day[x][y][z] + 1
                queue.append((nx, ny, nz))

                if least_day < day[nx][ny][nz]:
                    least_day = day[nx][ny][nz]

is_all_grown = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 0:
                is_all_grown = False
                break

if is_all_grown:
    print(least_day)
else:
    print(-1)
