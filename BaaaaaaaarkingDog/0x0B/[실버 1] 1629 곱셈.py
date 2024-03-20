a, b, c = map(int, input().split())

def square_mod(a, b, c):
    if b == 1:
        return a % c

    val = square_mod(a, b // 2, c)
    val = val * val % c
    
    if b % 2 == 0:
        return val
    else:
        return val * a % c

print(square_mod(a, b, c))
