import sys

input = sys.stdin.readline

n = int(input())
buildings = [int(input()) for _ in range(n)]

stack = []
result = 0

for building in buildings:
    while stack and stack[-1] <= building:
        # building의 옥상을 보지 못하는 경우, stack에서 제거
        # 즉, stack에는 building의 옥상을 볼 수 있는 케이스만 남게 됨
        stack.pop()

    stack.append(building)
    # buliding의 옥상을 볼 수 있는 케이스 중 자기 자신을 제외하고(-1) result에 더해줌
    result += len(stack) - 1

print(result)
