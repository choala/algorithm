import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

# BFS 기본 세팅
maze = []
fire = [[-1 for _ in range(c)] for _ in range(r)]
dist = [[-1 for _ in range(c)] for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

f_queue = deque()
j_queue = deque()

# maze 기본 세팅
for _ in range(r):
    row = list(input().strip())
    maze.append(row)

# 불의 발화점과 지훈이의 시작점 찾기
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            fire[i][j] = 0
            f_queue.append((i, j))
        if maze[i][j] == 'J':
            dist[i][j] = 0
            j_queue.append((i, j))

while f_queue:
    x, y = f_queue.popleft()

    for direc in range(4):
        nx = x + dx[direc]
        ny = y + dy[direc]

        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            # 벽이 아니면서 아직 불에 타지 않은 지점인 경우
            if maze[nx][ny] != '#' and fire[nx][ny] == -1:
                fire[nx][ny] = fire[x][y] + 1
                f_queue.append((nx, ny))

is_possible = False
escape_time = 0

while j_queue and not is_possible:
    x, y = j_queue.popleft()

    for direc in range(4):
        nx = x + dx[direc]
        ny = y + dy[direc]

        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            # 벽이 아니면서 아직 지나가지 않은 지점인 경우
            if maze[nx][ny] != '#' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                
                # 불에 타기 전에 지나가는 경우
                if fire[nx][ny] == -1 or dist[nx][ny] < fire[nx][ny]:
                    j_queue.append((nx, ny))
        else:
            is_possible = True
            escape_time = dist[x][y] + 1

if is_possible:
    print(escape_time)
else:
    print("IMPOSSIBLE")
