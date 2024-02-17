import sys

input = sys.stdin.readline

MAX = 100005
data = [-1 for _ in range(MAX)]
pos = 0

sum = 0

def push(x):
    global pos
    
    data[pos] = x
    pos += 1

def pop():
    global pos
    
    pos -= 1

def top():
    global pos

    return data[pos - 1]

k = int(input())
for _ in range(k):
    n = int(input())

    if n == 0:
        pop()
    else:
        push(n)

for _ in range(pos):
    sum += top()
    pop()
    
print(sum)
