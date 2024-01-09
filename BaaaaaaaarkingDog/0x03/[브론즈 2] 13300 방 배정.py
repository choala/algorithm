students = [[0 for _ in range(2)] for _ in range(6)]

n, k = map(int, input().split()) # n: 학생 수, k: 한 방당 최대 인원 수
for _ in range(n):
    s, y = map(int, input().split()) # s: 성별(여학생: 0, 남학생: 1), y: 학년
    students[y - 1][s] += 1

room = 0
for grade in students:
    room += grade[0] // k
    if grade[0] % k != 0:
        room += 1

    room += grade[1] // k
    if grade[1] % k != 0:
        room += 1
        
print(room)
