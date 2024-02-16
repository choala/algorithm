MAX = 1000005
data = [-1 for _ in range(MAX)]
pos = 0

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
