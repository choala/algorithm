from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    distance = [[-1 for _ in range(m)] for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    
    distance[0][0] = 1
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if maps[nx][ny] == 1 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
    
    return distance[n - 1][m - 1]
