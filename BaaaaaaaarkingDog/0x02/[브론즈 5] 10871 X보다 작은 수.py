n, x = map(int, input().split())
a_arr = list(map(int, input().split()))

for a in a_arr:
    if a < x:
        print(a, end=" ")
