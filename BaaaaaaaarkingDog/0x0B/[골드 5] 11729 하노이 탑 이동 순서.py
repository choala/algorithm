n = int(input())

print(2 ** n - 1)

# n개의 원판을 s에서 e로 옮기는 함수
def hanoi(s, e, n):
    # base condition
    if n == 1:
        print(s, e)
        return
        
    hanoi(s, 6 - s - e, n - 1)
    hanoi(s, e, 1)
    hanoi(6 - s - e, e, n - 1)

hanoi(1, 3, n)
