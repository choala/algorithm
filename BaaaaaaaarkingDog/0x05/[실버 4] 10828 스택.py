import sys

input = sys.stdin.readline

MAX = 10005
data = [-1 for _ in range(MAX)]
pos = 0

def push(x):
    global pos

    data[pos] = x
    pos += 1

def pop():
    global pos

    if size() > 0:
        pos -= 1
        return data[pos]
    else:
        return -1

def size():
    return pos

def empty():
    if size() == 0:
        return 1
    else:
        return 0

def top():
    global pos

    if empty() == 1:
        return -1
    else:
        return data[pos - 1]

n = int(input())
for _ in range(n):
    command = input().rstrip().split()

    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    else:
        print(top())
