import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    array = input().rstrip()

    is_valid = True
    is_reversed = False

    parsed = array[1:-1].split(',')
    queue = deque(parsed) if parsed[0].isdigit() else deque()

    for command in p:
        # p는 10만보다 작거나 같음 > 'R'이 최대 10만 번 실행 가능하므로
        # 배열에 들어있는 수의 개수가 10만 개일 경우, 최대 100억 번의 연산이 수행됨
        # 따라서 실제로 뒤집지 않고, 뒤집는 것과 같은 효과를 낼 수 있는 방법이 필요
        if command == 'R':
            is_reversed = not is_reversed
        else:
            if queue:
                if is_reversed:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                is_valid = False
                break

    if is_valid:
        print('[', end='')
        
        if is_reversed:
            queue.reverse()

        print(','.join(queue), end='')
        
        print(']')
    else:
        print("error")
