import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

stack = []
results = []

for ai in reversed(a):
    while stack:
        target = stack[-1]

        if target <= ai:
            stack.pop()
        else:
            results.append(target)
            break
    else:
        results.append(-1)

    stack.append(ai)

for result in reversed(results):
    print(result, end=' ')
