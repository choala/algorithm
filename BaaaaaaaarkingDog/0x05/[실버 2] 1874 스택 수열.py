import sys

input = sys.stdin.readline

MAX = 100005
data = [-1 for _ in range(MAX)]
pos = 1

process = []
target = 1
flag = 0

def push(x):
    global pos

    data[pos] = x
    pos += 1

def pop():
    global pos

    if pos > 0:
        pos -= 1

def top():
    global pos

    return data[pos - 1]

n = int(input())
for _ in range(n):
    x = int(input())
    
    for i in range(target, 2 * n + 1):
        if i <= n:
            if i <= x:
                push(i)
                process.append("+")
                target += 1
            else:
                if top() == x:
                    pop()
                    process.append("-")
                    break
                else:
                    flag = 1
                    break
        else:
            if top() == x:
                pop()
                process.append("-")
                break
            else:
                flag = 1
                break

if flag == 1:
    print("NO")
else:
    for p in process:
        print(p)
