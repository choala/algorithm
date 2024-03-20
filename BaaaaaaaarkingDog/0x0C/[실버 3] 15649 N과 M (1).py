n, m = map(int, input().split())

sequence = [-1 for _ in range(10)]
is_used = [False for _ in range(10)]

# k개의 숫자가 선택된 상황에서 다음 k 번째 숫자를 정하는 함수
def next(k):
    # base condition
    if k == m:
        for i in range(m):
            print(sequence[i], end=' ')

        return

    for i in range(1, n + 1):
        if not is_used[i]:
            # k 번째 숫자 i 선택
            sequence[k] = i
            is_used[i] = True
            next(k + 1) 
            is_used[i] = False

next(0)
