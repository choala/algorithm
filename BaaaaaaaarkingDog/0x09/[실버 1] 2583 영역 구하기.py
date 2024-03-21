import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())

# BFS 기본 세팅
paper = [[0 for _ in range(n)] for _ in range(m)]
is_visited = [[0 for _ in range(n)] for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

# 좌표에 따라 종이에 직사각형 채우기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = '#'

area_list = []
for i in range(m):
    for j in range(n):
        # BFS 시작점 찾기
        if paper[i][j] != '#' and is_visited[i][j] == 0:
            is_visited[i][j] = 1
            queue.append((i, j))

            area = 0
            while queue:
                x, y = queue.popleft()
                area += 1

                for direc in range(4):
                    nx = x + dx[direc]
                    ny = y + dy[direc]

                    if nx >= 0 and nx < m and ny >= 0 and ny < n:
                        if paper[nx][ny] != '#' and is_visited[nx][ny] == 0:
                            is_visited[nx][ny] = 1
                            queue.append((nx, ny))

            area_list.append(area)

print(len(area_list))

area_list.sort()
for area in area_list:
    print(area, end=' ')
