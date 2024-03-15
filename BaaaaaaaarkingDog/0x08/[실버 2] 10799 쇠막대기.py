stack = []

s = input()
pieces = 0
before = ''

for i in s:
    if i == '(':
        stack.append('(')
    else:
        stack.pop()
        
        # 레이저인 경우
        if before == '(':
            pieces += len(stack)
        # 쇠막대기인 경우
        else:
            pieces += 1
        
    before = i

print(pieces)
