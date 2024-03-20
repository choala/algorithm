import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    length = int(input())
    cursor_x, cursor_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())

    # BFS 기본 세팅
    board = [[-1 for _ in range(length)] for _ in range(length)]
    dx = [-2, -2, 2, 2, -1, -1, 1, 1]
    dy = [-1, 1, -1, 1, -2, 2, -2, 2]

    queue = deque()

    board[cursor_x][cursor_y] = 0
    queue.append((cursor_x, cursor_y))

    while board[goal_x][goal_y] == -1:
        x, y = queue.popleft()

        for direc in range(8):
            nx = x + dx[direc]
            ny = y + dy[direc]

            if nx >= 0 and nx < length and ny >= 0 and ny < length:
                if board[nx][ny] == -1:
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))

    print(board[goal_x][goal_y])
