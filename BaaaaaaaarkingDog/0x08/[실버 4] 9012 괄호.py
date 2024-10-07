import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    str = input().rstrip()

    stack = []
    is_valid = True

    for c in str:
        if c == '(':
            stack.append(c)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_valid = False
                break

    if not stack and is_valid:
        print("YES")
    else:
        print("NO")
