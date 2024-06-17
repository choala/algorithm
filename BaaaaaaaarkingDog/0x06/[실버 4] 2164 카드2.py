import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque(list(range(1, n + 1)))

count = 0
while len(queue) != 1:
    if count % 2 == 0:
        queue.popleft()
    else:
        queue.append(queue.popleft())

    count += 1

print(queue[0])
