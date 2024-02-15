MAX = 5005
data = [-1 for _ in range(MAX)]
next = [-1 for _ in range(MAX)]
prev = [-1 for _ in range(MAX)]

unused = 1
cursor = 0
length = 0

def insert(pos, n):
    global unused

    data[unused] = n
    # 원형 연결 리스트로 구현하기 위해 끝에 추가되는 노드는 첫 노드와 연결
    if next[pos] == -1:
        next[unused] = next[0]
    else:
        next[unused] = next[pos]
    prev[unused] = pos

    next[pos] = unused
    prev[next[unused]] = unused

    unused += 1

def delete(pos):
    global length

    # 출력 형식을 맞추기 위해 조건에 따라 end 옵션의 값을 달리 함
    if length == 1:
        print(pos, end="")
    else:
        print(pos, end=", ")

    next[prev[pos]] = next[pos]
    if next[pos] != -1:
        prev[next[pos]] = prev[pos]

    length -= 1

n, k = map(int, input().split())
length = n

for i in range(n):
    insert(i, i + 1)

print("<", end="")
while length != 0:
    for _ in range(k):
        cursor = next[cursor]
    delete(cursor)
print(">")
