MAX = 1000005
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

    head += 1

def pop_back():
    global tail

    tail -= 1

def front():
    global head

    return data[head]

def back():
    global tail

    return data[tail - 1]
