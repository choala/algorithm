import sys

MAX = 1000005
data = []
next = []
prev = []

unused = 0
cursor = 0

def init():
    global data, next, prev, unused, cursor
    
    data = [-1 for _ in range(MAX)]
    next = [-1 for _ in range(MAX)]
    prev = [-1 for _ in range(MAX)]
    
    unused = 1
    cursor = 0
    
def traverse():
    target = next[0]

    while target != -1:
        if next[target] != -1:
            print(data[target], end="")
        else:
            print(data[target])
            
        target = next[target]

def insert(pos, char):
    global unused
    
    data[unused] = char
    next[unused] = next[pos]
    prev[unused] = pos

    next[pos] = unused
    if next[unused] != -1:
        prev[next[unused]] = unused

    unused += 1

def delete(pos):
    next[prev[pos]] = next[pos]
    if next[pos] != -1:
        prev[next[pos]] = prev[pos]

input = sys.stdin.readline

case = int(input())
for _ in range(case):
    init()
    
    string = input().rstrip()
    
    for s in string:
        if s == "-":
            if prev[cursor] != -1:
                delete(cursor)
                cursor = prev[cursor]
        elif s == "<":
            if prev[cursor] != -1:
                cursor = prev[cursor]
        elif s == ">":
            if next[cursor] != -1:
                cursor = next[cursor]
        else:
            insert(cursor, s)
            cursor = next[cursor]

    traverse()
