import sys
from collections import deque

input = sys.stdin.readline

# 수빈이(n)와 동생(k)의 위치 입력받기
n, k = map(int, input().split())

# BFS 세팅
pos = [-1 for _ in range(100001)]

dx = [-1, 1, 2]

queue = deque()

# 시작점(수빈이 위치) 설정
pos[n] = 0
queue.append(n)

while queue and pos[k] == -1:
    x = queue.popleft()

    for dir in range(3):
        nx = 0

        if dx[dir] == 2:
            nx = x * dx[dir]
        else:
            nx = x + dx[dir]

        if nx >= 0 and nx < 100001 and pos[nx] == -1:
            pos[nx] = pos[x] + 1
            queue.append(nx)

print(pos[k])
