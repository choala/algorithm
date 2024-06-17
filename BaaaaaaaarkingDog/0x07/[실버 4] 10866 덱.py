import sys

input = sys.stdin.readline

MAX = 10005
data = [-1] * (2 * MAX + 1)
head, tail = MAX, MAX

def push_front(x):
    global head

    head -= 1
    data[head] = x

def push_back(x):
    global tail

    data[tail] = x
    tail += 1

def pop_front():
    global head, tail

    if head == tail:
        print(-1)
    else:
        print(data[head])
        head += 1

def pop_back():
    global head, tail

    if head == tail:
        print(-1)
    else:
        print(data[tail - 1])
        tail -= 1

def size():
    global head, tail

    print(tail - head)

def empty():
    global head, tail

    if head == tail:
        print(1)
    else:
        print(0)

def front():
    global head, tail

    if head == tail:
        print(-1)
    else:
        print(data[head])

def back():
    global head, tail

    if head == tail:
        print(-1)
    else:
        print(data[tail - 1])

n = int(input())
for _ in range(n):
    command = input().split()

    if command[0] == "push_front":
        push_front(command[1])
    elif command[0] == "push_back":
        push_back(command[1])
    elif command[0] == "pop_front":
        pop_front()
    elif command[0] == "pop_back":
        pop_back()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "front":
        front()
    else:
        back()
