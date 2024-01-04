num = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    tmp = list(reversed(num[a - 1:b]))
    num = num[0:a - 1] + tmp + num[b:20]

for i in range(20):
    print(num[i], end=" ")
