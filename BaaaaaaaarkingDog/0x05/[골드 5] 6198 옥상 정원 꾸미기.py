import sys

input = sys.stdin.readline

n = int(input())
buildings = [int(input()) for _ in range(n)]

stack = []
tmp = []
results = []

for i, building in enumerate(reversed(buildings)):
    count = 0
    tmp = stack.copy()
    
    while tmp:
        target = tmp[-1]

        if target < building:
            tmp.pop()
            count += 1
        else:
            results.append(count)
            break
    else:
        results.append(count)

    stack.append(building)

print(sum(results))
