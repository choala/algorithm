import sys

input = sys.stdin.readline

results = []

s = input().rstrip()
while s != '.':
    stack = []
    index = 0
    is_valid = True

    while index < len(s):
        if s[index] == '(' or s[index] == '[':
            stack.append(s[index])
        elif s[index] == ')' or s[index] == ']':
            if stack:
                top = stack[-1]

                if top == '(' and s[index] == ')':
                    stack.pop()
                elif top == '[' and s[index] == ']':
                    stack.pop()
                else:
                    is_valid = False
                    break
            else:
                is_valid = False
                break

        index += 1

    if stack:
        is_valid = False

    if is_valid:
        results.append("yes")
    else:
        results.append("no")

    s = input().rstrip()

for result in results:
    print(result)
