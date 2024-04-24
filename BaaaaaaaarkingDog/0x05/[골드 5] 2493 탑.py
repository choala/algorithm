n = int(input())
tops = list(map(int, input().split()))

stack = []
results = []

for i, top in enumerate(tops):
    while stack:
        target = stack[-1]

        if target[0] < top:
            stack.pop()
        else:
            results.append(target[1])
            break
    else:
        results.append(0)

    stack.append((top, i + 1))
    

for result in results:
    print(result, end=' ')
