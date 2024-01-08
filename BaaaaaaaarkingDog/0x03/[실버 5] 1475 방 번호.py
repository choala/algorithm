room_num = input()

num = [0 for _ in range(10)]
for i in room_num:
    if i == "6" or i == "9":
        if num[6] == num[9]:
            num[6] += 1
        else:
            num[9] += 1
    else:
        num[int(i)] += 1

print(max(num))
