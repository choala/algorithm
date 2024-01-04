def func(x, y):
    print(y - x - 1)
    
    for i in range(x + 1, y):
        print(i, end=" ")

a, b = map(int, input().split())

if a > b:
    func(b, a)
elif a < b:
    func(a, b)
else:
    print(0)
