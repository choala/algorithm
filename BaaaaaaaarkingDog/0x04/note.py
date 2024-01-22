MAX = 1000005
data = [-1 for _ in range(MAX)]
prev = [-1 for _ in range(MAX)]
next = [-1 for _ in range(MAX)]

# 새로 입주 가능한 번지
unused = 1

def traverse():
    # 0번지는 더미 노드
    # 첫 번째 번지를 cursor 변수에 할당
    cursor = next[0]
    while cursor != -1:
        print(data[cursor], end=" ")
        cursor = next[cursor]

    print("\n")

# addr 번지에 num을 입주시키는 함수
def insert(addr, num):
    global unused
    
    # 입주 절차
    # 1. 입주 가능한 번지에 num 할당
    data[unused] = num
    # 2. 이전 번지(addr)와 연결
    prev[unused] = addr
    # 3. 다음 번지와 연결
    next[unused] = next[addr]

    # 입주 소식 알리기
    # 1. 이전 번지(addr)의 next 변경
    next[addr] = unused
    # 2. 다음 번지의 prev 변경 (단, 빈 번지가 아닌 경우)
    if next[unused] != -1:
        prev[next[unused]] = unused

    # 입주 가능한 번지 변경
    unused += 1

def delete(addr):
    # 이전 하우스의 다음 번지를 변경
    next[prev[addr]] = next[addr]
    # 다음 하우스의 이전 번지를 변경 (단, 다음 하우스가 있는 경우)
    if next[addr] != -1:
        prev[next[addr]] = prev[addr]

def insert_test():
    print("insert_test() \n")
    insert(0, 10)
    traverse()
    insert(0, 30)
    traverse()
    insert(2, 40)
    traverse()
    insert(1, 20)
    traverse()
    insert(4, 70)
    traverse()

def delete_text():
    print("delete_test() \n")
    delete(1)
    traverse()
    delete(2)
    traverse()
    delete(4)
    traverse()
    delete(5)
    traverse()

insert_test()
delete_text()
