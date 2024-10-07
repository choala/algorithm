import sys

input = sys.stdin.readline

n = int(input())

result = 0

for _ in range(n):
    str = input().rstrip()
    
    stack = []

    for c in str:
        if c == 'A':
            if stack and stack[-1] == 'A':
                stack.pop()
            else:
                stack.append('A')
        else:
            if stack and stack[-1] == 'B':
                stack.pop()
            else:
                stack.append('B')
            
    if not stack:
        result += 1

print(result)
