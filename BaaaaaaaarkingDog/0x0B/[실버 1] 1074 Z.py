n, r, c = map(int, input().split())

# 2^n * 2^n 배열에서 (r, c)를 몇 번째로 방문하는지 반환하는 함수
def z(n, r, c):
    # base condition
    if n == 0:
        return 0

    length = 2 ** n
    half = 2 ** (n - 1)
    
    if r < half and c < half:
        return z(n - 1, r, c)
    elif r < half and c < length:
        return half * half * 1 + z(n - 1, r, c - half)
    elif r < length and c < half:
        return half * half * 2 + z(n - 1, r - half, c)
    else:
        return half * half * 3 + z(n - 1, r - half, c - half)

print(z(n, r, c))
