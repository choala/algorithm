n = int(input())

board = []
count = 0

col_is_used = [False for _ in range(n)] # 열 단위로 퀸 존재 여부를 나타내는 리스트
g1_is_used = [False for _ in range(2 * n - 1)] # 기울기 1 직선 단위로 퀸 존재 여부를 나타내는 리스트 (x + y)
g2_is_used = [False for _ in range(2 * n - 1)] # 기울기 -1 직선 단위로 퀸 존재 여부를 나타내는 리스트 (x - y + n - 1)

# k 번째 행에 퀸을 두는 함수
def queen(k):
    global board
    global count
    
    if k == n:
        count += 1
        return

    # (k, c)에 퀸을 둘 수 있는지 판단
    for c in range(n):
        if not col_is_used[c] and not g1_is_used[k + c] and not g2_is_used[k - c + n - 1]:
            board.append((k, c))
            col_is_used[c] = True
            g1_is_used[k + c] = True
            g2_is_used[k - c + n - 1] = True

            queen(k + 1)

            board.pop()
            col_is_used[c] = False
            g1_is_used[k + c] = False
            g2_is_used[k - c + n - 1] = False
    
queen(0)

print(count)
