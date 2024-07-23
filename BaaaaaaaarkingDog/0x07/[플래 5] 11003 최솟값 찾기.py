import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())

a = [0]
d = [0]
a.extend(map(int, input().split()))

queue = deque()

for i in range(1, n + 1):
    if queue and i - l + 1 > queue[0][1]:
        queue.popleft()
    
    while queue:
        num, pos = queue[-1][0], queue[-1][1]

        if a[i] > num:
            d.append(queue[0][0])
            queue.append((a[i], i))
            break
        else:
            queue.pop()
    else:
        d.append(a[i])
        queue.append((a[i], i))
    
for i in range(1, n + 1):
    print(d[i], end=' ')
