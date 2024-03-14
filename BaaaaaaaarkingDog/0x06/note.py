MAX = 1000005
data = [-1 for _ in range(MAX)]
head, tail = 0, 0

def push(x):
    global tail
    
    data[tail] = x
    tail += 1

def pop():
    global head

    head += 1

def front():
    global head

    return data[head]

def back():
    global tail

    return data[tail - 1]
