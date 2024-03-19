from collections import deque

n, k = map(int, input().split())

# BFS 기본 세팅
sec = [-1 for _ in range(200001)]
dx = [-1, 1, 2]

queue = deque()

# 수빈이의 시작점 큐에 삽입
sec[n] = 0
queue.append(n)

keep_finding = True

# 수빈이와 동생의 시작점이 같은 경우
if n == k:
    keep_finding = False

while queue and keep_finding:
    x = queue.popleft()

    for i in range(3):
        if i <= 1:
            nx = x + dx[i]
        else:
            nx = x * dx[i]

        if nx >= 0 and nx < 200001:
            # 해당 위치에 처음 도달하는 경우
            if sec[nx] == -1:
                sec[nx] = sec[x] + 1
                queue.append(nx)

            # 해당 위치에 동생이 있는 경우
            if nx == k:
                keep_finding = False

print(sec[k])
