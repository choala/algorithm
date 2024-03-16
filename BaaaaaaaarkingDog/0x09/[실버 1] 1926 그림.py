import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# BFS 기본 세팅
board = []
visit = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = []

# board 기본 세팅
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

paint_count = 0
paint_max_area = 0

for i in range(n):
    for j in range(m):
        # 시작 지점 찾기
        if board[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            queue.append((i, j))
            
            paint_count += 1
            paint_area = 0

            while queue:
                x, y = queue.pop(0)
                paint_area += 1
                
                for direc in range(4):
                    nx = x + dx[direc]
                    ny = y + dy[direc]
    
                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if board[nx][ny] == 1 and visit[nx][ny] == 0:
                            visit[nx][ny] = 1
                            queue.append((nx, ny))
    
            if paint_max_area < paint_area:
                paint_max_area = paint_area
                
print(paint_count)
print(paint_max_area)
