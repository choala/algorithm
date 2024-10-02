import sys

input = sys.stdin.readline

str = input().rstrip()

stack = []
total = 0
tmp = 1

before = ''

for c in str:
    if c == '(':
        stack.append(c)
        tmp *= 2
    elif c == '[':
        stack.append(c)
        tmp *= 3
    elif c == ')' and stack and stack[-1] == '(':
        if before == '(':
            total += tmp
        
        stack.pop()
        tmp //= 2
    elif c == ']' and stack and stack[-1] == '[':
        if before == '[':
            total += tmp
            
        stack.pop()
        tmp //= 3
    else:
        total = 0
        break

    before = c

if stack:
    print(0)
else:
    print(total)
