import sys

MAX = 10005
data = [-1 for _ in range(2 * MAX + 1)]
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
    global head

    if head != tail:
        head += 1
        return data[head - 1]
    else:
        return -1

def pop_back():
    global tail

    if head != tail:
        tail -= 1
        return data[tail]
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

    if command[0] == "push_front":
        push_front(command[1])
    elif command[0] == "push_back":
        push_back(command[1])
    elif command[0] == "pop_front":
        print(pop_front())
    elif command[0] == "pop_back":
        print(pop_back())
    elif command[0] == "size":
        print(tail - head)
    elif command[0] == "empty":
        if tail == head:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        print(front())
    elif command[0] == "back":
        print(back())
