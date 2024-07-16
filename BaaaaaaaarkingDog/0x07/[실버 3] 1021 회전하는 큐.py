import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
pick_list = list(map(int, input().split()))

queue = deque(range(1, n + 1))
count = 0

for pick in pick_list:
    while queue[0] != pick:
        # pick의 index와 queue의 전체 길이 비교 > 짧은 쪽으로 rotate
        index = queue.index(pick)
        
        if n - index > index:
            queue.rotate(-1)
        else:
            queue.rotate(1)
        
        count += 1
    else:
        queue.popleft()
        n -= 1

print(count)
