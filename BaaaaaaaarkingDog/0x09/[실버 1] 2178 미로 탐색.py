import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# BFS 기본 세팅
maze = []
distance = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = []

# maze 기본 세팅
for _ in range(n):
    row = list(input().strip())
    row = list(map(int, row))
    maze.append(row)

distance[0][0] = 1
queue.append((0, 0))

while queue:
    x, y = queue.pop(0)

    for direc in range(4):
        nx = x + dx[direc]
        ny = y + dy[direc]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if maze[nx][ny] == 1 and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

print(distance[n - 1][m - 1])
