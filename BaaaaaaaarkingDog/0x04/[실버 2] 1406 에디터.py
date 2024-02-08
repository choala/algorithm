import sys

MAX = 600005
data = [-1 for _ in range(MAX)]
next = [-1 for _ in range(MAX)]
prev = [-1 for _ in range(MAX)]

unused = 1
cursor = 0

def traverse():
    target = next[0]

    while target != -1:    
        print(chr(data[target]), end="")
        target = next[target]

def insert(pos, char):
    global unused

    data[unused] = ord(char)
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

text = input()
for t in text:
    insert(cursor, t)
    cursor += 1

m = int(input())
for _ in range(m):
    command = sys.stdin.readline().rstrip().split()
    
    if len(command) == 1:
        if command[0] == "L" and prev[cursor] != -1:
            cursor = prev[cursor]
        elif command[0] == "D" and next[cursor] != -1:
            cursor = next[cursor]
        elif command[0] == "B" and prev[cursor] != -1:
            delete(cursor)
            cursor = prev[cursor]
    else:
        insert(cursor, command[1])
        cursor = next[cursor]

traverse()
