import sys

input = sys.stdin.readline

n = int(input())
heights = [int(input()) for _ in range(n)]

stack = []
cases = 0

for height in heights:
    index = len(stack) - 1
    
    while stack and index >= 0:
        target = stack[index]

        cases += 1
        if target < height:
            stack.pop()
            
        index -= 1
            
    stack.append(height)
    index += 1

print(cases)
