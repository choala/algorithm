import sys

input = sys.stdin.readline

str = input().rstrip()
stack = []
isValid = True

while str != '.':
    for c in str:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                isValid = False
                break
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                isValid = False
                break

    if not stack and isValid:
        print("yes")
    else:
        print("no")

    str = input().rstrip()
    stack = []
    isValid = True
