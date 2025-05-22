import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# BFS 세팅
redGreenBlue = [[False for _ in range(n)] for _ in range(n)]
redGreen = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

# 그림 세팅
paint = []

for _ in range(n):
    row = list(input().rstrip())
    paint.append(row)

# 적록색약이 아닌 사람이 보는 구역의 수 찾기
redGreenBlueCount = 0

for i in range(n):
    for j in range(n):
        if not redGreenBlue[i][j]:
            redGreenBlue[i][j] = True
            queue.append((i, j))

            # 기준 색상 정하기
            color = paint[i][j]
            redGreenBlueCount += 1

            while queue:
                x, y = queue.popleft()

                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]

                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        if paint[nx][ny] == color and not redGreenBlue[nx][ny]:
                            redGreenBlue[nx][ny] = True
                            queue.append((nx, ny))

# 적록색약안 사람이 보는 구역의 수 찾기
redGreenCount = 0

for i in range(n):
    for j in range(n):
        if not redGreen[i][j]:
            redGreen[i][j] = True
            queue.append((i, j))

            # 기준 색상 정하기
            color = paint[i][j]
            redGreenCount += 1

            while queue:
                x, y = queue.popleft()

                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]

                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        # 파랑을 기준으로 구역을 찾을 때
                        if color == 'B':
                            if paint[nx][ny] == color and not redGreen[nx][ny]:
                                redGreen[nx][ny] = True
                                queue.append((nx, ny))
                        else:
                            if (paint[nx][ny] == 'R' or paint[nx][ny] == 'G') and not redGreen[nx][ny]:
                                redGreen[nx][ny] = True
                                queue.append((nx, ny))

print(redGreenBlueCount)
print(redGreenCount)
