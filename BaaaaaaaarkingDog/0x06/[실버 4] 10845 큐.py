import sys

MAX = 10005
data = [-1 for _ in range(MAX)]
head, tail = 0, 0

def push(x):
    global tail

    data[tail] = x
    tail += 1

def pop():
    global head

    if head != tail:
        head += 1
        return data[head - 1]
    else:
        return -1

def front():
    global head

    return data[head] if head != tail else -1

def back():
    global tail

    return data[tail - 1] if head != tail else -1

n = int(input())

for _ in range(n):
    command = sys.stdin.readline().strip().split()

    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "size":
        print(tail - head)
    elif command[0] == "empty":
        if head == tail:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        print(front())
    elif command[0] == "back":
        print(back())
