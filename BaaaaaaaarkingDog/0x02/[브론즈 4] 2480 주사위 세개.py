dice = [0 for _ in range(7)]
a, b, c = map(int, input().split())

flag = 0
dice[a] += 1
dice[b] += 1
dice[c] += 1

for i in range(len(dice)):
    if dice[i] == 3:
        print(10000 + i * 1000)
        flag = 1
    elif dice[i] == 2:
        print(1000 + i * 100)
        flag = 1

if flag == 0:
    print(max([a, b, c]) * 100)
