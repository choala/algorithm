import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    a = input().rstrip()
    
    queue = deque()

    # [x1,...,xn]에서 숫자만 추출 > queue에 저장
    tmp = ''
    for i in a:
        if i.isdigit():
            tmp += i
        else:
            if tmp:
                queue.append(int(tmp))
                tmp = ''

    # 'R'과 'D'에 따라 배열 처리
    start_index = 0
    end_index = n - 1
    
    for command in p:
        # p는 10만보다 작거나 같음 > 'R'이 최대 10만 번 실행 가능하므로
        # 배열에 들어있는 수의 개수가 10만 개일 경우, 최대 100억 번의 연산이 수행됨
        # 즉, 실제로 뒤집지 않고 뒤집는 것과 같은 효과를 낼 수 있는 방법이 필요
        if command == 'R':
            start_index, end_index = end_index, start_index
        else:
            if start_index != end_index:
                if start_index < end_index:
                    start_index += 1
                else:
                    start_index -= 1
            else:
                break

    # 포맷에 맞게 출력
    if start_index != end_index:
        print('[', end='')
        
        if start_index < end_index:
            for i in range(start_index, end_index + 1):
                if i == end_index:
                    print(queue[i], end='')
                else:
                    print(queue[i], end=',')
        else:
            for i in range(start_index, end_index - 1, -1):
                if i == end_index:
                    print(queue[i], end='')
                else:
                    print(queue[i], end=',')
        
        print(']')
    else:
        print("error")
