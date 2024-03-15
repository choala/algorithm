stack = []

s = input()
result = 0
before = ''

is_valid = True

for i in s:
    if i == '(' or i == '[':
        stack.append(i)
    else:
        if i == ')':
            if stack:
                # ()인 경우
                if before == '(':
                    stack.pop()
                    stack.append(2)
                # (X)인 경우
                else:
                    if stack[-1] == '[':
                        is_valid = False
                        break
                        
                    tmp = 0
                    popped = stack.pop()
    
                    while popped != '(':
                        tmp += popped

                        if stack:
                            popped = stack.pop()
                        else:
                            is_valid = False
                            break
    
                    stack.append(2 * tmp)
            else:
                is_valid = False
                break
        elif i == ']':
            if stack:
                # []인 경우
                if before == '[':
                    stack.pop()
                    stack.append(3)
                # [X]인 경우
                else:
                    if stack[-1] == '(':
                        is_valid = False
                        break
                        
                    tmp = 0
                    popped = stack.pop()
    
                    while popped != '[':
                        tmp += popped

                        if stack:
                            popped = stack.pop()
                        else:
                            is_valid = False
                            break
    
                    stack.append(3 * tmp)
            else:
                is_valid = False
                break
    before = i

for s in stack:
    if not isinstance(s, int):
        is_valid = False
        break

if is_valid:
    print(sum(stack))
else:
    print(0)
