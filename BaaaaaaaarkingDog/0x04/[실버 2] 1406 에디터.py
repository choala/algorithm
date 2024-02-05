import sys

input = sys.stdin.readline().rstrip

MAX = 600005
data = [-1 for _ in range(MAX)]
next = [-1 for _ in range(MAX)]
prev = [-1 for _ in range(MAX)]

unused = 1

def traverse():
    start = next[0]

    while start != -1:
        print(chr(data[start]), end="")
        start = next[start]

def insert(pos, char):
    global unused

    data[unused] = ord(char)
    next[unused] = next[pos]
    prev[unused] = pos
    
    unused += 1

def delete(pos):
    next[prev[pos]] = next[pos]
    prev[next[pos]] = prev[pos]

text = input()
cursor = len(text)   
for t in text:
    insert(unused, t)

m = int(input())
for _ in range(m):
    command = input().split()

    if len(command) == 1:
        if command[0] == "L":
            cursor -= 1
        elif command[0] == "D":
            cursor += 1
        else:
            delete(cursor)
            
    else:
        insert(cursor, "$")
