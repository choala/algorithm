a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)
count = [0 for _ in range(10)]

for i in mul:
    count[int(i)] += 1

for c in count:
    print(c)
