import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())

    # BFS 기본 세팅
    maze = []
    sec = [[-1 for _ in range(w)] for _ in range(h)]
    fire = [[-1 for _ in range(w)] for _ in range(h)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    s_queue = deque()
    f_queue = deque()

    # maze 기본 세팅
    for _ in range(h):
        row = list(input().strip())
        maze.append(row)

    # 상근이의 시작점과 불의 발화점 찾기
    for i in range(h):
        for j in range(w):
            if maze[i][j] == '@':
                sec[i][j] = 0
                s_queue.append((i, j))
            if maze[i][j] == '*':
                fire[i][j] = 0
                f_queue.append((i, j))

    # 불에 대한 BFS
    while f_queue:
        x, y = f_queue.popleft()

        for direc in range(4):
            nx = x + dx[direc]
            ny = y + dy[direc]

            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                # 벽이 아니면서 불에 타지 않은 지점인 경우
                if maze[nx][ny] != '#' and fire[nx][ny] == -1:
                    fire[nx][ny] = fire[x][y] + 1
                    f_queue.append((nx, ny))
                
    # 상근이에 대한 BFS
    is_possible = False
    escape_time = 0
    
    while s_queue and not is_possible:
        x, y = s_queue.popleft()

        for direc in range(4):
            nx = x + dx[direc]
            ny = y + dy[direc]

            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                # 벽이 아니면서 아직 지나가지 않은 지점인 경우
                if maze[nx][ny] != '#' and sec[nx][ny] == -1:
                    # 아직 불이 나지 않았거나 불보다 먼저 지나가는 경우
                    if fire[nx][ny] == -1 or sec[x][y] + 1 < fire[nx][ny]:
                        sec[nx][ny] = sec[x][y] + 1
                        s_queue.append((nx, ny))
            else:
                is_possible = True
                escape_time = sec[x][y] + 1

    if is_possible:
        print(escape_time)
    else:
        print("IMPOSSIBLE")
